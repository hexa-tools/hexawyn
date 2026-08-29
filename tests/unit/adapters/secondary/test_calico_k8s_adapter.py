"""Tests for CalicoK8sAdapter — k8s-backed CalicoPort implementation."""

from __future__ import annotations

from typing import cast
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    HexawynError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.calico import CalicoDetectionStatus, DataplaneMode
from kubernetes.client.rest import ApiException


def _pool(mode: str = "Never", vxlan: str = "Never", cidr: str = "10.1.0.0/16") -> dict:
    return {
        "metadata": {"name": "pool-1"},
        "spec": {
            "cidr": cidr,
            "ipipMode": mode,
            "vxlanMode": vxlan,
            "disabled": False,
            "natOutgoing": True,
            "nodeSelector": "all()",
        },
    }


def _pod(node: str, ready_status: str = "True", phase: str = "Running") -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = f"calico-node-{node}"
    pod.spec.node_name = node
    pod.status.phase = phase
    pod.status.conditions = [MagicMock(type="Ready", status=ready_status)]
    pod.status.container_statuses = []
    return pod


def _node(name: str) -> MagicMock:
    node = MagicMock()
    node.metadata.name = name
    return node


def _daemonset(namespace: str, image: str) -> MagicMock:
    ds = MagicMock()
    ds.metadata.namespace = namespace
    ds.metadata.name = "calico-node"
    container = MagicMock()
    container.image = image
    ds.spec.template.spec.containers = [container]
    return ds


def _crd(**plural_behavior: object) -> MagicMock:  # noqa: C901
    crd = MagicMock()
    ns_behavior = cast(dict, plural_behavior.pop("_namespaced", {}))
    get_behavior = cast(dict, plural_behavior.pop("_get", {}))
    get_cluster_behavior = cast(dict, plural_behavior.pop("_get_cluster", {}))

    def list_cluster(group: str, version: str, plural: str) -> object:
        behavior = plural_behavior.get(plural)
        if behavior is None:
            raise ApiException(status=404, reason=f"not found: {plural}")
        if isinstance(behavior, Exception):
            raise behavior
        return behavior

    def list_namespaced(  # noqa: PLR0913
        group: str, version: str, namespace: str, plural: str, label_selector: str = ""
    ) -> object:
        behavior = ns_behavior.get(plural)
        if behavior is None:
            raise ApiException(status=404, reason=f"not found: {plural}")
        if isinstance(behavior, Exception):
            raise behavior
        return behavior

    def get_namespaced(group: str, version: str, namespace: str, plural: str, name: str) -> object:
        behavior = get_behavior.get(plural)
        if behavior is None:
            raise ApiException(status=404, reason=f"not found: {plural}")
        if isinstance(behavior, Exception):
            raise behavior
        return behavior

    def get_cluster(group: str, version: str, plural: str, name: str) -> object:
        behavior = get_cluster_behavior.get(plural)
        if behavior is None:
            raise ApiException(status=404, reason=f"not found: {plural}")
        if isinstance(behavior, Exception):
            raise behavior
        return behavior

    crd.list_cluster_custom_object.side_effect = list_cluster
    crd.list_namespaced_custom_object.side_effect = list_namespaced
    crd.get_namespaced_custom_object.side_effect = get_namespaced
    crd.get_cluster_custom_object.side_effect = get_cluster
    return crd


def _apps(daemonsets: list[MagicMock] | None = None) -> MagicMock:
    apps = MagicMock()
    apps.list_daemon_set_for_all_namespaces.return_value = MagicMock(items=daemonsets or [])
    return apps


def _core(pods: list[MagicMock] | None, nodes: list[MagicMock] | None) -> MagicMock:
    core = MagicMock()
    core.list_node.return_value = MagicMock(items=nodes or [])
    core.list_pod_for_all_namespaces.return_value = MagicMock(items=pods or [])
    return core


class TestCalicoK8sAdapterDetect:
    def test_installed_via_crds(self) -> None:
        crd = _crd(
            ippools={"items": [_pool(mode="Always")]},
            felixconfigurations={"items": []},
            hostendpoints={"items": []},
            clusterinformations={"items": [{"spec": {"version": "v3.26.1"}}]},
        )
        apps = _apps([_daemonset("calico-system", "quay.io/calico/node:v3.26.1")])
        core = _core([_pod("node-1"), _pod("node-2")], [_node("node-1"), _node("node-2")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd, metrics_source=None)

        result = adapter.detect()

        assert result.installed is True
        assert result.status == CalicoDetectionStatus.INSTALLED
        assert result.mode == DataplaneMode.IPIP
        assert result.version == "v3.26.1"
        assert result.total_nodes == 2  # noqa: PLR2004
        assert result.ready_agents == 2  # noqa: PLR2004

    def test_installed_via_daemonset_when_crds_absent(self) -> None:
        crd = _crd()
        apps = _apps([_daemonset("calico-system", "quay.io/calico/node:v3.28.0")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.installed is True
        assert result.namespace == "calico-system"
        assert result.version == "v3.28.0"

    def test_not_installed(self) -> None:
        crd = _crd()
        apps = _apps([])
        core = _core([], [])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.installed is False
        assert result.status == CalicoDetectionStatus.NOT_INSTALLED
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.version is None
        assert result.mode == DataplaneMode.UNKNOWN

    def test_degraded_when_agent_not_ready(self) -> None:
        crd = _crd(ippools={"items": [_pool(mode="Never", vxlan="Always")]})
        apps = _apps([_daemonset("calico-system", "calico/node:v3.26.1")])
        core = _core(
            [_pod("node-1", ready_status="True"), _pod("node-2", ready_status="False")],
            [_node("node-1"), _node("node-2")],
        )
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.mode == DataplaneMode.VXLAN
        assert result.ready_agents == 1
        assert result.degraded_agents == 1
        assert result.degraded_summary is not None

    def test_empty_agent_list_is_degraded(self) -> None:
        crd = _crd(ippools={"items": [_pool()]})
        apps = _apps([_daemonset("calico-system", "calico/node:v3.26.1")])
        core = _core([], [])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.installed is True
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.total_nodes == 0
        assert result.degraded_summary is not None

    def test_version_raw_preserved(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            clusterinformations={"items": [{"spec": {"version": "v3.28.0-rc.1"}}]},
        )
        apps = _apps([_daemonset("calico-system", "calico/node:v3.28.0-rc.1")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.version == "v3.28.0-rc.1"

    def test_rbac_forbidden_raises_insufficient_permissions(self) -> None:
        crd = _crd(ippools=ApiException(status=403, reason="forbidden"))
        apps = _apps([])
        core = _core([], [])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        with pytest.raises(InsufficientPermissionsError):
            adapter.detect()

    def test_ebpf_mode_detected_from_felix(self) -> None:
        crd = _crd(
            ippools={"items": []},
            felixconfigurations={"items": [{"spec": {"bpfEnabled": True}}]},
        )
        apps = _apps([_daemonset("calico-system", "calico/node:v3.26.1")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.mode == DataplaneMode.EBPF

    def test_tigera_operator_flag(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            installs={"items": [{"spec": {"version": "v1.27.0"}}]},
        )
        apps = _apps([])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        result = adapter.detect()

        assert result.tigera_operator is True
        assert result.enterprise is True


class TestCalicoK8sAdapterOtherMethods:
    def test_list_ip_pools_installed(self) -> None:
        crd = _crd(ippools={"items": [_pool(mode="Always")]})
        apps = _apps([_daemonset("calico-system", "node:v3")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        pools = adapter.list_ip_pools()

        assert len(pools) == 1
        assert pools[0].cidr == "10.1.0.0/16"
        assert pools[0].ipip_mode == "Always"
        assert pools[0].nat_outgoing is True
        assert pools[0].node_selector == "all()"

    def test_list_ip_pools_disabled_flag_surfaced(self) -> None:
        disabled_pool = {
            "metadata": {"name": "pool-disabled"},
            "spec": {"cidr": "10.2.0.0/16", "disabled": True, "natOutgoing": False},
        }
        crd = _crd(ippools={"items": [disabled_pool]})
        apps = _apps([_daemonset("calico-system", "node:v3")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

        pools = adapter.list_ip_pools()

        assert pools[0].disabled is True
        assert pools[0].nat_outgoing is False

    def test_list_ip_pools_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_ip_pools() == []

    def test_list_network_policies_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_network_policies() == []

    def test_get_network_policy_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.get_network_policy("np", "default") is None

    def test_audit_policies_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        result = adapter.audit_policies()
        assert result.get("installed") is False

    def test_list_host_endpoints_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_host_endpoints() == []

    def test_bgp_audit_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.bgp_audit() == {}

    def test_encryption_status_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.encryption_status() == {}

    def test_felix_metrics_uses_metrics_source(self) -> None:
        metrics = MagicMock()
        metrics.felix_metrics.return_value = {"available": True, "metrics": {"x": 1}}
        adapter = CalicoK8sAdapter(metrics_source=metrics)
        assert adapter.felix_metrics()["available"] is True
        metrics.felix_metrics.assert_called_once()

    def test_felix_metrics_without_source(self) -> None:
        adapter = CalicoK8sAdapter()
        assert adapter.felix_metrics()["available"] is False

    def test_felix_policy_counters_uses_metrics_source(self) -> None:
        metrics = MagicMock()
        metrics.felix_policy_counters.return_value = {"available": True, "samples": []}
        adapter = CalicoK8sAdapter(metrics_source=metrics)
        assert adapter.felix_policy_counters()["available"] is True
        metrics.felix_policy_counters.assert_called_once()

    def test_felix_policy_counters_without_source(self) -> None:
        adapter = CalicoK8sAdapter()
        assert adapter.felix_policy_counters()["available"] is False

    def test_status_returns_result(self) -> None:
        crd = _crd(ippools={"items": [_pool()]})
        apps = _apps([_daemonset("calico-system", "node:v3")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)
        assert isinstance(adapter.status().agents, list)


class TestCalicoK8sAdapterInstalledParsing:
    def _adapter(  # noqa: PLR0913
        self, crd: MagicMock, apps: MagicMock | None = None, core: MagicMock | None = None
    ) -> CalicoK8sAdapter:
        apps = apps or _apps([_daemonset("calico-system", "node:v3")])
        core = core or _core([_pod("node-1")], [_node("node-1")])
        return CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)

    def test_list_network_policies_global(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            globalnetworkpolicies={
                "items": [
                    {
                        "metadata": {"name": "g-np"},
                        "spec": {
                            "order": 10.0,
                            "selector": "app=='web'",
                            "ingress": ["a"],
                            "egress": ["b"],
                            "applyOnForward": True,
                        },
                    }
                ]
            },
        )
        policies = self._adapter(crd).list_network_policies()
        assert len(policies) == 1  # noqa: PLR2004
        assert policies[0].namespace == ""
        assert policies[0].apply_on_forward is True

    def test_list_network_policies_namespaced(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _namespaced={
                "networkpolicies": {
                    "items": [
                        {"metadata": {"name": "np", "namespace": "ns"}, "spec": {"order": 5.0}}
                    ]
                }
            },
        )
        policies = self._adapter(crd).list_network_policies(namespace="ns")
        assert len(policies) == 1  # noqa: PLR2004
        assert policies[0].namespace == "ns"

    def test_get_network_policy_installed(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _get={
                "networkpolicies": {
                    "apiVersion": "projectcalico.org/v3",
                    "kind": "NetworkPolicy",
                    "metadata": {"name": "np", "namespace": "ns"},
                    "spec": {"selector": "app=='web'"},
                }
            },
        )
        policy = self._adapter(crd).get_network_policy("np", "ns")
        assert policy is not None
        assert policy.name == "np"
        assert policy.kind == "CalicoNetworkPolicy"

    def test_get_global_network_policy_cluster_scope(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _get_cluster={
                "globalnetworkpolicies": {
                    "apiVersion": "projectcalico.org/v3",
                    "kind": "GlobalNetworkPolicy",
                    "metadata": {"name": "g-np"},
                    "spec": {"selector": "all()"},
                }
            },
        )
        policy = self._adapter(crd).get_network_policy("g-np", "")
        assert policy is not None
        assert policy.kind == "GlobalNetworkPolicy"
        assert policy.namespace == ""

    def test_get_network_policy_wrong_kind_refused(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _get={
                "networkpolicies": {
                    "apiVersion": "networking.k8s.io/v1",
                    "kind": "NetworkPolicy",
                    "metadata": {"name": "np", "namespace": "ns"},
                    "spec": {},
                }
            },
        )
        with pytest.raises(HexawynError):
            self._adapter(crd).get_network_policy("np", "ns")

    def test_get_network_policy_rbac_forbidden(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _get={"networkpolicies": ApiException(status=403, reason="forbidden")},
        )
        with pytest.raises(InsufficientPermissionsError):
            self._adapter(crd).get_network_policy("np", "ns")

    def test_audit_policies_installed(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            globalnetworkpolicies={"items": [{"metadata": {"name": "g"}, "spec": {}}]},
        )
        out = self._adapter(crd).audit_policies()
        assert out["installed"] is True
        assert out["global"] == 1  # noqa: PLR2004

    def test_list_host_endpoints_installed(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            hostendpoints={
                "items": [
                    {
                        "metadata": {"name": "he"},
                        "spec": {
                            "node": "n1",
                            "interfaceName": "eth0",
                            "expectedIPs": ["10.0.0.1"],
                            "labels": {"kubernetes.io/hostname": "n1"},
                            "profiles": ["default.host-endpoints"],
                        },
                    }
                ]
            },
        )
        endpoints = self._adapter(crd).list_host_endpoints()
        assert len(endpoints) == 1  # noqa: PLR2004
        assert endpoints[0].expected_ip == "10.0.0.1"
        assert ("kubernetes.io/hostname", "n1") in endpoints[0].labels
        assert endpoints[0].applied_policies == ("default.host-endpoints",)

    def test_list_host_endpoints_no_labels(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            hostendpoints={"items": [{"metadata": {"name": "he"}, "spec": {"node": "n1"}}]},
        )
        endpoints = self._adapter(crd).list_host_endpoints()
        assert endpoints[0].labels == ()
        assert endpoints[0].applied_policies == ()

    def test_bgp_audit_installed(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            bgpconfigurations={"items": [{"spec": {"nodeToNodeMeshEnabled": True}}]},
        )
        out = self._adapter(crd).bgp_audit()
        assert out["bgp_configurations"] == 1  # noqa: PLR2004
        assert out["node_to_node_mesh_configured"] is True

    def test_list_bgp_configurations(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            bgpconfigurations={
                "items": [
                    {
                        "metadata": {"name": "default"},
                        "spec": {
                            "asNumber": "64512",
                            "nodeToNodeMeshEnabled": True,
                            "serviceClusterIPs": ["10.96.0.0/16"],
                        },
                    }
                ]
            },
        )
        configs = self._adapter(crd).list_bgp_configurations()
        assert len(configs) == 1  # noqa: PLR2004
        assert configs[0].as_number == "64512"
        assert configs[0].service_cluster_ips == ("10.96.0.0/16",)

    def test_list_bgp_configurations_malformed_asn(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            bgpconfigurations={"items": [{"spec": {"asNumber": "not-a-number"}}]},
        )
        configs = self._adapter(crd).list_bgp_configurations()
        assert configs[0].as_number == "not-a-number"

    def test_list_bgp_peers(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            bgppeers={
                "items": [
                    {
                        "metadata": {"name": "peer-1"},
                        "spec": {
                            "peerIP": "10.0.0.2",
                            "asNumber": "64513",
                            "nodeSelector": "all()",
                        },
                    }
                ]
            },
        )
        peers = self._adapter(crd).list_bgp_peers()
        assert len(peers) == 1  # noqa: PLR2004
        assert peers[0].peer_ip == "10.0.0.2"
        assert peers[0].as_number == "64513"
        assert peers[0].node_selector == "all()"

    def test_list_bgp_peers_not_installed(self) -> None:
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_bgp_peers() == []
        assert adapter.list_bgp_configurations() == []

    def test_encryption_status_encrypted(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            felixconfigurations={"items": [{"spec": {"wireguardEnabled": True}}]},
        )
        out = self._adapter(crd).encryption_status()
        assert out["wireguard_enabled"] is True

    def test_encryption_status_per_node(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            felixconfigurations={
                "items": [
                    {
                        "metadata": {"name": "default"},
                        "spec": {"wireguardEnabled": True},
                    },
                    {
                        "metadata": {"name": "node.node-1"},
                        "spec": {"wireguardEnabled": False},
                    },
                ]
            },
        )
        out = self._adapter(crd).encryption_status()
        assert out["wireguard_enabled"] is True
        assert {"node": "node-1", "wireguard_enabled": False} in out["per_node"]

    def test_version_from_install_via_tigera(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            installs={"items": [{"spec": {"version": "v1.27.0"}}]},
        )
        apps = _apps([])
        result = self._adapter(crd, apps=apps).detect()
        assert result.version == "v1.27.0"
        assert result.tigera_operator is True

    def test_felix_ebpf_via_feature_gates(self) -> None:
        crd = _crd(
            ippools={"items": []},
            felixconfigurations={"items": [{"spec": {"featureGates": {"BPFEnabled": True}}}]},
        )
        assert self._adapter(crd).detect().mode == DataplaneMode.EBPF

    def test_cluster_unreachable_raised(self) -> None:
        crd = _crd(ippools=ApiException(status=500, reason="boom"))
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=crd)
        with pytest.raises(ClusterUnreachableError):
            adapter.detect()

    def test_daemonset_image_without_tag(self) -> None:
        crd = _crd()
        apps = _apps([_daemonset("calico-system", "quay.io/calico/node")])
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)
        result = adapter.detect()
        assert result.installed is True
        assert result.version is None

    def test_pod_message_extracted_from_terminated(self) -> None:
        pod = _pod("node-1", ready_status="False")
        state = MagicMock()
        state.waiting = None
        state.terminated = MagicMock(message="crash")
        pod.status.container_statuses = [MagicMock(state=state)]
        crd = _crd(ippools={"items": [_pool()]})
        core = _core([pod], [_node("node-1")])
        agents = self._adapter(crd, core=core).detect().agents
        assert agents[0].message == "crash"

    def test_encryption_status_unencrypted_when_installed(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            felixconfigurations={"items": [{"spec": {"wireguardEnabled": False}}]},
        )
        out = self._adapter(crd).encryption_status()
        assert out["wireguard_enabled"] is False

    def test_encryption_status_no_configuration(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            felixconfigurations={"items": []},
        )
        out = self._adapter(crd).encryption_status()
        assert out["wireguard_enabled"] is None

    def test_get_network_policy_installed_not_found(self) -> None:
        crd = _crd(ippools={"items": [_pool()]}, _get={"networkpolicies": ApiException(status=404)})
        with pytest.raises(ResourceNotFoundError):
            self._adapter(crd).get_network_policy("np", "ns")

    def test_connectivity_health_with_source(self) -> None:
        metrics = MagicMock()
        metrics.connectivity_health.return_value = {"available": True, "status": "healthy"}
        adapter = CalicoK8sAdapter(metrics_source=metrics)
        assert adapter.connectivity_health()["status"] == "healthy"

    def test_connectivity_health_without_source(self) -> None:
        adapter = CalicoK8sAdapter()
        assert adapter.connectivity_health()["available"] is False

    def test_pod_message_from_waiting(self) -> None:
        pod = _pod("node-1", ready_status="False")
        state = MagicMock()
        state.terminated = None
        state.waiting = MagicMock(message="waiting-for-cni")
        pod.status.container_statuses = [MagicMock(state=state)]
        crd = _crd(ippools={"items": [_pool()]})
        core = _core([pod], [_node("node-1")])
        agents = self._adapter(crd, core=core).detect().agents
        assert agents[0].message == "waiting-for-cni"

    def test_pod_message_skips_none_state(self) -> None:
        pod = _pod("node-1", ready_status="True")
        first = MagicMock()
        first.state = None
        second_state = MagicMock()
        second_state.waiting = None
        second_state.terminated = MagicMock(message="ok-msg")
        pod.status.container_statuses = [first, MagicMock(state=second_state)]
        crd = _crd(ippools={"items": [_pool()]})
        core = _core([pod], [_node("node-1")])
        agents = self._adapter(crd, core=core).detect().agents
        assert agents[0].message == "ok-msg"

    def test_version_from_cluster_information_when_no_daemonset(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            clusterinformations={"items": [{"spec": {"version": "v3.30.0"}}]},
        )
        apps = _apps([])
        result = self._adapter(crd, apps=apps).detect()
        assert result.version == "v3.30.0"

    def test_version_from_install_no_valid_version(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            installs={"items": [{"spec": {}}]},
        )
        apps = _apps([])
        result = self._adapter(crd, apps=apps).detect()
        assert result.version is None

    def test_calico_node_daemonset_error_returns_none(self) -> None:
        apps = MagicMock()
        apps.list_daemon_set_for_all_namespaces.side_effect = RuntimeError("boom")
        crd = _crd(ippools={"items": [_pool()]})
        core = _core([_pod("node-1")], [_node("node-1")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)
        assert adapter.detect().installed is True

    def test_calico_node_pods_error_returns_empty(self) -> None:
        core = MagicMock()
        core.list_node.return_value = MagicMock(items=[])
        core.list_pod_for_all_namespaces.side_effect = RuntimeError("boom")
        crd = _crd(ippools={"items": [_pool()]})
        apps = _apps([_daemonset("calico-system", "node:v3")])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd)
        assert adapter.detect().agents == []

    def test_pod_without_ready_condition(self) -> None:
        pod = MagicMock()
        pod.metadata.name = "calico-node-x"
        pod.spec.node_name = "node-1"
        pod.status.phase = "Running"
        pod.status.conditions = []
        pod.status.container_statuses = []
        crd = _crd(ippools={"items": [_pool()]})
        core = _core([pod], [_node("node-1")])
        agents = self._adapter(crd, core=core).detect().agents
        assert agents[0].phase.value == "running"

    def test_list_network_policies_namespaced_not_found(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            _namespaced={"networkpolicies": ApiException(status=404)},
        )
        assert self._adapter(crd).list_network_policies(namespace="ns") == []

    def test_duplicate_pools_dedup_signals_and_list_all(self) -> None:
        crd = _crd(ippools={"items": [_pool(mode="Always"), _pool(mode="Always")]})
        adapter = self._adapter(crd)
        assert adapter.detect().mode == DataplaneMode.IPIP
        assert len(adapter.list_ip_pools()) == 2  # noqa: PLR2004

    def test_mixed_ipip_and_vxlan_pools_resolves_vxlan(self) -> None:
        crd = _crd(ippools={"items": [_pool(mode="Always"), _pool(mode="Never", vxlan="Always")]})
        result = self._adapter(crd).detect()
        assert result.mode == DataplaneMode.VXLAN

    def test_same_signal_across_multiple_pools_still_ipip(self) -> None:
        crd = _crd(ippools={"items": [_pool(mode="CrossSubnet"), _pool(mode="Always")]})
        assert self._adapter(crd).detect().mode == DataplaneMode.IPIP

    def _core_with_namespaces(self, namespaces: list[str]) -> MagicMock:
        core = MagicMock()
        core.list_node.return_value = MagicMock(items=[])
        core.list_pod_for_all_namespaces.return_value = MagicMock(items=[])
        core.list_namespace.return_value = MagicMock(
            items=[MagicMock(metadata=MagicMock(name=ns)) for ns in namespaces]
        )
        return core

    def test_list_network_policies_cluster_only(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            globalnetworkpolicies={
                "items": [{"metadata": {"name": "g-np"}, "spec": {"selector": "all()"}}]
            },
        )
        adapter = CalicoK8sAdapter(
            core_api=self._core_with_namespaces([]),
            apps_api=_apps([_daemonset("calico-system", "v3")]),
            crd_api=crd,
        )
        policies = adapter.list_network_policies()
        assert len(policies) == 1  # noqa: PLR2004
        assert policies[0].kind == "GlobalNetworkPolicy"
        assert policies[0].namespace == ""

    def test_list_network_policies_scans_namespaces(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            globalnetworkpolicies={"items": [{"metadata": {"name": "g-np"}, "spec": {}}]},
            _namespaced={
                "networkpolicies": {
                    "items": [{"metadata": {"name": "np", "namespace": "ns"}, "spec": {}}]
                }
            },
        )
        adapter = CalicoK8sAdapter(
            core_api=self._core_with_namespaces(["ns"]),
            apps_api=_apps([_daemonset("calico-system", "v3")]),
            crd_api=crd,
        )
        policies = adapter.list_network_policies()
        assert len(policies) == 2  # noqa: PLR2004
        assert sum(1 for p in policies if p.kind == "GlobalNetworkPolicy") == 1  # noqa: PLR2004
        assert sum(1 for p in policies if p.kind == "CalicoNetworkPolicy") == 1  # noqa: PLR2004

    def test_list_network_policies_rbac_forbidden(self) -> None:
        crd = _crd(
            ippools={"items": [_pool()]},
            globalnetworkpolicies=ApiException(status=403, reason="forbidden"),
        )
        adapter = self._adapter(crd)
        with pytest.raises(InsufficientPermissionsError):
            adapter.list_network_policies()


class TestCalicoK8sAdapterRuntimeFallbacks:
    def test_runtime_api_fallbacks(self) -> None:
        with (
            patch("kubernetes.client.CoreV1Api") as core_cls,
            patch("kubernetes.client.AppsV1Api") as apps_cls,
            patch("kubernetes.client.CustomObjectsApi") as crd_cls,
        ):
            adapter = CalicoK8sAdapter()
            assert adapter._runtime_core_api is core_cls.return_value
            assert adapter._runtime_apps_api is apps_cls.return_value
            assert adapter._runtime_crd_api is crd_cls.return_value


class TestCalicoK8sAdapterWorkloads:
    def _workload_pod(self, namespace: str) -> MagicMock:
        pod = MagicMock()
        pod.metadata.namespace = namespace
        return pod

    def test_list_workloads_groups_by_namespace(self) -> None:
        core = MagicMock()
        core.list_pod_for_all_namespaces.return_value = MagicMock(
            items=[
                self._workload_pod("ns1"),
                self._workload_pod("ns1"),
                self._workload_pod("ns2"),
            ]
        )
        adapter = CalicoK8sAdapter(core_api=core, apps_api=_apps([]), crd_api=_crd())
        workloads = adapter.list_workloads()
        by_ns = {w.namespace: w.pod_count for w in workloads}
        assert by_ns == {"ns1": 2, "ns2": 1}

    def test_list_workloads_empty(self) -> None:
        core = MagicMock()
        core.list_pod_for_all_namespaces.return_value = MagicMock(items=[])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_workloads() == []

    def test_list_workloads_error_returns_empty(self) -> None:
        core = MagicMock()
        core.list_pod_for_all_namespaces.side_effect = RuntimeError("boom")
        adapter = CalicoK8sAdapter(core_api=core, apps_api=_apps([]), crd_api=_crd())
        assert adapter.list_workloads() == []


class TestCalicoK8sAdapterCoverage:
    def test_get_network_policy_cluster_not_found_raises(self) -> None:
        crd = _crd(ippools={"items": []}, _get_cluster={"globalnetworkpolicies": None})
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=crd)
        with pytest.raises(ResourceNotFoundError):
            adapter.get_network_policy("global-pol", "")

    def test_get_network_policy_cluster_api_error_raises_unreachable(self) -> None:
        crd = _crd(
            ippools={"items": []},
            _get_cluster={"globalnetworkpolicies": ApiException(status=500, reason="backend down")},
        )
        adapter = CalicoK8sAdapter(core_api=_core([], []), apps_api=_apps([]), crd_api=crd)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_network_policy("global-pol", "")

    def test_parse_and_guard_rejects_unknown_kind(self) -> None:
        with pytest.raises(HexawynError):
            CalicoK8sAdapter._parse_and_guard(
                {"apiVersion": "projectcalico.org", "kind": "BogusKind"},
                namespaced=False,
            )

    def test_list_workloads_namespaced_uses_namespaced_api(self) -> None:
        core = MagicMock()
        pod = MagicMock()
        pod.metadata.namespace = "default"
        core.list_namespaced_pod.return_value = MagicMock(items=[pod])
        adapter = CalicoK8sAdapter(core_api=core, apps_api=_apps([]), crd_api=_crd())

        result = adapter.list_workloads(namespace="default")

        core.list_namespaced_pod.assert_called_with(namespace="default", timeout_seconds=10)
        assert len(result) == 1
        assert result[0].namespace == "default"

    def test_namespaces_api_error_returns_empty(self) -> None:
        core = MagicMock()
        core.list_namespace.side_effect = RuntimeError("boom")
        adapter = CalicoK8sAdapter(core_api=core, apps_api=_apps([]), crd_api=_crd())
        assert adapter._namespaces() == []

    def test_parse_bgp_configuration_mesh_from_dict(self) -> None:
        result = CalicoK8sAdapter._parse_bgp_configuration(
            {
                "metadata": {"name": "default"},
                "spec": {"nodeToNodeMesh": {"enabled": True}},
            }
        )
        assert result.name == "default"
        assert result.node_to_node_mesh_enabled is True
