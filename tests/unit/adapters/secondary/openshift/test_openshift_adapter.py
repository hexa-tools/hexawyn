from __future__ import annotations

from collections.abc import Mapping
from unittest.mock import Mock

import pytest
from hexawyn.adapters.secondary.openshift.openshift_adapter import (
    OpenShiftAdapter,
    _items,
    _mapping,
    _metadata,
    _to_image_stream,
    _to_project,
    _to_route,
    _to_scc,
    _translate_error,
)
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
)


def _context(name: str = "test-cluster", cluster: str = "test-cluster-api") -> ClusterContext:
    return {"name": name, "cluster": cluster, "provider": "openshift", "namespace": "default"}


def _dynamic_client(items: list[Mapping[str, object]] | None = None) -> Mock:
    client = Mock()
    payload = {"items": items or []}
    client.list_cluster_custom_object.return_value = payload
    client.list_namespaced_custom_object.return_value = payload
    return client


def _project_item(name: str, phase: str = "Active", display_name: str = "") -> dict[str, object]:
    return {
        "metadata": {"name": name},
        "status": {"phase": phase},
        "spec": {"displayName": display_name},
    }


def _route_item(
    name: str, namespace: str = "default", host: str = "", svc: str = ""
) -> dict[str, object]:
    return {
        "metadata": {"name": name, "namespace": namespace},
        "spec": {"host": host, "to": {"name": svc}},
    }


def _route_item_with_tls(
    name: str, namespace: str = "default", host: str = "", svc: str = ""
) -> dict[str, object]:
    return {
        "metadata": {"name": name, "namespace": namespace},
        "spec": {"host": host, "to": {"name": svc}, "tls": {}},
    }


def _scc_item(name: str, privileged_container: str = "unprivileged") -> dict[str, object]:
    if privileged_container == "privileged":
        return {
            "metadata": {"name": name},
            "allowPrivilegedContainer": True,
            "runAsUser": {"type": "RunAsAny"},
        }
    return {
        "metadata": {"name": name},
        "allowPrivilegedContainer": False,
        "runAsUser": {"type": "MustRunAsRange"},
    }


def _scc_item_custom(name: str, privileged: bool, run_as_type: str) -> dict[str, object]:
    return {
        "metadata": {"name": name},
        "allowPrivilegedContainer": privileged,
        "runAsUser": {"type": run_as_type},
    }


def _is_item(name: str, namespace: str = "default", tag_count: int = 0) -> dict[str, object]:
    item: dict[str, object] = {
        "metadata": {"name": name, "namespace": namespace},
        "status": {},
    }
    if tag_count > 0:
        item["status"]["tags"] = [{"tag": f"v{i}"} for i in range(tag_count)]
    return item


class TestOpenShiftAdapterDelegation:
    def test_list_pods_delegates(self) -> None:
        delegate = Mock(spec=K8sPort)
        delegate.list_pods.return_value = [PodInfo(name="pod1", namespace="ns1")]
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)
        result = adapter.list_pods("ns1")
        assert result[0]["name"] == "pod1"
        delegate.list_pods.assert_called_once_with("ns1")

    def test_list_namespaces_delegates(self) -> None:
        delegate = Mock(spec=K8sPort)
        delegate.list_namespaces.return_value = [
            NamespaceInfo(name="ns1", status="Active", age="1d")
        ]
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)
        result = adapter.list_namespaces()
        assert result[0]["name"] == "ns1"
        delegate.list_namespaces.assert_called_once()

    def test_get_cluster_metrics_delegates(self) -> None:
        delegate = Mock(spec=K8sPort)
        delegate.get_cluster_metrics.return_value = ClusterMetrics(
            cpu_usage_pct=50.0, memory_usage_pct=60.0, node_count=3, pod_count=10
        )
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)
        result = adapter.get_cluster_metrics()
        assert result["cpu_usage_pct"] == 50.0  # noqa: PLR2004
        delegate.get_cluster_metrics.assert_called_once()

    def test_get_cluster_context_returns_openshift_provider(self) -> None:
        ctx = _context("prod-eu", "api.prod-eu.example.com")
        adapter = OpenShiftAdapter(ctx)
        result = adapter.get_cluster_context()
        assert result["provider"] == "openshift"
        assert result["name"] == "prod-eu"
        assert result["cluster"] == "api.prod-eu.example.com"

    def test_get_cluster_context_falls_back_to_name_for_cluster(self) -> None:
        ctx = ClusterContext(
            name="my-cluster", cluster="my-cluster", provider="openshift", namespace="default"
        )
        ctx.pop("cluster")
        adapter = OpenShiftAdapter(ctx)
        result = adapter.get_cluster_context()
        assert result["cluster"] == "my-cluster"


class TestOpenShiftResourceOperations:
    def test_list_projects_returns_parsed_projects(self) -> None:
        client = _dynamic_client(
            [
                _project_item("my-project", "Active", "My Project"),
                _project_item("other", "Terminating"),
            ]
        )
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        result = adapter.list_projects()
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "my-project"
        assert result[0]["status"] == "Active"
        assert result[0]["display_name"] == "My Project"
        assert result[1]["status"] == "Terminating"

    def test_list_projects_empty(self) -> None:
        client = _dynamic_client([])
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        assert adapter.list_projects() == []

    def test_list_routes_returns_parsed_routes(self) -> None:
        client = _dynamic_client(
            [
                _route_item_with_tls("web-route", "default", "web.example.com", "web-svc"),
                _route_item("api-route", "api", "api.example.com", "api-svc"),
            ]
        )
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        result = adapter.list_routes("default")
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "web-route"
        assert result[0]["host"] == "web.example.com"
        assert result[0]["tls_enabled"] is True
        assert result[1]["tls_enabled"] is False

    def test_list_routes_empty(self) -> None:
        client = _dynamic_client([])
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        assert adapter.list_routes("default") == []

    def test_list_security_context_constraints_returns_parsed_sccs(self) -> None:
        client = _dynamic_client(
            [
                _scc_item("anyuid", privileged_container="unprivileged"),
                _scc_item_custom("privileged", True, "RunAsAny"),
            ]
        )
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        result = adapter.list_security_context_constraints()
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "anyuid"
        assert result[0]["allow_privileged_container"] is False
        assert result[1]["allow_privileged_container"] is True
        assert result[1]["run_as_user_type"] == "RunAsAny"

    def test_list_sccs_empty(self) -> None:
        client = _dynamic_client([])
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        assert adapter.list_security_context_constraints() == []

    def test_list_image_streams_returns_parsed_streams(self) -> None:
        client = _dynamic_client(
            [
                _is_item("my-app", "default", tag_count=3),
                _is_item("other-app", "default", tag_count=0),
            ]
        )
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        result = adapter.list_image_streams("default")
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "my-app"
        assert result[0]["tag_count"] == 3  # noqa: PLR2004
        assert result[1]["tag_count"] == 0

    def test_list_image_streams_empty(self) -> None:
        client = _dynamic_client([])
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        assert adapter.list_image_streams("default") == []

    def test_list_projects_403_raises_insufficient_permissions(self) -> None:
        client = Mock()
        exc = Exception()
        exc.status = 403  # type: ignore[attr-defined]
        client.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        with pytest.raises(InsufficientPermissionsError):
            adapter.list_projects()

    def test_list_routes_api_error_raises_cluster_unreachable(self) -> None:
        client = Mock()
        exc = Exception()
        exc.status = 500  # type: ignore[attr-defined]
        client.list_namespaced_custom_object.side_effect = exc
        adapter = OpenShiftAdapter(_context(), dynamic_client=client)
        with pytest.raises(ClusterUnreachableError):
            adapter.list_routes("default")


class TestHelperFunctions:
    def test_items_returns_list_of_mappings(self) -> None:
        payload: Mapping[str, object] = {"items": [{"name": "a"}, {"name": "b"}, "not-a-mapping"]}
        assert len(_items(payload)) == 2  # noqa: PLR2004

    def test_items_no_items_key_returns_empty(self) -> None:
        assert _items({}) == []

    def test_items_not_a_list_returns_empty(self) -> None:
        assert _items({"items": "not-alist"}) == []

    def test_metadata_returns_metadata_dict(self) -> None:
        assert _metadata({"metadata": {"name": "x"}}) == {"name": "x"}

    def test_metadata_missing_returns_empty_dict(self) -> None:
        assert _metadata({}) == {}

    def test_mapping_returns_nested_dict(self) -> None:
        assert _mapping({"spec": {"key": "val"}}, "spec") == {"key": "val"}

    def test_mapping_missing_returns_empty_dict(self) -> None:
        assert _mapping({}, "spec") == {}

    def test_to_project_default_values(self) -> None:
        item: dict[str, object] = {"metadata": {}}
        result = _to_project(item)
        assert result["name"] == ""
        assert result["status"] == "Unknown"
        assert result["display_name"] == ""

    def test_to_route_default_values(self) -> None:
        item: dict[str, object] = {"metadata": {}, "spec": {"to": {}}}
        result = _to_route(item)
        assert result["name"] == ""
        assert result["host"] == ""
        assert result["target_service"] == ""
        assert result["tls_enabled"] is False

    def test_to_scc_default_values(self) -> None:
        item: dict[str, object] = {"metadata": {}}
        result = _to_scc(item)
        assert result["name"] == ""
        assert result["allow_privileged_container"] is False
        assert result["run_as_user_type"] == ""

    def test_to_image_stream_default_values(self) -> None:
        item: dict[str, object] = {"metadata": {}}
        result = _to_image_stream(item)
        assert result["name"] == ""
        assert result["namespace"] == ""
        assert result["tag_count"] == 0

    def test_translate_error_403_with_namespace(self) -> None:
        exc = Exception()
        exc.status = 403  # type: ignore[attr-defined]
        result = _translate_error(exc, "routes", "ns1")
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_generic_with_namespace(self) -> None:
        exc = Exception()
        exc.status = 500  # type: ignore[attr-defined]
        result = _translate_error(exc, "routes", "ns1")
        assert isinstance(result, ClusterUnreachableError)
        assert "namespace" in result.context
