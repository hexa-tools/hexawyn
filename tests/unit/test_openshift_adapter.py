from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.application.ports.driven.openshift_resource_port import (
    OpenShiftResourcePort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_FORBIDDEN = 403


def _context(name: str = "ocp-prod", namespace: str = "default") -> ClusterContext:
    return {
        "name": name,
        "cluster": name,
        "provider": "openshift",
        "namespace": namespace,
    }


def _projects_payload() -> dict:
    return {
        "items": [
            {
                "metadata": {"name": "team-a"},
                "status": {"phase": "Active"},
                "spec": {"displayName": "Team A"},
            },
            {"metadata": {"name": "team-b"}, "status": {"phase": "Terminating"}},
        ]
    }


def _routes_payload() -> dict:
    return {
        "items": [
            {
                "metadata": {"name": "web", "namespace": "team-a"},
                "spec": {
                    "host": "web.apps.ocp.example.com",
                    "to": {"name": "web-svc"},
                    "tls": {"termination": "edge"},
                },
            }
        ]
    }


def _sccs_payload() -> dict:
    return {
        "items": [
            {
                "metadata": {"name": "restricted"},
                "allowPrivilegedContainer": False,
                "runAsUser": {"type": "MustRunAsRange"},
            }
        ]
    }


def _image_streams_payload() -> dict:
    return {
        "items": [
            {
                "metadata": {"name": "python", "namespace": "openshift"},
                "status": {"tags": [{"tag": "3.11"}, {"tag": "3.12"}]},
            }
        ]
    }


class TestPortImplementation:
    def test_is_a_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        adapter = OpenShiftAdapter(_context(), k8s_delegate=MagicMock(spec=K8sPort))

        assert isinstance(adapter, K8sPort)

    def test_is_an_openshift_resource_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        adapter = OpenShiftAdapter(_context(), k8s_delegate=MagicMock(spec=K8sPort))

        assert isinstance(adapter, OpenShiftResourcePort)


class TestK8sPortDelegation:
    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        delegate = MagicMock(spec=K8sPort)
        delegate.list_pods.return_value = [{"name": "p1", "namespace": "ns"}]
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)

        result = adapter.list_pods("ns")

        delegate.list_pods.assert_called_once_with("ns")
        assert result[0]["name"] == "p1"

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        delegate = MagicMock(spec=K8sPort)
        delegate.list_namespaces.return_value = [{"name": "ns", "status": "Active", "age": "1d"}]
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)

        assert adapter.list_namespaces()[0]["name"] == "ns"

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        delegate = MagicMock(spec=K8sPort)
        delegate.get_cluster_metrics.return_value = {
            "cpu_usage_pct": 1.0,
            "memory_usage_pct": 2.0,
            "node_count": 3,
            "pod_count": 4,
        }
        adapter = OpenShiftAdapter(_context(), k8s_delegate=delegate)

        assert adapter.get_cluster_metrics()["node_count"] == 3

    def test_defaults_to_vanilla_delegate_when_none_injected(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        vanilla_instance = MagicMock(spec=K8sPort)
        vanilla_instance.list_pods.return_value = []
        adapter = OpenShiftAdapter(_context("ocp-prod"))

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=vanilla_instance,
        ) as vanilla_cls:
            result = adapter.list_pods()

        vanilla_cls.assert_called_once_with("ocp-prod")
        assert result == []


class TestClusterContext:
    def test_reports_openshift_provider(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        adapter = OpenShiftAdapter(
            _context("ocp-prod", namespace="team-a"),
            k8s_delegate=MagicMock(spec=K8sPort),
        )

        result = adapter.get_cluster_context()

        assert result["provider"] == "openshift"
        assert result["namespace"] == "team-a"

    def test_falls_back_to_name_when_cluster_short_name_missing(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter

        context: ClusterContext = {
            "name": "ocp-prod",
            "cluster": "",
            "provider": "openshift",
            "namespace": "default",
        }
        adapter = OpenShiftAdapter(context, k8s_delegate=MagicMock(spec=K8sPort))

        assert adapter.get_cluster_context()["cluster"] == "ocp-prod"


class TestListProjects:
    def test_maps_projects(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_cluster_custom_object.return_value = _projects_payload()
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        projects = adapter.list_projects()

        assert projects[0] == {
            "name": "team-a",
            "status": "Active",
            "display_name": "Team A",
        }
        assert projects[1]["display_name"] == ""

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_cluster_custom_object.side_effect = _api_exception(_FORBIDDEN)
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_projects()

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_cluster_custom_object.side_effect = _api_exception(500)
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        with pytest.raises(ClusterUnreachableError):
            adapter.list_projects()


class TestListRoutes:
    def test_maps_routes(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_namespaced_custom_object.return_value = _routes_payload()
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        routes = adapter.list_routes("team-a")

        assert routes[0]["host"] == "web.apps.ocp.example.com"
        assert routes[0]["target_service"] == "web-svc"
        assert routes[0]["tls_enabled"] is True

    def test_route_without_tls_is_not_tls_enabled(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "api", "namespace": "team-a"},
                    "spec": {"host": "h"},
                }
            ]
        }
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        routes = adapter.list_routes("team-a")

        assert routes[0]["tls_enabled"] is False
        assert routes[0]["target_service"] == ""

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter

        client = MagicMock()
        client.list_namespaced_custom_object.side_effect = _api_exception(_FORBIDDEN)
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_routes("team-a")

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter

        client = MagicMock()
        client.list_namespaced_custom_object.side_effect = _api_exception(500)
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        with pytest.raises(ClusterUnreachableError):
            adapter.list_routes("team-a")


class TestListSecurityContextConstraints:
    def test_maps_sccs(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_cluster_custom_object.return_value = _sccs_payload()
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        sccs = adapter.list_security_context_constraints()

        assert sccs[0]["name"] == "restricted"
        assert sccs[0]["allow_privileged_container"] is False
        assert sccs[0]["run_as_user_type"] == "MustRunAsRange"


class TestListImageStreams:
    def test_maps_image_streams(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )

        client = MagicMock()
        client.list_namespaced_custom_object.return_value = _image_streams_payload()
        adapter = OpenShiftAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), dynamic_client=client
        )

        streams = adapter.list_image_streams("openshift")

        assert streams[0]["name"] == "python"
        assert streams[0]["tag_count"] == 2


class TestLazyClientCreation:
    def test_creates_custom_objects_api_when_not_injected(self) -> None:
        from hexawyn.adapters.secondary.openshift import openshift_adapter as module

        adapter = module.OpenShiftAdapter(_context(), k8s_delegate=MagicMock(spec=K8sPort))
        fake_api = MagicMock()
        fake_api.list_cluster_custom_object.return_value = {"items": []}
        fake_k8s = MagicMock()
        fake_k8s.CustomObjectsApi.return_value = fake_api

        with patch.dict("sys.modules", {"kubernetes": MagicMock(client=fake_k8s)}):
            result = adapter.list_projects()

        assert result == []
        fake_k8s.CustomObjectsApi.assert_called_once_with()


def _api_exception(status: int) -> Exception:
    exc = Exception("api error")
    exc.status = status  # type: ignore[attr-defined]
    return exc
