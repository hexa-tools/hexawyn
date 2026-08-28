"""Tests for domain/services/calico/connectivity_health_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    DataplaneMode,
)
from hexawyn.domain.services.calico.connectivity_health_service import (
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

    def test_healthy(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", True)],
            total_nodes=2,
            ready_agents=2,
        )
        result = build_calico_connectivity_health(
            detection=detection,
            connectivity={"available": True, "status": "healthy"},
        )
        assert result.verdict == "healthy"
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.degraded_nodes == []
        assert result.tunnel_summary == "IPIP tunnel"
        assert result.connectivity_probe == "healthy"

    def test_node_down_degraded(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", False)],
            total_nodes=2,
            ready_agents=1,
            degraded_agents=1,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.verdict == "degraded"
        assert result.degraded_nodes == ["b"]
        assert result.bgp_summary is not None
        assert "degraded" in result.bgp_summary

    def test_no_agents_unknown(self) -> None:
        detection = self._detection(agents=[], total_nodes=0, ready_agents=0)
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.verdict == "unknown"
        assert result.bgp_summary == "UNKNOWN — no calico-node agents observed"

    def test_unknown_tunnel_state_not_invented(self) -> None:
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

    def test_vxlan_and_ebpf_tunnel_summaries(self) -> None:
        vxlan = build_calico_connectivity_health(
            detection=self._detection(
                mode=DataplaneMode.VXLAN,
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={},
        )
        assert vxlan.tunnel_summary == "VXLAN tunnel"
        ebpf = build_calico_connectivity_health(
            detection=self._detection(
                mode=DataplaneMode.EBPF,
                agents=[self._agent("a", True)],
                total_nodes=1,
                ready_agents=1,
            ),
            connectivity={},
        )
        assert "eBPF" in ebpf.tunnel_summary

    def test_connectivity_probe_degraded(self) -> None:
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

    def test_not_installed(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            agents=[],
            total_nodes=0,
            ready_agents=0,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_summary_reflects_verdict(self) -> None:
        detection = self._detection(
            agents=[self._agent("a", True), self._agent("b", True)],
            total_nodes=2,
            ready_agents=2,
        )
        result = build_calico_connectivity_health(detection=detection, connectivity={})
        assert result.summary is not None
        assert "2/2" in result.summary
