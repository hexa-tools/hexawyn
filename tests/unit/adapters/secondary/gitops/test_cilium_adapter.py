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
    ResourceNotFoundError,
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


def _netpol_item(name: str, spec: dict, namespace: str | None = None) -> dict:
    metadata: dict[str, object] = {"name": name}
    if namespace is not None:
        metadata["namespace"] = namespace
    return {"metadata": metadata, "spec": spec}


def _make_netpol_vanilla(namespaced: object, clusterwide: object) -> MagicMock:
    vanilla = MagicMock()
    crd_api = MagicMock()

    def dispatch(plural: str, **kwargs: object) -> object:
        if plural == "ciliumnetworkpolicies":
            if isinstance(namespaced, Exception):
                raise namespaced
            return namespaced
        if plural == "ciliumclusterwidenetworkpolicies":
            if isinstance(clusterwide, Exception):
                raise clusterwide
            return clusterwide
        raise AssertionError(f"unexpected plural {plural}")

    crd_api.list_cluster_custom_object.side_effect = dispatch
    vanilla._crd_api_client.return_value = crd_api
    vanilla._apps_api_client.return_value = MagicMock()
    vanilla._api_client.return_value = MagicMock()
    return vanilla


class TestCiliumNetworkPolicies:
    def test_lists_both_kinds_with_summary(self) -> None:
        namespaced = {
            "items": [
                _netpol_item(
                    "allow-db",
                    {
                        "endpointSelector": {"matchLabels": {"app": "db"}},
                        "ingress": [{"toPorts": [{"rules": {"http": {}}}]}],
                        "egress": [{}],
                    },
                    namespace="payments",
                )
            ]
        }
        clusterwide = {"items": [_netpol_item("global-allow", {}, namespace=None)]}
        vanilla = _make_netpol_vanilla(namespaced, clusterwide)

        result = CiliumAdapter(vanilla).list_network_policies()

        assert result.installed is True
        assert result.status == "present"
        assert result.total_policies == 2  # noqa: PLR2004
        assert result.namespaced_count == 1  # noqa: PLR2004
        assert result.clusterwide_count == 1  # noqa: PLR2004
        namespaced_policy = result.policies[0]
        assert namespaced_policy.kind == "CiliumNetworkPolicy"
        assert namespaced_policy.namespace == "payments"
        assert namespaced_policy.endpoint_selector == "matchLabels: app=db"
        assert namespaced_policy.l7_rule_count == 1  # noqa: PLR2004
        assert namespaced_policy.l7_protocols == ("http",)
        assert result.policies[1].kind == "CiliumClusterwideNetworkPolicy"

    def test_empty_when_no_policies(self) -> None:
        vanilla = _make_netpol_vanilla({"items": []}, {"items": []})

        result = CiliumAdapter(vanilla).list_network_policies()

        assert result.installed is True
        assert result.status == "empty"
        assert result.total_policies == 0
        assert result.note is not None

    def test_not_installed_when_group_absent(self) -> None:
        vanilla = _make_netpol_vanilla(ApiException(status=404), ApiException(status=404))

        result = CiliumAdapter(vanilla).list_network_policies()

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.policies == []
        assert result.note is not None

    def test_one_kind_absent(self) -> None:
        clusterwide = {"items": [_netpol_item("global-allow", {})]}
        vanilla = _make_netpol_vanilla(ApiException(status=404), clusterwide)

        result = CiliumAdapter(vanilla).list_network_policies()

        assert result.installed is True
        assert result.clusterwide_count == 1  # noqa: PLR2004
        assert result.namespaced_count == 0

    def test_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_netpol_vanilla(ApiException(status=403), {"items": []})

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).list_network_policies()

    def test_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_netpol_vanilla(RuntimeError("connection refused"), {"items": []})

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).list_network_policies()

    def test_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_netpol_vanilla(TimeoutError("timed out"), {"items": []})

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).list_network_policies()


def _policy_raw(name: str, spec: dict, namespace: str | None = None) -> dict:
    metadata: dict[str, object] = {"name": name}
    if namespace is not None:
        metadata["namespace"] = namespace
    return {"metadata": metadata, "spec": spec}


def _make_get_vanilla(list_result: object, namespaced: object, clusterwide: object) -> MagicMock:
    vanilla = MagicMock()
    crd_api = MagicMock()
    if isinstance(list_result, Exception):
        crd_api.list_cluster_custom_object.side_effect = list_result
    else:
        crd_api.list_cluster_custom_object.return_value = list_result
    if isinstance(namespaced, Exception):
        crd_api.get_namespaced_custom_object.side_effect = namespaced
    else:
        crd_api.get_namespaced_custom_object.return_value = namespaced
    if isinstance(clusterwide, Exception):
        crd_api.get_cluster_custom_object.side_effect = clusterwide
    else:
        crd_api.get_cluster_custom_object.return_value = clusterwide
    vanilla._crd_api_client.return_value = crd_api
    vanilla._apps_api_client.return_value = MagicMock()
    vanilla._api_client.return_value = MagicMock()
    return vanilla


class TestCiliumGetNetworkPolicy:
    def test_get_namespaced_policy(self) -> None:
        raw = _policy_raw(
            "allow-db",
            {
                "endpointSelector": {"matchLabels": {"app": "db"}},
                "ingress": [{"toPorts": [{"rules": {"http": {}}}]}],
            },
            namespace="payments",
        )
        vanilla = _make_get_vanilla({"items": []}, raw, None)

        detail = CiliumAdapter(vanilla).get_network_policy("allow-db", "payments")

        assert detail.installed is True
        assert detail.kind == "CiliumNetworkPolicy"
        assert detail.namespace == "payments"
        assert detail.name == "allow-db"
        assert detail.endpoint_selector == "matchLabels: app=db"
        assert detail.ingress_rules[0].l7[0].protocol == "http"

    def test_get_clusterwide_policy(self) -> None:
        raw = _policy_raw("global-allow", {"endpointSelector": {"matchLabels": {}}})
        vanilla = _make_get_vanilla({"items": []}, None, raw)

        detail = CiliumAdapter(vanilla).get_network_policy("global-allow", None)

        assert detail.kind == "CiliumClusterwideNetworkPolicy"
        assert detail.namespace is None
        assert detail.name == "global-allow"

    def test_get_not_found_raises_resource_not_found(self) -> None:
        vanilla = _make_get_vanilla({"items": []}, ApiException(status=404), None)

        with pytest.raises(ResourceNotFoundError):
            CiliumAdapter(vanilla).get_network_policy("missing", "payments")

    def test_get_not_installed_returns_marker(self) -> None:
        vanilla = _make_get_vanilla(ApiException(status=404), None, None)

        detail = CiliumAdapter(vanilla).get_network_policy("x", "payments")

        assert detail.installed is False
        assert detail.status == "not_installed"

    def test_get_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_get_vanilla({"items": []}, ApiException(status=403), None)

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).get_network_policy("x", "ns")

    def test_get_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_get_vanilla({"items": []}, RuntimeError("connection refused"), None)

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).get_network_policy("x", "ns")

    def test_get_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_get_vanilla({"items": []}, None, TimeoutError("timed out"))

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).get_network_policy("x", None)


def _audit_policy_raw(
    name: str,
    labels: dict[str, str],
    ingress: int = 0,
    egress: int = 0,
    l7: int = 0,
) -> dict:
    spec: dict[str, object] = {"endpointSelector": {"matchLabels": labels}}
    if ingress:
        spec["ingress"] = [{"toPorts": [{"rules": {"http": {}}}]}] if l7 else [{}]
    if egress:
        spec["egress"] = [{}]
    return {"metadata": {"name": name}, "spec": spec}


def _pod_raw(namespace: str, name: str, labels: dict[str, str]) -> dict:
    return {"metadata": {"namespace": namespace, "name": name, "labels": labels}}


def _make_audit_vanilla(list_result: object, pods_response: object) -> MagicMock:
    vanilla = MagicMock()
    crd_api = MagicMock()
    if isinstance(list_result, Exception):
        crd_api.list_cluster_custom_object.side_effect = list_result
    else:
        crd_api.list_cluster_custom_object.return_value = list_result
    vanilla._crd_api_client.return_value = crd_api
    core_api = MagicMock()
    if isinstance(pods_response, Exception):
        core_api.list_pod_for_all_namespaces.side_effect = pods_response
    else:
        core_api.list_pod_for_all_namespaces.return_value = pods_response
    vanilla._api_client.return_value = core_api
    vanilla._apps_api_client.return_value = MagicMock()
    return vanilla


class TestCiliumPolicyAudit:
    def test_audit_flags_workload_without_policy(self) -> None:
        list_result = {
            "items": [_audit_policy_raw("allow-db", {"app": "db"}, ingress=1, egress=1, l7=1)]
        }
        pods = {
            "items": [
                _pod_raw("payments", "db-0", {"app": "db"}),
                _pod_raw("payments", "web-0", {"app": "web"}),
                {"no-metadata": True},
            ]
        }
        vanilla = _make_audit_vanilla(list_result, pods)

        result = CiliumAdapter(vanilla).audit_policies()

        assert result.status == "gaps_found"
        assert result.view == "cilium"
        assert result.total_workloads == 2  # noqa: PLR2004
        assert result.findings[0].coverage == "no_policy"
        assert result.findings[0].workload == "web-0"

    def test_audit_fully_covered(self) -> None:
        list_result = {
            "items": [_audit_policy_raw("allow-db", {"app": "db"}, ingress=1, egress=1, l7=1)]
        }
        pods = {"items": [_pod_raw("payments", "db-0", {"app": "db"})]}
        vanilla = _make_audit_vanilla(list_result, pods)

        result = CiliumAdapter(vanilla).audit_policies()

        assert result.status == "covered"
        assert result.findings == []

    def test_audit_l7_gap(self) -> None:
        list_result = {"items": [_audit_policy_raw("allow-db", {"app": "db"}, ingress=1, egress=1)]}
        pods = {"items": [_pod_raw("payments", "db-0", {"app": "db"})]}
        vanilla = _make_audit_vanilla(list_result, pods)

        result = CiliumAdapter(vanilla).audit_policies()

        assert result.findings[0].coverage == "l7_gap"
        assert result.findings[0].l7_restricted is False

    def test_audit_partial_restriction(self) -> None:
        list_result = {"items": [_audit_policy_raw("allow-db", {"app": "db"}, ingress=1)]}
        pods = {"items": [_pod_raw("payments", "db-0", {"app": "db"})]}
        vanilla = _make_audit_vanilla(list_result, pods)

        result = CiliumAdapter(vanilla).audit_policies()

        assert result.findings[0].coverage == "partial"

    def test_audit_not_installed_returns_vanilla_view(self) -> None:
        vanilla = _make_audit_vanilla(ApiException(status=404), {"items": []})

        result = CiliumAdapter(vanilla).audit_policies()

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.view == "vanilla"
        assert result.findings == []

    def test_audit_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_audit_vanilla(ApiException(status=403), {"items": []})

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).audit_policies()

    def test_audit_workload_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_audit_vanilla({"items": []}, TimeoutError("timed out"))

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).audit_policies()


def _identity_raw(raw_id: str, labels: dict[str, str] | None = None) -> dict:
    metadata: dict[str, object] = {"name": raw_id}
    if labels:
        metadata["labels"] = labels
    return {"metadata": metadata, "spec": {}}


def _endpoint_raw(raw_id: str) -> dict:
    return {"status": {"identity": {"id": raw_id}}}


def _make_identities_vanilla(identities: object, endpoints: object) -> MagicMock:
    vanilla = MagicMock()
    crd_api = MagicMock()

    def dispatch(plural: str, **kwargs: object) -> object:
        if plural == "ciliumidentities":
            if isinstance(identities, Exception):
                raise identities
            return identities
        if plural == "ciliumendpoints":
            if isinstance(endpoints, Exception):
                raise endpoints
            return endpoints
        raise AssertionError(f"unexpected plural {plural}")

    crd_api.list_cluster_custom_object.side_effect = dispatch
    vanilla._crd_api_client.return_value = crd_api
    vanilla._apps_api_client.return_value = MagicMock()
    vanilla._api_client.return_value = MagicMock()
    return vanilla


class TestCiliumIdentities:
    def test_list_identities_with_endpoint_counts(self) -> None:
        identities = {
            "items": [
                _identity_raw("100", {"app": "db"}),
                _identity_raw("200", {"app": "web"}),
            ]
        }
        endpoints = {"items": [_endpoint_raw("100"), _endpoint_raw("100"), _endpoint_raw("200")]}
        vanilla = _make_identities_vanilla(identities, endpoints)

        result = CiliumAdapter(vanilla).list_identities()

        assert result.installed is True
        assert result.status == "present"
        assert result.total_identities == 2  # noqa: PLR2004
        assert result.identities[0].id == "100"
        assert result.identities[0].endpoint_count == 2  # noqa: PLR2004
        assert result.identities[1].endpoint_count == 1  # noqa: PLR2004

    def test_list_identities_empty(self) -> None:
        vanilla = _make_identities_vanilla({"items": []}, {"items": []})

        result = CiliumAdapter(vanilla).list_identities()

        assert result.status == "empty"
        assert result.total_identities == 0

    def test_list_identities_not_installed(self) -> None:
        vanilla = _make_identities_vanilla(ApiException(status=404), {"items": []})

        result = CiliumAdapter(vanilla).list_identities()

        assert result.installed is False
        assert result.status == "not_installed"

    def test_list_identities_endpoints_absent_counts_zero(self) -> None:
        identities = {"items": [_identity_raw("100")]}
        vanilla = _make_identities_vanilla(identities, ApiException(status=404))

        result = CiliumAdapter(vanilla).list_identities()

        assert result.identities[0].endpoint_count == 0

    def test_list_identities_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_identities_vanilla(ApiException(status=403), {"items": []})

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).list_identities()

    def test_list_identities_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_identities_vanilla(TimeoutError("timed out"), {"items": []})

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).list_identities()


def _make_seg_vanilla(
    identities: object,
    endpoints: object,
    netpol: object,
    netpol_clusterwide: object,
) -> MagicMock:
    vanilla = MagicMock()
    crd_api = MagicMock()

    def dispatch(plural: str, **kwargs: object) -> object:
        mapping = {
            "ciliumidentities": identities,
            "ciliumendpoints": endpoints,
            "ciliumnetworkpolicies": netpol,
            "ciliumclusterwidenetworkpolicies": netpol_clusterwide,
        }
        value = mapping[plural]
        if isinstance(value, Exception):
            raise value
        return value

    crd_api.list_cluster_custom_object.side_effect = dispatch
    vanilla._crd_api_client.return_value = crd_api
    vanilla._apps_api_client.return_value = MagicMock()
    vanilla._api_client.return_value = MagicMock()
    return vanilla


class TestCiliumSegmentationAudit:
    def test_flags_unrestricted_paths(self) -> None:
        identities = {
            "items": [
                _identity_raw("100", {"app": "web"}),
                _identity_raw("200", {"app": "db"}),
            ]
        }
        vanilla = _make_seg_vanilla(identities, {"items": []}, {"items": []}, {"items": []})

        result = CiliumAdapter(vanilla).segmentation_audit()

        assert result.status == "gaps_found"
        assert result.view == "cilium"
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.uncovered_paths == 2  # noqa: PLR2004

    def test_isolated_when_policy_restricts(self) -> None:
        identities = {
            "items": [
                _identity_raw("100", {"app": "web"}),
                _identity_raw("200", {"app": "db"}),
            ]
        }
        netpol = {"items": [_audit_policy_raw("deny-db", {"app": "db"}, ingress=1, egress=1)]}
        vanilla = _make_seg_vanilla(identities, {"items": []}, netpol, {"items": []})

        result = CiliumAdapter(vanilla).segmentation_audit()

        assert result.status == "isolated"
        assert result.findings == []

    def test_not_installed_returns_vanilla_view(self) -> None:
        vanilla = _make_seg_vanilla(
            ApiException(status=404), {"items": []}, {"items": []}, {"items": []}
        )

        result = CiliumAdapter(vanilla).segmentation_audit()

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.view == "vanilla"

    def test_policies_not_installed_falls_back(self) -> None:
        identities = {"items": [_identity_raw("100")]}
        vanilla = _make_seg_vanilla(
            identities, {"items": []}, ApiException(status=404), ApiException(status=404)
        )

        result = CiliumAdapter(vanilla).segmentation_audit()

        assert result.installed is False
        assert result.view == "vanilla"

    def test_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_seg_vanilla(
            ApiException(status=403), {"items": []}, {"items": []}, {"items": []}
        )

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).segmentation_audit()

    def test_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_seg_vanilla(
            TimeoutError("timed out"), {"items": []}, {"items": []}, {"items": []}
        )

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).segmentation_audit()


class TestCiliumEncryptionStatus:
    def test_wireguard_enabled(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 4, "numberReady": 3},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap=_configmap({"encryption-type": "wireguard", "encryption-enabled": "true"}),
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.installed is True
        assert result.status == "enabled"
        assert result.mode == "wireguard"
        assert result.coverage == "3/4"

    def test_ipsec_enabled(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 2, "numberReady": 2},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap=_configmap({"encryption-type": "ipsec", "encryption-enabled": "true"}),
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.mode == "ipsec"
        assert result.status == "enabled"

    def test_none_when_disabled(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 4, "numberReady": 4},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap=_configmap({"encryption-enabled": "false"}),
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.mode == "none"
        assert result.status == "disabled"
        assert result.encrypted_nodes == 0

    def test_unknown_mode_when_config_unreadable(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 4, "numberReady": 4},
                )
            ]
        )
        vanilla = _make_vanilla(
            daemonsets=ds,
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.mode == "UNKNOWN"
        assert result.status == "unknown"

    def test_not_installed(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=ApiException(status=404),
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.installed is False
        assert result.status == "not_installed"

    def test_crds_only_unknown(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": [{"kind": "CiliumNode"}]},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.installed is True
        assert result.status == "unknown"

    def test_unknown_mode_when_config_read_fails(self) -> None:
        ds = _daemonset_response(
            [
                _daemonset(
                    {"name": "cilium", "namespace": "kube-system"},
                    [{"name": "cilium-agent", "image": "quay.io/cilium/cilium:v1.16.3"}],
                    {"desiredNumberScheduled": 4, "numberReady": 4},
                )
            ]
        )
        vanilla = MagicMock()
        apps_api = MagicMock()
        apps_api.list_daemon_set_for_all_namespaces.return_value = ds
        vanilla._apps_api_client.return_value = apps_api
        crd_api = MagicMock()
        vanilla._crd_api_client.return_value = crd_api
        core_api = MagicMock()
        core_api.read_namespaced_config_map.side_effect = RuntimeError("read failed")
        vanilla._api_client.return_value = core_api

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.mode == "UNKNOWN"
        assert result.status == "unknown"

    def test_not_installed_when_crds_empty(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        result = CiliumAdapter(vanilla).encryption_status()

        assert result.installed is False
        assert result.status == "not_installed"

    def test_crd_error_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets={"items": []},
            crds=RuntimeError("connection refused"),
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).encryption_status()

    def test_rbac_403_raises_insufficient_permissions(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=ApiException(status=403),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(InsufficientPermissionsError):
            CiliumAdapter(vanilla).encryption_status()

    def test_unreachable_raises_cluster_unreachable(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=RuntimeError("connection refused"),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(ClusterUnreachableError):
            CiliumAdapter(vanilla).encryption_status()

    def test_timeout_raises_adapter_timeout(self) -> None:
        vanilla = _make_vanilla(
            daemonsets=TimeoutError("timed out"),
            crds={"items": []},
            pods={"items": []},
            configmap={},
        )

        with pytest.raises(AdapterTimeoutError):
            CiliumAdapter(vanilla).encryption_status()
