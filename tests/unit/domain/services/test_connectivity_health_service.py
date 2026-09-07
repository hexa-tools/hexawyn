"""Tests for domain/services/calico/connectivity_health_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoConnectivityHealthResult,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    CalicoNodeConnectivity,
    DataplaneMode,
)
from hexawyn.domain.services.calico.connectivity_health_service import (
    _bgp_summary,
    _summary,
    _tunnel_summary,
    build_calico_connectivity_health,
)


class TestBuildCalicoConnectivityHealth:
    def _agent(self, node: str, healthy: bool) -> CalicoNodeAgent:
        return CalicoNodeAgent(
            node=node,
            phase=CalicoAgentPhase.READY if healthy else CalicoAgentPhase.NOT_READY,
            ready=healthy,
            ready_replicas=1 if healthy else 0,
            desired_replicas=1,
            available_replicas=1 if healthy else 0,
        )

    def _detection(self, **overrides: object) -> CalicoDetectionResult:
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
            "total_nodes": 3,
            "ready_agents": 3,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def _expected(  # noqa: PLR0913
        self,
        *,
        verdict: str,
        ready_agents: int,
        total_agents: int,
        mode: DataplaneMode | None,
        tunnel_summary: str,
        bgp_summary: str,
        probe: str | None,
        nodes: list[CalicoNodeConnectivity],
        degraded_nodes: list[str],
    ) -> CalicoConnectivityHealthResult:
        return CalicoConnectivityHealthResult(
            installed=True,
            not_installed_marker=None,
            verdict=verdict,
            ready_agents=ready_agents,
            total_agents=total_agents,
            dataplane_mode=mode,
            tunnel_summary=tunnel_summary,
            bgp_summary=bgp_summary,
            connectivity_probe=probe,
            nodes=nodes,
            degraded_nodes=degraded_nodes,
            summary=(
                f"Calico dataplane {verdict}: {ready_agents}/{total_agents} "
                "calico-node agents ready"
            ),
            error=None,
        )

    def test_healthy_full_payload(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", True)],
            total_nodes=2,
            ready_agents=2,
        )
        result = build_calico_connectivity_health(
            detection=detection,
            connectivity={"available": True, "status": "healthy"},
        )
        assert result == self._expected(
            verdict="healthy",
            ready_agents=2,
            total_agents=2,
            mode=DataplaneMode.IPIP,
            tunnel_summary="IPIP tunnel",
            bgp_summary="BGP node-to-node mesh reachable (all calico-node agents ready)",
            probe="healthy",
            nodes=[
                CalicoNodeConnectivity(node="a", ready=True),
                CalicoNodeConnectivity(node="b", ready=True),
            ],
            degraded_nodes=[],
        )

    def test_node_down_degraded_full_payload(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", False)],
            total_nodes=2,
            ready_agents=1,
            degraded_agents=1,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result == self._expected(
            verdict="degraded",
            ready_agents=1,
            total_agents=2,
            mode=DataplaneMode.IPIP,
            tunnel_summary="IPIP tunnel",
            bgp_summary="1 calico-node agent(s) degraded — BGP sessions may be affected",
            probe=None,
            nodes=[
                CalicoNodeConnectivity(node="a", ready=True),
                CalicoNodeConnectivity(node="b", ready=False),
            ],
            degraded_nodes=["b"],
        )

    def test_no_agents_unknown_full_payload(self) -> None:
        detection = self._detection(agents=[], total_nodes=0, ready_agents=0)
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result == self._expected(
            verdict="unknown",
            ready_agents=0,
            total_agents=0,
            mode=DataplaneMode.IPIP,
            tunnel_summary="IPIP tunnel",
            bgp_summary="UNKNOWN — no calico-node agents observed",
            probe=None,
            nodes=[],
            degraded_nodes=[],
        )

    def test_unknown_mode_tunnel_not_invented(self) -> None:
        detection = self._detection(
            mode=DataplaneMode.UNKNOWN,
            agents=[self._agent("a", True)],
            total_nodes=1,
            ready_agents=1,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.tunnel_summary == "UNKNOWN"

    def test_missing_mode_tunnel_unknown(self) -> None:
        detection = self._detection(
            mode=None,
            agents=[self._agent("a", True)],
            total_nodes=1,
            ready_agents=1,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.tunnel_summary == "UNKNOWN"
        assert result.verdict == "healthy"

    def test_vxlan_tunnel_summary(self) -> None:
        result = build_calico_connectivity_health(
            detection=self._detection(
                mode=DataplaneMode.VXLAN,
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={},
        )
        assert result.tunnel_summary == "VXLAN tunnel"

    def test_ebpf_tunnel_summary(self) -> None:
        result = build_calico_connectivity_health(
            detection=self._detection(
                mode=DataplaneMode.EBPF,
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={},
        )
        assert result.tunnel_summary == "eBPF dataplane (no IPIP/VXLAN tunnel)"

    def test_connectivity_probe_status_passthrough(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", True)],
            total_nodes=2,
            ready_agents=2,
        )
        result = build_calico_connectivity_health(
            detection=detection,
            connectivity={"available": True, "status": "degraded"},
        )
        assert result.verdict == "healthy"
        assert result.connectivity_probe == "degraded"

    def test_connectivity_probe_not_available_ignored(self) -> None:
        result = build_calico_connectivity_health(
            detection=self._detection(
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={"available": False, "status": "degraded"},
        )
        assert result.connectivity_probe is None

    def test_connectivity_available_without_status_ignored(self) -> None:
        result = build_calico_connectivity_health(
            detection=self._detection(
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={"available": True, "status": None},
        )
        assert result.connectivity_probe is None

    def test_not_installed_full_payload(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            agents=[],
            total_nodes=0,
            ready_agents=0,
            error="kube api unreachable",
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.verdict == "unknown"
        assert result.ready_agents == 0
        assert result.total_agents == 0
        assert result.dataplane_mode is None
        assert result.tunnel_summary == "UNKNOWN"
        assert result.bgp_summary == "UNKNOWN"
        assert result.connectivity_probe is None
        assert result.nodes == []
        assert result.degraded_nodes == []
        assert result.summary is None
        assert result.error == "kube api unreachable"

    def test_installed_forwards_detection_error(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True)],
            total_nodes=1,
            ready_agents=1,
            error="partial probe",
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.installed is True
        assert result.error == "partial probe"


class TestTunnelSummaryDirect:
    def test_none_mode_unknown(self) -> None:
        assert _tunnel_summary(None) == "UNKNOWN"

    def test_known_modes(self) -> None:
        assert _tunnel_summary(DataplaneMode.IPIP) == "IPIP tunnel"
        assert _tunnel_summary(DataplaneMode.VXLAN) == "VXLAN tunnel"
        assert _tunnel_summary(DataplaneMode.EBPF) == "eBPF dataplane (no IPIP/VXLAN tunnel)"

    def test_unmapped_mode_unknown(self) -> None:
        assert _tunnel_summary(DataplaneMode.UNKNOWN) == "UNKNOWN"


class TestBgpSummaryDirect:
    def test_zero_total_unknown(self) -> None:
        assert _bgp_summary(0, 0) == "UNKNOWN — no calico-node agents observed"

    def test_all_ready_reachable(self) -> None:
        assert (
            _bgp_summary(2, 2) == "BGP node-to-node mesh reachable (all calico-node agents ready)"
        )

    def test_single_degraded(self) -> None:
        assert (
            _bgp_summary(1, 2) == "1 calico-node agent(s) degraded — BGP sessions may be affected"
        )

    def test_multiple_degraded(self) -> None:
        assert (
            _bgp_summary(1, 3) == "2 calico-node agent(s) degraded — BGP sessions may be affected"
        )


class TestSummaryDirect:
    def test_healthy_summary(self) -> None:
        assert _summary("healthy", 2, 2) == "Calico dataplane healthy: 2/2 calico-node agents ready"

    def test_degraded_summary(self) -> None:
        assert (
            _summary("degraded", 1, 2) == "Calico dataplane degraded: 1/2 calico-node agents ready"
        )

    def test_unknown_summary(self) -> None:
        assert _summary("unknown", 0, 0) == "Calico dataplane unknown: 0/0 calico-node agents ready"
