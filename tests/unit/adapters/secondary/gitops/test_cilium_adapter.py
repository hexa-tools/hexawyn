from __future__ import annotations

import types
from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.gitops import cilium_adapter as ca
from hexawyn.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)
from kubernetes.client.exceptions import ApiException


def _make_vanilla(
    daemonsets: object = None,
    crds: object = None,
    pods: object = None,
    configmap: object = None,
) -> MagicMock:
    vanilla = MagicMock()

    crd_api = MagicMock()
    if isinstance(crds, Exception):
        crd_api.list_cluster_custom_object.side_effect = crds
    else:
        crd_api.list_cluster_custom_object.return_value = crds
    vanilla._crd_api_client.return_value = crd_api

    apps_api = MagicMock()
    if isinstance(daemonsets, Exception):
        apps_api.list_daemon_set_for_all_namespaces.side_effect = daemonsets
    else:
        apps_api.list_daemon_set_for_all_namespaces.return_value = daemonsets
    vanilla._apps_api_client.return_value = apps_api

    core_api = MagicMock()
    core_api.list_namespaced_pod.return_value = pods
    core_api.read_namespaced_config_map.return_value = configmap
    vanilla._api_client.return_value = core_api

    return vanilla


def _daemonset(meta: dict, containers: list[dict], status: dict) -> dict:
    return {
        "metadata": meta,
        "spec": {"template": {"spec": {"containers": containers}}},
        "status": status,
    }


def _daemonset_response(items: list[dict]) -> dict:
    return {"items": items}


def _ready_pod(name: str, node: str, image: str, restart: int = 0) -> dict:
    return {
        "metadata": {"name": name, "namespace": "kube-system"},
        "spec": {"nodeName": node},
        "status": {
            "phase": "Running",
            "containerStatuses": [
                {
                    "name": "cilium-agent",
                    "ready": True,
                    "restartCount": restart,
                    "image": image,
                    "state": {},
                }
            ],
        },
    }


def _not_ready_pod(name: str, node: str, image: str, restart: int = 0) -> dict:
    return {
        "metadata": {"name": name, "namespace": "kube-system"},
        "spec": {"nodeName": node},
        "status": {
            "phase": "Running",
            "containerStatuses": [
                {
                    "name": "cilium-agent",
                    "ready": False,
                    "restartCount": restart,
                    "image": image,
                    "state": {"waiting": {"message": "agent not ready"}},
                }
            ],
        },
    }


def _pod_response(items: list[dict]) -> dict:
    return {"items": items}


def _configmap(data: dict) -> dict:
    return {"data": data}


class TestCiliumAdapter:
    def test_implements_cilium_port(self) -> None:
        adapter = CiliumAdapter(MagicMock())
        assert isinstance(adapter, CiliumPort)

    def test_detect_installed_with_agents(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 2, "numberReady": 2},
                )
            ]
        )
        pods = _pod_response(
            [
                _ready_pod("cilium-a", "node-1", "quay.io/cilium/cilium:v1.16.3"),
                _ready_pod("cilium-b", "node-2", "quay.io/cilium/cilium:v1.16.3"),
            ]
        )
        vanilla = _make_vanilla(daemonsets=ds, crds={"items": []}, pods=pods, configmap={})

        result = CiliumAdapter(vanilla).detect()

        assert result.installed is True
        assert result.status == "installed"
        assert result.version == "v1.16.3"
        assert result.namespace == "kube-system"
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.degraded_summary is None

    def test_detect_version_raw_preserved(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.0-pre.1"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _make_vanilla(daemonsets=ds, crds={"items": []}, pods={"items": []}, configmap={})

        result = CiliumAdapter(vanilla).detect()

        assert result.version == "v1.16.0-pre.1"

    def test_detect_degraded_when_agents_not_ready(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 3, "numberReady": 2},
                )
            ]
        )
        pods = _pod_response(
            [
                _ready_pod("cilium-a", "node-1", "quay.io/cilium/cilium:v1.16.3"),
                _not_ready_pod("cilium-b", "node-2", "quay.io/cilium/cilium:v1.16.3"),
                _ready_pod("cilium-c", "node-3", "quay.io/cilium/cilium:v1.16.3"),
            ]
        )
        vanilla = _make_vanilla(daemonsets=ds, crds={"items": []}, pods=pods, configmap={})

        result = CiliumAdapter(vanilla).detect()

        assert result.status == "degraded"
        assert result.total_agents == 3  # noqa: PLR2004
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.degraded_summary == "2/3 agents ready"

    def test_detect_mode_native_routing(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap=_configmap({"routing-mode": "native"}),
        )

        result = CiliumAdapter(vanilla).detect()

        assert result.mode == "native-routing"

    def test_detect_mode_tunnel_via_routing_mode_key(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap=_configmap({"routing-mode": "tunnel"}),
        )

        result = CiliumAdapter(vanilla).detect()

        assert result.mode == "tunnel"

    def test_detect_mode_unknown_when_configmap_missing(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).detect()

        assert result.mode == "UNKNOWN"

    def test_detect_not_installed_when_no_daemonset_and_no_crds(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )
        crd_api = vanilla._crd_api_client.return_value
        err = MagicMock()
        err.status = 404
        crd_api.list_cluster_custom_object.side_effect = err

        result = CiliumAdapter(vanilla).detect()

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.version is None
        assert result.note is not None

    def test_detect_installed_via_crds_when_no_daemonset(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": [{"kind": "CiliumNode"}]},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).detect()

        assert result.installed is True
        assert result.note is not None

    def test_detect_rbac_403_raises_insufficient_permissions(self) -> None:
        err = MagicMock()
        err.status = 403
        vanilla = _make_vanilla(
            daemonsets=err, crds={"items": []}, pods={"items": []}, configmap={}
        )

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).detect()

    def test_detect_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=RuntimeError("connection refused"),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).detect()

    def test_parse_image_version(self) -> None:
        assert CiliumAdapter._parse_image_version("quay.io/cilium/cilium:v1.16.3") == "v1.16.3"
        assert CiliumAdapter._parse_image_version("quay.io/cilium/cilium") is None
        assert CiliumAdapter._parse_image_version("") is None
        assert CiliumAdapter._parse_image_version("quay.io/cilium/cilium@sha256:abc") is None
        assert (
            CiliumAdapter._parse_image_version("quay.io/cilium/cilium:v1.16.0-pre.1")
            == "v1.16.0-pre.1"
        )


def _build_vanilla(  # noqa: PLR0913
    daemonsets: object,
    crds: object,
    pods: object,
    configmap: object,
    pod_error: Exception | None = None,
    configmap_error: Exception | None = None,
) -> MagicMock:
    vanilla = MagicMock()
    apps_api = MagicMock()
    apps_api.list_daemon_set_for_all_namespaces.return_value = daemonsets
    vanilla._apps_api_client.return_value = apps_api

    crd_api = MagicMock()
    crd_api.list_cluster_custom_object.return_value = crds
    vanilla._crd_api_client.return_value = crd_api

    core_api = MagicMock()
    if pod_error is not None:
        core_api.list_namespaced_pod.side_effect = pod_error
    else:
        core_api.list_namespaced_pod.return_value = pods
    if configmap_error is not None:
        core_api.read_namespaced_config_map.side_effect = configmap_error
    else:
        core_api.read_namespaced_config_map.return_value = configmap
    vanilla._api_client.return_value = core_api
    return vanilla


class TestCiliumAdapterAdditional:
    def test_detect_timeout_raises_adapter_timeout(self) -> None:
        err = TimeoutError("request timed out")
        vanilla = _make_vanilla(
            daemonsets=err, crds={"items": []}, pods={"items": []}, configmap={}
        )
        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).detect()

    def test_detect_rbac_exception_raises_insufficient_permissions(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=ApiException(status=403),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )
        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).detect()

    def test_detect_crd_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=RuntimeError("connection refused"),
            pods={"items": []},
            configmap={},
        )
        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).detect()

    def test_detect_not_installed_on_crd_404_exception(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=ApiException(status=404),
            pods={"items": []},
            configmap={},
        )
        result = CiliumAdapter(vanilla).detect()
        assert result.installed is False
        assert result.status == "not_installed"

    def test_detect_version_none_when_container_name_mismatch(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "not-cilium", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _build_vanilla(ds, {"items": []}, {"items": []}, {})
        result = CiliumAdapter(vanilla).detect()
        assert result.installed is True
        assert result.version is None

    def test_detect_version_none_when_no_container_definition(self) -> None:
        ds = _daemonset_response(
            [
                {
                    "metadata": {"name": "cilium", "namespace": "kube-system"},
                    "spec": {"template": {"spec": {}}},
                    "status": {"desiredNumberScheduled": 1, "numberReady": 1},
                }
            ]
        )
        vanilla = _build_vanilla(ds, {"items": []}, {"items": []}, {})
        result = CiliumAdapter(vanilla).detect()
        assert result.version is None

    def test_detect_mode_via_tunnel_key(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _build_vanilla(ds, {"items": []}, {"items": []}, _configmap({"tunnel": "vxlan"}))
        result = CiliumAdapter(vanilla).detect()
        assert result.mode == "tunnel"

    def test_detect_mode_unknown_when_no_relevant_key(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _build_vanilla(ds, {"items": []}, {"items": []}, _configmap({"foo": "bar"}))
        result = CiliumAdapter(vanilla).detect()
        assert result.mode == "UNKNOWN"

    def test_detect_mode_unknown_when_configmap_read_fails(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 1, "numberReady": 1},
                )
            ]
        )
        vanilla = _build_vanilla(ds, {"items": []}, {"items": []}, {}, configmap_error=RuntimeError)
        result = CiliumAdapter(vanilla).detect()
        assert result.mode == "UNKNOWN"

    def test_detect_mode_unknown_when_namespace_not_string(self) -> None:
        assert CiliumAdapter(MagicMock())._detect_mode(None) == "UNKNOWN"

    def test_list_agents_empty_when_namespace_not_string(self) -> None:
        assert CiliumAdapter(MagicMock())._list_agents(None) == []

    def test_list_agents_empty_when_pod_list_fails(self) -> None:
        vanilla = _build_vanilla(
            {"items": []}, {"items": []}, {"items": []}, {}, pod_error=RuntimeError
        )
        assert CiliumAdapter(vanilla)._list_agents("kube-system") == []

    def test_parse_pod_skips_unrelated_containers(self) -> None:
        pod = {
            "metadata": {"name": "cilium-abc", "namespace": "kube-system"},
            "spec": {"nodeName": "node-1"},
            "status": {
                "phase": "Running",
                "containerStatuses": [
                    {"name": "istio-proxy", "ready": False, "restartCount": 9, "image": "x"},
                    {
                        "name": "cilium-agent",
                        "ready": True,
                        "restartCount": 1,  # noqa: PLR2004
                        "image": "quay.io/cilium/cilium:v1.16.3",
                        "state": {},
                    },
                ],
            },
        }
        agent = CiliumAdapter._parse_pod(pod)
        assert agent.ready is True
        assert agent.restart_count == 1  # noqa: PLR2004
        assert agent.image == "quay.io/cilium/cilium:v1.16.3"


class TestCiliumHelpers:
    def test_to_snake_converts_camel_case(self) -> None:
        assert ca._to_snake("nodeName") == "node_name"

    def test_get_reads_object_snake_case_attr(self) -> None:
        obj = types.SimpleNamespace(restart_count=3)  # noqa: PLR2004
        assert ca._get(obj, "restartCount") == 3  # noqa: PLR2004

    def test_get_returns_none_for_none(self) -> None:
        assert ca._get(None, "key") is None

    def test_items_returns_empty_for_none(self) -> None:
        assert ca._items(None) == []

    def test_safe_int_none_is_zero(self) -> None:
        assert ca._safe_int(None) == 0

    def test_safe_int_bool(self) -> None:
        assert ca._safe_int(True) == 1

    def test_safe_int_numeric_string(self) -> None:
        assert ca._safe_int("5") == 5  # noqa: PLR2004

    def test_safe_int_invalid_string_is_zero(self) -> None:
        assert ca._safe_int("abc") == 0


class TestCiliumStatus:
    def test_status_healthy_when_all_ready(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 2, "numberReady": 2},
                )
            ]
        )
        pods = _pod_response(
            [
                _ready_pod("cilium-a", "node-1", "quay.io/cilium/cilium:v1.16.3"),
                _ready_pod("cilium-b", "node-2", "quay.io/cilium/cilium:v1.16.3"),
            ]
        )
        vanilla = _make_vanilla(daemonsets=ds, crds={"items": []}, pods=pods, configmap={})

        result = CiliumAdapter(vanilla).status()

        assert result.installed is True
        assert result.status == "healthy"
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.degraded_summary is None
        assert result.controller_errors == 0
        assert result.connectivity == "ok"

    def test_status_degraded_when_some_down(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 2, "numberReady": 1},
                )
            ]
        )
        pods = _pod_response(
            [
                _ready_pod("cilium-a", "node-1", "quay.io/cilium/cilium:v1.16.3"),
                _not_ready_pod("cilium-b", "node-2", "quay.io/cilium/cilium:v1.16.3"),
            ]
        )
        vanilla = _make_vanilla(daemonsets=ds, crds={"items": []}, pods=pods, configmap={})

        result = CiliumAdapter(vanilla).status()

        assert result.status == "degraded"
        assert result.degraded_summary == "1/2 agents ready"
        assert result.controller_errors == 1  # noqa: PLR2004
        assert result.connectivity == "degraded"
        assert len(result.nodes) == 2  # noqa: PLR2004

    def test_status_not_installed(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=ApiException(status=404),
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).status()

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.nodes == []
        assert result.note is not None

    def test_status_crds_only(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": [{"kind": "CiliumNode"}]},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).status()

        assert result.installed is True
        assert result.status == "unknown"
        assert result.note is not None

    def test_status_not_installed_when_crds_empty(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).status()

        assert result.installed is False
        assert result.status == "not_installed"

    def test_status_crd_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=RuntimeError("connection refused"),
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).status()

    def test_status_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=RuntimeError("connection refused"),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).status()

    def test_status_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=TimeoutError("request timed out"),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).status()

    def test_status_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=ApiException(status=403),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).status()
