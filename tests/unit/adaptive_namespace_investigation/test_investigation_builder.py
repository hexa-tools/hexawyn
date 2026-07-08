"""Unit tests for build_adaptive_investigation — pure composition of the final
report from already-ranked, already-drilled resource investigations."""

from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    AdaptiveInvestigationRequest,
    OverviewSnapshot,
    RankedFailingResource,
    ResourceInvestigation,
    UnhealthyResourceRef,
)
from hexawyn.domain.models.incident_triage import IncidentCauseCategory
from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
    build_adaptive_investigation,
)


def _overview(unhealthy: list[UnhealthyResourceRef] | None = None) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace="production",
        namespace_status="Active",
        health_status="Critical",
        unhealthy_resources=unhealthy or [],
        summary="2 unhealthy resource(s) found in 'production'.",
    )


def _request(depth: int = 3) -> AdaptiveInvestigationRequest:
    return AdaptiveInvestigationRequest(namespace="production", depth=depth)


class TestNoFailingResources:
    def test_healthy_summary_no_drilldown(self) -> None:
        """TC2: no failing resources → healthy summary, no drill-down."""
        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=[],
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert report.investigated_resources == []
        assert report.root_cause_candidates == []
        assert report.recommended_actions == []
        assert report.namespace == "production"


class TestOomFlagging:
    def test_oom_flagged_in_root_cause_candidates(self) -> None:
        """TC4: failing deployment with OOMKilled containers → OOM flagged in
        root cause candidates."""
        resource = RankedFailingResource(
            name="auth-deploy-xyz", kind="Pod", reason="OOMKilled", restart_count=12, rank=0
        )
        investigation = ResourceInvestigation(
            resource=resource,
            events=["OOMKilling: Memory cgroup out of memory (x3)"],
            logs=[],
            last_termination_reason="OOMKilled",
        )

        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(
                [UnhealthyResourceRef(name="auth-deploy-xyz", kind="Pod", reason="OOMKilled")]
            ),
            investigated_resources=[investigation],
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert len(report.root_cause_candidates) == 1
        candidate = report.root_cause_candidates[0]
        assert candidate.category == IncidentCauseCategory.RESOURCE_EXHAUSTION
        assert "auth-deploy-xyz" in candidate.involved_objects
        assert any("OOM" in e for e in candidate.evidence)
        assert report.recommended_actions


class TestEmptyEvents:
    def test_investigation_continues_with_available_data(self) -> None:
        """Edge case: pod events empty → investigation continues with
        available data (logs alone)."""
        resource = RankedFailingResource(
            name="payment-pod-abc",
            kind="Pod",
            reason="CrashLoopBackOff",
            restart_count=45,
            rank=0,
        )
        investigation = ResourceInvestigation(
            resource=resource,
            events=[],
            logs=["panic: runtime error: invalid memory address"],
            last_termination_reason=None,
        )

        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=[investigation],
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert len(report.investigated_resources) == 1
        assert len(report.root_cause_candidates) == 1


class TestSkippedResources:
    def test_skipped_resources_passed_through(self) -> None:
        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=[],
            skipped_resources=["ghost-pod"],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert report.skipped_resources == ["ghost-pod"]


class TestNodePressureContext:
    def test_node_pressure_context_passed_through(self) -> None:
        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=[],
            skipped_resources=[],
            node_pressure_context="3 pod(s) pending — likely cluster resource pressure.",
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert (
            report.node_pressure_context == "3 pod(s) pending — likely cluster resource pressure."
        )


class TestRootCauseRankingAndDedup:
    def test_candidates_sorted_by_confidence_descending_and_actions_deduped(self) -> None:
        crash_resource = RankedFailingResource(
            name="payment-pod-abc", kind="Pod", reason="CrashLoopBackOff", restart_count=45, rank=0
        )
        unknown_resource = RankedFailingResource(
            name="weird-pod", kind="Pod", reason="Error", restart_count=2, rank=1
        )
        investigations = [
            ResourceInvestigation(
                resource=unknown_resource, events=[], logs=["something strange happened"]
            ),
            ResourceInvestigation(
                resource=crash_resource,
                events=["BackOff: Back-off restarting failed container (x10)"],
                logs=["panic: runtime error"],
            ),
        ]

        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=investigations,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert (
            report.root_cause_candidates[0].confidence >= report.root_cause_candidates[1].confidence
        )
        assert len(report.recommended_actions) == len(set(report.recommended_actions))

    def test_has_more_failing_passthrough(self) -> None:
        report = build_adaptive_investigation(
            request=_request(),
            overview=_overview(),
            investigated_resources=[],
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=True,
            remaining_failing_count=47,
        )

        assert report.has_more_failing is True
        assert report.remaining_failing_count == 47
