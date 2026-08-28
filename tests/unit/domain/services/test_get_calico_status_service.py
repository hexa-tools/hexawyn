"""Tests for domain/services/calico — get_calico_status composition."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    DataplaneMode,
)
from hexawyn.domain.services.calico.get_calico_status_service import (
    build_calico_status_result,
)


class TestBuildCalicoStatusResult:
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
            "agents": [self._agent("a"), self._agent("b")],
            "total_nodes": 2,
            "ready_agents": 2,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

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

    def _healthy_connectivity(self) -> dict[str, object]:
        return {"available": True, "status": "healthy", "active_endpoint_agents": 2}

    def _healthy_felix(self) -> dict[str, object]:
        return {"available": True, "metrics": {"felix_active_local_endpoints": 2.0}}

    def test_not_installed(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            agents=[],
            total_nodes=0,
            ready_agents=0,
        )
        result = build_calico_status_result(detection=detection, connectivity={}, felix={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.status == CalicoDetectionStatus.NOT_INSTALLED
        assert result.total_agents == 0

    def test_healthy(self) -> None:
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.INSTALLED
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.degraded_summary is None
        assert result.connectivity_status == "healthy"
        assert result.felix_errors == 0

    def test_degraded_by_agents(self) -> None:
        detection = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            agents=[self._agent("a"), self._agent("b", "False")],
            total_nodes=2,
            ready_agents=1,
            degraded_agents=1,
            degraded_summary="1/2 calico-node agents ready (1 degraded)",
        )
        result = build_calico_status_result(
            detection=detection,
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_summary is not None
        assert "1/2" in result.degraded_summary

    def test_degraded_by_felix_errors(self) -> None:
        felix = {"available": True, "metrics": {"felix_int_dataplane_errors": 3.0}}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=felix,
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.felix_errors == 3  # noqa: PLR2004
        assert result.degraded_summary is not None

    def test_degraded_by_connectivity(self) -> None:
        connectivity = {"available": True, "status": "degraded", "active_endpoint_agents": 0}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=connectivity,
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.connectivity_status == "degraded"

    def test_connectivity_unavailable_passthrough(self) -> None:
        connectivity = {"available": False, "status": "degraded", "detail": "no metrics port"}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=connectivity,
            felix=self._healthy_felix(),
        )
        assert result.connectivity_available is False
        assert result.connectivity_status is None
        assert result.connectivity_detail == "no metrics port"

    def test_felix_unavailable(self) -> None:
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix={"available": False},
        )
        assert result.felix_errors_available is False
        assert result.felix_errors is None

    def test_empty_agents_installed_is_degraded(self) -> None:
        detection = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            agents=[],
            total_nodes=0,
            ready_agents=0,
            degraded_summary="0 calico-node agents detected",
        )
        result = build_calico_status_result(
            detection=detection,
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.total_agents == 0

    def test_felix_metrics_missing_metrics(self) -> None:
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix={"available": True, "metrics": None},
        )
        assert result.felix_errors_available is True
        assert result.felix_errors == 0

    def test_felix_error_non_numeric_skipped(self) -> None:
        felix = {"available": True, "metrics": {"felix_error": "not-a-number"}}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=felix,
        )
        assert result.felix_errors == 0
        assert result.status == CalicoDetectionStatus.INSTALLED

    def test_connectivity_available_no_status(self) -> None:
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity={"available": True},
            felix=self._healthy_felix(),
        )
        assert result.connectivity_available is True
        assert result.connectivity_status is None

    def test_connectivity_unknown_status_falls_back_degraded(self) -> None:
        connectivity = {"available": True, "status": "unknown", "active_endpoint_agents": 0}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=connectivity,
            felix=self._healthy_felix(),
        )
        assert result.connectivity_status == "degraded"
        assert result.status == CalicoDetectionStatus.DEGRADED

    def test_degraded_agents_without_agent_summary(self) -> None:
        detection = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            degraded_summary=None,
            agents=[self._agent("a"), self._agent("b", "False")],
            total_nodes=2,
            ready_agents=1,
            degraded_agents=1,
        )
        result = build_calico_status_result(
            detection=detection,
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_summary == "1/2 calico-node agents ready"

    def test_degraded_zero_total_without_agent_summary(self) -> None:
        detection = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            degraded_summary=None,
            agents=[],
            total_nodes=0,
            ready_agents=0,
            degraded_agents=0,
        )
        result = build_calico_status_result(
            detection=detection,
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_summary == "0 calico-node agents detected"

    def test_degraded_fallback_generic_summary(self) -> None:
        detection = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            degraded_summary=None,
            agents=[self._agent("a"), self._agent("b")],
            total_nodes=2,
            ready_agents=2,
            degraded_agents=0,
        )
        result = build_calico_status_result(
            detection=detection,
            connectivity={"available": True, "status": "healthy", "active_endpoint_agents": 2},
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_summary == "Calico datapath degraded"
