"""Unit tests for the Adaptive Namespace Investigation domain models — pure
dataclasses, no I/O."""

from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    AdaptiveInvestigationReport,
    AdaptiveInvestigationRequest,
    RankedFailingResource,
    ResourceInvestigation,
    UnhealthyResourceRef,
)


class TestUnhealthyResourceRef:
    def test_fields(self) -> None:
        ref = UnhealthyResourceRef(name="payment-pod-abc", kind="Pod", reason="CrashLoopBackOff")

        assert ref.name == "payment-pod-abc"
        assert ref.kind == "Pod"
        assert ref.reason == "CrashLoopBackOff"


class TestRankedFailingResource:
    def test_fields(self) -> None:
        ranked = RankedFailingResource(
            name="payment-pod-abc",
            kind="Pod",
            reason="CrashLoopBackOff",
            restart_count=45,
            rank=0,
        )

        assert ranked.restart_count == 45
        assert ranked.rank == 0


class TestResourceInvestigation:
    def test_defaults(self) -> None:
        resource = RankedFailingResource(
            name="auth-pod-xyz", kind="Pod", reason="OOMKilled", restart_count=12, rank=1
        )

        investigation = ResourceInvestigation(resource=resource, events=[], logs=[])

        assert investigation.last_termination_reason is None
        assert investigation.events == []
        assert investigation.logs == []


class TestAdaptiveInvestigationRequest:
    def test_default_depth(self) -> None:
        request = AdaptiveInvestigationRequest(namespace="production")

        assert request.depth == 3

    def test_custom_depth(self) -> None:
        request = AdaptiveInvestigationRequest(namespace="production", depth=1)

        assert request.depth == 1


class TestAdaptiveInvestigationReport:
    def test_defaults(self) -> None:
        report = AdaptiveInvestigationReport(
            namespace="production",
            namespace_status="Active",
            health_status="Critical",
            overview_summary="2 unhealthy resource(s) found in 'production'.",
        )

        assert report.investigated_resources == []
        assert report.root_cause_candidates == []
        assert report.recommended_actions == []
        assert report.skipped_resources == []
        assert report.node_pressure_context is None
        assert report.has_more_failing is False
        assert report.remaining_failing_count == 0
