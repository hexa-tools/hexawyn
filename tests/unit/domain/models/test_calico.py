"""Tests for domain/models/calico.py — pure, no infrastructure."""

from __future__ import annotations

import pytest
from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoBgpAuditResult,
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoConnectivityHealthResult,
    CalicoCoverageGap,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoEncryptionNodeStatus,
    CalicoEncryptionStatusResult,
    CalicoFelixMetricsResult,
    CalicoFelixPolicyCounter,
    CalicoHostEndpoint,
    CalicoIPPool,
    CalicoNetworkPolicy,
    CalicoNodeAgent,
    CalicoNodeConnectivity,
    CalicoPolicyAuditResult,
    CalicoSegmentationAuditResult,
    CalicoSegmentationEdge,
    CalicoStatusResult,
    CalicoWorkload,
    DataplaneMode,
)


class TestEnums:
    def test_dataplane_mode_values(self) -> None:
        assert DataplaneMode.IPIP.value == "IPIP"
        assert DataplaneMode.VXLAN.value == "VXLAN"
        assert DataplaneMode.EBPF.value == "eBPF"
        assert DataplaneMode.UNKNOWN.value == "UNKNOWN"

    def test_agent_phase_values(self) -> None:
        assert CalicoAgentPhase.READY.value == "ready"
        assert CalicoAgentPhase.RUNNING.value == "running"
        assert CalicoAgentPhase.NOT_READY.value == "not_ready"
        assert CalicoAgentPhase.UNKNOWN.value == "unknown"

    def test_detection_status_values(self) -> None:
        assert CalicoDetectionStatus.INSTALLED.value == "installed"
        assert CalicoDetectionStatus.DEGRADED.value == "degraded"
        assert CalicoDetectionStatus.NOT_INSTALLED.value == "not_installed"


class TestCalicoNodeAgent:
    def _agent(self, **overrides: object) -> CalicoNodeAgent:
        base: dict[str, object] = {
            "node": "node-1",
            "phase": CalicoAgentPhase.READY,
            "ready": True,
            "ready_replicas": 1,
            "desired_replicas": 1,
            "available_replicas": 1,
            "message": None,
        }
        base.update(overrides)
        return CalicoNodeAgent(**base)  # type: ignore[arg-type]

    def test_ready_agent_is_healthy(self) -> None:
        assert self._agent().healthy is True

    def test_ready_but_zero_desired_is_unhealthy(self) -> None:
        assert self._agent(desired_replicas=0).healthy is False

    def test_ready_but_short_replicas_is_unhealthy(self) -> None:
        assert self._agent(ready_replicas=0).healthy is False

    def test_not_ready_agent_is_unhealthy(self) -> None:
        assert self._agent(ready=False, phase=CalicoAgentPhase.NOT_READY).healthy is False

    def test_boundary_one_replica_healthy(self) -> None:
        assert self._agent(ready_replicas=1, desired_replicas=1).healthy is True

    def test_defaults_message_none(self) -> None:
        assert self._agent().message is None


class TestDetectionResultProperties:
    def _result(self, **overrides: object) -> CalicoDetectionResult:
        base: dict[str, object] = {
            "installed": True,
            "status": CalicoDetectionStatus.INSTALLED,
            "not_installed_marker": None,
            "version": "v3.26.1",
            "mode": DataplaneMode.IPIP,
            "namespace": "calico-system",
            "tigera_operator": False,
            "enterprise": False,
            "agents": [],
            "total_nodes": 1,
            "ready_agents": 1,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_installed_not_installed_false(self) -> None:
        result = self._result()
        assert result.not_installed is False
        assert result.marker is None

    def test_not_installed_flag_and_marker(self) -> None:
        result = self._result(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            version=None,
            namespace=None,
            mode=DataplaneMode.UNKNOWN,
            total_nodes=0,
            ready_agents=0,
            degraded_agents=0,
        )
        assert result.not_installed is True
        assert result.marker == "NOT_INSTALLED"
        assert result.marker == NOT_INSTALLED_MARKER

    def test_empty_agent_list_is_allowed(self) -> None:
        result = self._result(agents=[], total_nodes=0)
        assert result.agents == []
        assert result.total_nodes == 0

    def test_frozen(self) -> None:
        with pytest.raises(Exception):
            self._result().installed = False  # type: ignore[misc]


class TestSerieProjections:
    def test_network_policy(self) -> None:
        np = CalicoNetworkPolicy(
            name="np",
            namespace="default",
            order=100.0,
            selector="app == 'web'",
            ingress_rules=("allow-80",),
            egress_rules=(),
            apply_on_forward=False,
        )
        assert np.name == "np"
        assert np.ingress_rules == ("allow-80",)
        assert np.kind == "CalicoNetworkPolicy"
        assert np.action is None
        assert np.ingress_rule_count == 0

    def test_network_policy_full_fields(self) -> None:
        np = CalicoNetworkPolicy(
            name="g-np",
            namespace="",
            kind="GlobalNetworkPolicy",
            selector="all()",
            action="deny",
            ingress_rules=("deny tcp",),
            egress_rules=(),
            ingress_rule_count=1,
            egress_rule_count=0,
            order=20.0,
            apply_on_forward=True,
        )
        assert np.kind == "GlobalNetworkPolicy"
        assert np.action == "deny"
        assert np.ingress_rule_count == 1  # noqa: PLR2004
        assert np.has_l7_rule is False

    def test_network_policy_l7_flag(self) -> None:
        np = CalicoNetworkPolicy(
            name="np",
            namespace="ns",
            kind="CalicoNetworkPolicy",
            selector="app=='web'",
            action="allow",
            ingress_rules=(),
            egress_rules=(),
            ingress_rule_count=0,
            egress_rule_count=0,
            order=10.0,
            apply_on_forward=False,
            has_l7_rule=True,
        )
        assert np.has_l7_rule is True

    def test_ip_pool(self) -> None:
        pool = CalicoIPPool(
            name="pool",
            cidr="10.1.0.0/16",
            ipip_mode="Always",
            vxlan_mode="Never",
            disabled=False,
        )
        assert pool.cidr == "10.1.0.0/16"
        assert pool.nat_outgoing is False
        assert pool.node_selector == ""

    def test_ip_pool_nat_and_node_selector(self) -> None:
        pool = CalicoIPPool(
            name="pool",
            cidr="10.1.0.0/16",
            ipip_mode="Never",
            vxlan_mode="Never",
            disabled=True,
            nat_outgoing=True,
            node_selector="all()",
        )
        assert pool.disabled is True
        assert pool.nat_outgoing is True
        assert pool.node_selector == "all()"

    def test_host_endpoint(self) -> None:
        he = CalicoHostEndpoint(
            name="he", node="node-1", interface_name="eth0", expected_ip="10.0.0.1"
        )
        assert he.expected_ip == "10.0.0.1"
        assert he.expected_ips == ()
        assert he.labels == ()
        assert he.applied_policies == ()

    def test_host_endpoint_full_fields(self) -> None:
        he = CalicoHostEndpoint(
            name="he",
            node="node-1",
            interface_name="eth0",
            expected_ip="10.0.0.1",
            expected_ips=("10.0.0.1",),
            labels=(("kubernetes.io/hostname", "node-1"),),
            applied_policies=("default.host-endpoints",),
        )
        assert he.labels == (("kubernetes.io/hostname", "node-1"),)
        assert he.applied_policies == ("default.host-endpoints",)
        assert he.expected_ips == ("10.0.0.1",)


class TestCalicoStatusResult:
    def _result(self, **overrides: object) -> CalicoStatusResult:
        base: dict[str, object] = {
            "installed": True,
            "not_installed_marker": None,
            "status": CalicoDetectionStatus.INSTALLED,
            "ready_agents": 3,
            "total_agents": 3,
            "degraded_summary": None,
            "agents": [],
            "felix_errors_available": True,
            "felix_errors": 0,
            "connectivity_available": True,
            "connectivity_status": "healthy",
            "connectivity_detail": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoStatusResult(**base)  # type: ignore[arg-type]

    def test_healthy_fields(self) -> None:
        result = self._result()
        assert result.installed is True
        assert result.status == CalicoDetectionStatus.INSTALLED
        assert result.ready_agents == 3  # noqa: PLR2004
        assert result.total_agents == 3  # noqa: PLR2004
        assert result.degraded_summary is None
        assert result.connectivity_status == "healthy"

    def test_not_installed_flag_and_marker(self) -> None:
        result = self._result(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
        )
        assert result.not_installed is True
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_degraded_status(self) -> None:
        result = self._result(
            status=CalicoDetectionStatus.DEGRADED,
            degraded_summary="1/3 calico-node agents ready (2 degraded)",
        )
        assert result.degraded_summary is not None

    def test_felix_errors_exposed(self) -> None:
        result = self._result(felix_errors=3, felix_errors_available=True)
        assert result.felix_errors == 3  # noqa: PLR2004
        assert result.felix_errors_available is True

    def test_felix_unavailable_none_errors(self) -> None:
        result = self._result(felix_errors=None, felix_errors_available=False)
        assert result.felix_errors is None
        assert result.felix_errors_available is False

    def test_connectivity_unavailable(self) -> None:
        result = self._result(connectivity_available=False, connectivity_status=None)
        assert result.connectivity_available is False
        assert result.connectivity_status is None

    def test_empty_agents_allowed(self) -> None:
        result = self._result(agents=[])
        assert result.agents == []

    def test_frozen(self) -> None:
        with pytest.raises(Exception):
            self._result().installed = False  # type: ignore[misc]


class TestAuditProjections:
    def test_workload(self) -> None:
        workload = CalicoWorkload(namespace="default", pod_count=4)
        assert workload.namespace == "default"
        assert workload.pod_count == 4  # noqa: PLR2004

    def test_coverage_gap(self) -> None:
        gap = CalicoCoverageGap(
            namespace="staging",
            workload_count=3,
            policy_count=1,
            issue="no_default_deny",
            network_status="partially_restricted",
            risk_level="medium",
            selectors=["app=='web'"],
            note="partial",
        )
        assert gap.namespace == "staging"
        assert gap.issue == "no_default_deny"
        assert gap.risk_level == "medium"

    def test_audit_result(self) -> None:
        result = CalicoPolicyAuditResult(
            installed=True,
            not_installed_marker=None,
            total_namespaces_checked=2,
            gap_count=1,
            findings=[],
            summary="1 namespace(s) have Calico L3/L4 coverage gaps out of 2.",
            error=None,
        )
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.installed is True
        assert result.total_namespaces_checked == 2  # noqa: PLR2004

    def test_audit_result_not_installed(self) -> None:
        result = CalicoPolicyAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_namespaces_checked=0,
            gap_count=0,
            findings=[],
            summary=None,
            error="gone",
        )
        assert result.not_installed is True
        assert result.not_installed_marker == "NOT_INSTALLED"


class TestSegmentationAuditProjections:
    def test_edge(self) -> None:
        edge = CalicoSegmentationEdge(
            source="tier-a",
            destination="tier-b",
            restricted=False,
            selectors=["app=='web'"],
            note="allowed",
        )
        assert edge.source == "tier-a"
        assert edge.destination == "tier-b"
        assert edge.restricted is False
        assert edge.selectors == ["app=='web'"]

    def test_edge_restricted(self) -> None:
        edge = CalicoSegmentationEdge(
            source="tier-a",
            destination="tier-b",
            restricted=True,
            selectors=[],
            note=None,
        )
        assert edge.restricted is True

    def test_segmentation_audit_result(self) -> None:
        result = CalicoSegmentationAuditResult(
            installed=True,
            not_installed_marker=None,
            view="calico",
            tiers=["tier-a", "tier-b"],
            edges=[],
            gap_count=0,
            total_paths=2,
            summary="No unrestricted tier-to-tier paths out of 2.",
            error=None,
        )
        assert result.view == "calico"
        assert result.tiers == ["tier-a", "tier-b"]
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.not_installed is False

    def test_segmentation_audit_result_not_installed(self) -> None:
        result = CalicoSegmentationAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            view="vanilla",
            tiers=[],
            edges=[],
            gap_count=0,
            total_paths=0,
            summary=None,
            error="absent",
        )
        assert result.not_installed is True
        assert result.view == "vanilla"


class TestBgpAuditProjections:
    def test_bgp_configuration(self) -> None:
        config = CalicoBgpConfiguration(
            name="default",
            as_number="64512",
            node_to_node_mesh_enabled=True,
            service_cluster_ips=("10.96.0.0/16",),
        )
        assert config.as_number == "64512"
        assert config.node_to_node_mesh_enabled is True
        assert config.service_cluster_ips == ("10.96.0.0/16",)

    def test_bgp_peer(self) -> None:
        peer = CalicoBgpPeer(
            name="peer-1", peer_ip="10.0.0.2", as_number="64513", node_selector="all()"
        )
        assert peer.peer_ip == "10.0.0.2"
        assert peer.as_number == "64513"

    def test_bgp_audit_result(self) -> None:
        result = CalicoBgpAuditResult(
            installed=True,
            not_installed_marker=None,
            as_number="64512",
            node_to_node_mesh_enabled=True,
            service_cluster_ips=("10.96.0.0/16",),
            peers=[],
            peer_count=2,
            session_state="reachable",
            session_note="All calico-node agents ready",
            summary="BGP ASN 64512, 2 peers",
            error=None,
        )
        assert result.peer_count == 2  # noqa: PLR2004
        assert result.session_state == "reachable"
        assert result.not_installed is False

    def test_bgp_audit_result_not_installed(self) -> None:
        result = CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error="absent",
        )
        assert result.not_installed is True
        assert result.session_state == "unknown"


class TestEncryptionStatusProjections:
    def test_node_status(self) -> None:
        node = CalicoEncryptionNodeStatus(node="node-1", wireguard_enabled=True)
        assert node.node == "node-1"
        assert node.wireguard_enabled is True

    def test_encryption_status_result(self) -> None:
        result = CalicoEncryptionStatusResult(
            installed=True,
            not_installed_marker=None,
            wireguard_enabled=True,
            mode=DataplaneMode.IPIP,
            per_node=[CalicoEncryptionNodeStatus(node="node-1", wireguard_enabled=True)],
            summary="WireGuard enabled (IPIP)",
            error=None,
        )
        assert result.wireguard_enabled is True
        assert result.mode == DataplaneMode.IPIP
        assert result.not_installed is False

    def test_encryption_status_result_not_installed(self) -> None:
        result = CalicoEncryptionStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            wireguard_enabled=None,
            mode=None,
            per_node=[],
            summary=None,
            error="absent",
        )
        assert result.not_installed is True
        assert result.wireguard_enabled is None


class TestFelixMetricsProjections:
    def test_policy_counter(self) -> None:
        counter = CalicoFelixPolicyCounter(
            policy="default.deny-all",
            allow_packets=0,
            deny_packets=120,
            allow_bytes=0,
            deny_bytes=40960,
        )
        assert counter.policy == "default.deny-all"
        assert counter.deny_packets == 120  # noqa: PLR2004

    def test_felix_metrics_result(self) -> None:
        result = CalicoFelixMetricsResult(
            installed=True,
            not_installed_marker=None,
            metrics_available=True,
            metrics_message=None,
            policies=[
                CalicoFelixPolicyCounter(
                    policy="p", allow_packets=0, deny_packets=1, allow_bytes=0, deny_bytes=0
                )
            ],
            total_denies=1,
            total_allows=0,
            deny_policy_count=1,
            error=None,
        )
        assert result.metrics_available is True
        assert result.total_denies == 1  # noqa: PLR2004
        assert result.deny_policy_count == 1  # noqa: PLR2004
        assert result.not_installed is False

    def test_felix_metrics_result_not_installed(self) -> None:
        result = CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            metrics_available=False,
            metrics_message=None,
            policies=[],
            total_denies=0,
            total_allows=0,
            deny_policy_count=0,
            error="absent",
        )
        assert result.not_installed is True
        assert result.policies == []


class TestConnectivityHealthProjections:
    def test_node_connectivity(self) -> None:
        node = CalicoNodeConnectivity(node="node-1", ready=True)
        assert node.node == "node-1"
        assert node.ready is True

    def test_connectivity_health_result(self) -> None:
        result = CalicoConnectivityHealthResult(
            installed=True,
            not_installed_marker=None,
            verdict="healthy",
            ready_agents=3,
            total_agents=3,
            dataplane_mode=DataplaneMode.IPIP,
            tunnel_summary="IPIP tunnel",
            bgp_summary="BGP node-to-node mesh reachable",
            connectivity_probe="healthy",
            nodes=[CalicoNodeConnectivity(node="node-1", ready=True)],
            degraded_nodes=[],
            summary="Calico dataplane healthy: 3/3 calico-node agents ready",
            error=None,
        )
        assert result.verdict == "healthy"
        assert result.tunnel_summary == "IPIP tunnel"
        assert result.not_installed is False

    def test_connectivity_health_result_not_installed(self) -> None:
        result = CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            verdict="unknown",
            ready_agents=0,
            total_agents=0,
            dataplane_mode=None,
            tunnel_summary="UNKNOWN",
            bgp_summary="UNKNOWN",
            connectivity_probe=None,
            nodes=[],
            degraded_nodes=[],
            summary=None,
            error="absent",
        )
        assert result.not_installed is True
        assert result.verdict == "unknown"
