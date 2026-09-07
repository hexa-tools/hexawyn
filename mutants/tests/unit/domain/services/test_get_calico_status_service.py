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
    _compose_degraded_summary,
    _connectivity_status,
    _felix_error_total,
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
        assert result.ready_agents == 0
        assert result.agents == []
        assert result.degraded_summary is None
        assert result.felix_errors_available is False
        assert result.felix_errors is None
        assert result.connectivity_available is False
        assert result.connectivity_status is None
        assert result.connectivity_detail is None
        assert result.error is None

    def test_not_installed_forwards_detection_error(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            agents=[],
            total_nodes=0,
            ready_agents=0,
            error="kube api unreachable",
        )
        result = build_calico_status_result(detection=detection, connectivity={}, felix={})
        assert result.error == "kube api unreachable"

    def test_healthy(self) -> None:
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.INSTALLED
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.degraded_summary is None
        assert result.agents == [self._agent("a"), self._agent("b")]
        assert result.felix_errors_available is True
        assert result.felix_errors == 0
        assert result.connectivity_available is True
        assert result.connectivity_status == "healthy"
        assert result.connectivity_detail is None
        assert result.error is None

    def test_installed_forwards_detection_error(self) -> None:
        detection = self._detection(error="partial felix metrics")
        result = build_calico_status_result(
            detection=detection,
            connectivity=self._healthy_connectivity(),
            felix=self._healthy_felix(),
        )
        assert result.installed is True
        assert result.error == "partial felix metrics"

    def test_degraded_by_felix_errors(self) -> None:
        felix = {"available": True, "metrics": {"felix_int_dataplane_errors": 3.0}}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=felix,
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.felix_errors == 3  # noqa: PLR2004
        assert result.degraded_summary == "3 felix dataplane errors"

    def test_degraded_by_single_felix_error(self) -> None:
        felix = {"available": True, "metrics": {"felix_int_dataplane_errors": 1.0}}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=self._healthy_connectivity(),
            felix=felix,
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.degraded_summary == "1 felix dataplane errors"

    def test_degraded_by_connectivity(self) -> None:
        connectivity = {"available": True, "status": "degraded", "active_endpoint_agents": 0}
        result = build_calico_status_result(
            detection=self._detection(),
            connectivity=connectivity,
            felix=self._healthy_felix(),
        )
        assert result.status == CalicoDetectionStatus.DEGRADED
        assert result.connectivity_status == "degraded"
        assert result.degraded_summary == "dataplane connectivity degraded"

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
        assert result.degraded_summary == "1/2 calico-node agents ready (1 degraded)"

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


class TestConnectivityStatusDirect:
    """Direct coverage of the _connectivity_status helper branches."""

    def test_unavailable_returns_none(self) -> None:
        assert _connectivity_status({"available": False, "status": "degraded"}) is None

    def test_no_status_returns_none(self) -> None:
        assert _connectivity_status({"available": True}) is None

    def test_healthy_status_trusted_without_agent_breakdown(self) -> None:
        assert _connectivity_status({"available": True, "status": "healthy"}) == "healthy"

    def test_healthy_status_trusted_with_zero_agents(self) -> None:
        status = _connectivity_status(
            {"available": True, "status": "healthy", "active_endpoint_agents": 0}
        )
        assert status == "healthy"

    def test_degraded_status_trusted_with_agents_present(self) -> None:
        status = _connectivity_status(
            {"available": True, "status": "degraded", "active_endpoint_agents": 2}
        )
        assert status == "degraded"

    def test_unknown_status_falls_back_degraded_without_agents(self) -> None:
        status = _connectivity_status(
            {"available": True, "status": "unknown", "active_endpoint_agents": 0}
        )
        assert status == "degraded"

    def test_unknown_status_falls_back_healthy_with_agents(self) -> None:
        status = _connectivity_status(
            {"available": True, "status": "unknown", "active_endpoint_agents": 3}
        )
        assert status == "healthy"

    def test_case_sensitive_status_ignored(self) -> None:
        status = _connectivity_status(
            {"available": True, "status": "HEALTHY", "active_endpoint_agents": 2}
        )
        assert status == "healthy"


class TestFelixErrorTotalDirect:
    """Direct coverage of the _felix_error_total aggregation rules."""

    def test_unavailable_returns_none(self) -> None:
        assert _felix_error_total({"available": False}) is None

    def test_non_mapping_metrics_returns_zero(self) -> None:
        assert _felix_error_total({"available": True, "metrics": None}) == 0

    def test_no_error_keys_returns_zero(self) -> None:
        metrics = {"felix_active_local_endpoints": 2.0}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 0

    def test_single_numeric_error_key_sums(self) -> None:
        metrics = {"felix_int_dataplane_errors": 3.0}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 3  # noqa: PLR2004

    def test_multiple_numeric_error_keys_accumulate(self) -> None:
        metrics = {"felix_a_errors": 1.0, "felix_b_errors": 2.0}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 3  # noqa: PLR2004

    def test_error_key_with_error_substring_counts(self) -> None:
        metrics = {"felix_dataplane_errors_total": 5.0}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 5  # noqa: PLR2004

    def test_non_numeric_key_before_numeric_keeps_scanning(self) -> None:
        metrics = {"felix_a_error": "not-a-number", "felix_b_errors": 2.0}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 2  # noqa: PLR2004

    def test_numeric_key_before_non_numeric_keeps_result(self) -> None:
        metrics = {"felix_a_errors": 2.0, "felix_b_error": "not-a-number"}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 2  # noqa: PLR2004

    def test_all_non_numeric_returns_zero(self) -> None:
        metrics = {"felix_a_error": "oops", "felix_b_error": "not-a-number"}
        assert _felix_error_total({"available": True, "metrics": metrics}) == 0


class TestComposeDegradedSummaryDirect:
    """Direct coverage of the _compose_degraded_summary string builder."""

    def test_agent_summary_used_verbatim(self) -> None:
        summary = _compose_degraded_summary(
            ready=1,
            total=2,
            agent_summary="1/2 calico-node agents ready (1 degraded)",
            felix_errors=None,
            connectivity_status=None,
        )
        assert summary == "1/2 calico-node agents ready (1 degraded)"

    def test_ready_shortfall_single_agent_boundary(self) -> None:
        summary = _compose_degraded_summary(
            ready=0,
            total=1,
            agent_summary=None,
            felix_errors=None,
            connectivity_status=None,
        )
        assert summary == "0/1 calico-node agents ready"

    def test_ready_shortfall_two_of_two_not_degraded(self) -> None:
        summary = _compose_degraded_summary(
            ready=2,
            total=2,
            agent_summary=None,
            felix_errors=None,
            connectivity_status=None,
        )
        assert summary == "Calico datapath degraded"

    def test_zero_total_detected(self) -> None:
        summary = _compose_degraded_summary(
            ready=0,
            total=0,
            agent_summary=None,
            felix_errors=None,
            connectivity_status=None,
        )
        assert summary == "0 calico-node agents detected"

    def test_felix_errors_single_boundary(self) -> None:
        summary = _compose_degraded_summary(
            ready=2,
            total=2,
            agent_summary=None,
            felix_errors=1,
            connectivity_status=None,
        )
        assert summary == "1 felix dataplane errors"

    def test_connectivity_degraded_part(self) -> None:
        summary = _compose_degraded_summary(
            ready=2,
            total=2,
            agent_summary=None,
            felix_errors=None,
            connectivity_status="degraded",
        )
        assert summary == "dataplane connectivity degraded"

    def test_ready_shortfall_takes_precedence_over_agent_summary(self) -> None:
        summary = _compose_degraded_summary(
            ready=1,
            total=2,
            agent_summary=None,
            felix_errors=None,
            connectivity_status=None,
        )
        assert summary == "1/2 calico-node agents ready"

    def test_multiple_parts_joined_with_semicolon(self) -> None:
        summary = _compose_degraded_summary(
            ready=1,
            total=2,
            agent_summary=None,
            felix_errors=3,
            connectivity_status="degraded",
        )
        assert summary == (
            "1/2 calico-node agents ready; 3 felix dataplane errors; "
            "dataplane connectivity degraded"
        )

    def test_connectivity_healthy_not_reported_as_degraded(self) -> None:
        summary = _compose_degraded_summary(
            ready=2,
            total=2,
            agent_summary=None,
            felix_errors=None,
            connectivity_status="healthy",
        )
        assert summary == "Calico datapath degraded"
