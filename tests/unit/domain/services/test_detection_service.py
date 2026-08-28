"""Tests for domain/services/calico — pure detection logic."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoDetectionSignals,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    DataplaneMode,
)
from hexawyn.domain.services.calico.detection_service import (
    build_agent_phase,
    build_degraded_summary,
    build_detection_result,
    resolve_dataplane_mode,
)


class TestResolveDataplaneMode:
    def test_empty_signals_is_unknown(self) -> None:
        assert resolve_dataplane_mode(set()) == DataplaneMode.UNKNOWN

    def test_ebpf_signal(self) -> None:
        assert resolve_dataplane_mode({"ebpf"}) == DataplaneMode.EBPF

    def test_vxlan_signal(self) -> None:
        assert resolve_dataplane_mode({"vxlan"}) == DataplaneMode.VXLAN

    def test_ipip_signal(self) -> None:
        assert resolve_dataplane_mode({"ipip"}) == DataplaneMode.IPIP

    def test_ebpf_takes_priority(self) -> None:
        assert resolve_dataplane_mode({"ebpf", "vxlan", "ipip"}) == DataplaneMode.EBPF

    def test_vxlan_over_ipip(self) -> None:
        assert resolve_dataplane_mode({"vxlan", "ipip"}) == DataplaneMode.VXLAN

    def test_case_insensitive(self) -> None:
        assert resolve_dataplane_mode({"VXLAN", "IPIP"}) == DataplaneMode.VXLAN

    def test_unknown_signal_is_ignored(self) -> None:
        assert resolve_dataplane_mode({"bogus"}) == DataplaneMode.UNKNOWN


class TestBuildAgentPhase:
    def test_ready_true_is_ready(self) -> None:
        assert build_agent_phase("running", "True") == CalicoAgentPhase.READY

    def test_ready_false_is_not_ready(self) -> None:
        assert build_agent_phase("running", "False") == CalicoAgentPhase.NOT_READY

    def test_running_unknown_ready_is_running(self) -> None:
        assert build_agent_phase("Running", "Unknown") == CalicoAgentPhase.RUNNING

    def test_pending_is_unknown(self) -> None:
        assert build_agent_phase("Pending", "Unknown") == CalicoAgentPhase.UNKNOWN


class TestBuildDegradedSummary:
    def _agent(self, node: str, healthy_status: str = "True") -> CalicoNodeAgent:
        healthy = healthy_status == "True"
        return CalicoNodeAgent(
            node=node,
            phase=CalicoAgentPhase.READY if healthy else CalicoAgentPhase.NOT_READY,
            ready=healthy,
            ready_replicas=1 if healthy else 0,
            desired_replicas=1,
            available_replicas=1 if healthy else 0,
        )

    def test_empty_list_returns_none(self) -> None:
        assert build_degraded_summary([]) is None

    def test_all_healthy_returns_none(self) -> None:
        assert build_degraded_summary([self._agent("a")]) is None

    def test_one_degraded(self) -> None:
        summary = build_degraded_summary([self._agent("a"), self._agent("b", "False")])
        assert summary is not None
        assert "1/2" in summary
        assert "degraded" in summary

    def test_all_degraded(self) -> None:
        summary = build_degraded_summary([self._agent("a", "False"), self._agent("b", "False")])
        assert summary is not None
        assert "0/2" in summary


class TestBuildDetectionResult:
    def _signals(self, **overrides: object) -> CalicoDetectionSignals:
        base: dict[str, object] = {
            "installed": True,
            "version": "v3.26.1",
            "namespace": "calico-system",
            "mode_signals": {"ipip"},
            "tigera_operator": False,
            "enterprise": False,
            "agents": [self._agent("a"), self._agent("b")],
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionSignals(**base)  # type: ignore[arg-type]

    def _agent(self, node: str, healthy_status: str = "True") -> CalicoNodeAgent:
        healthy = healthy_status == "True"
        return CalicoNodeAgent(
            node=node,
            phase=CalicoAgentPhase.READY if healthy else CalicoAgentPhase.NOT_READY,
            ready=healthy,
            ready_replicas=1 if healthy else 0,
            desired_replicas=1,
            available_replicas=1 if healthy else 0,
        )

    def test_not_installed_honest(self) -> None:
        result = build_detection_result(
            CalicoDetectionSignals(
                installed=False,
                version=None,
                namespace=None,
                mode_signals=set(),
                tigera_operator=False,
                enterprise=False,
                agents=[],
                error=None,
            )
        )
        assert result.installed is False
        assert result.status == CalicoDetectionStatus.NOT_INSTALLED
        assert result.not_installed_marker == NOT_INSTALLED_MARKER
        assert result.mode == DataplaneMode.UNKNOWN
        assert result.version is None

    def test_installed_healthy(self) -> None:
        result = build_detection_result(self._signals())
        assert result.status == CalicoDetectionStatus.INSTALLED
        assert result.mode == DataplaneMode.IPIP
        assert result.total_nodes == 2  # noqa: PLR2004
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.degraded_agents == 0
        assert result.degraded_summary is None

    def test_installed_degraded(self) -> None:
        signals = self._signals(agents=[self._agent("a"), self._agent("b", "False")])
        result = build_detection_result(signals)
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_agents == 1
        assert result.degraded_summary is not None
        assert "1/2" in result.degraded_summary

    def test_empty_agents_when_installed_is_degraded(self) -> None:
        result = build_detection_result(self._signals(agents=[]))
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.total_nodes == 0
        assert result.degraded_summary is not None

    def test_version_raw_preserved(self) -> None:
        result = build_detection_result(self._signals(version="v3.28.0-rc.1"))
        assert result.version == "v3.28.0-rc.1"

    def test_tigera_enterprise_flags(self) -> None:
        result = build_detection_result(self._signals(tigera_operator=True, enterprise=True))
        assert result.tigera_operator is True
        assert result.enterprise is True

    def test_each_agent_summary_reflects_phase(self) -> None:
        result = build_detection_result(self._signals())
        assert all(a.phase == CalicoAgentPhase.READY for a in result.agents)
