from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    AdaptiveInvestigationReport,
    AdaptiveInvestigationRequest,
    OverviewSnapshot,
    RankedFailingResource,
    ResourceInvestigation,
)


class TestBuildAdaptiveInvestigation:
    def test_happy_path_builds_report(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="default", depth=3)
        overview = OverviewSnapshot(
            namespace="default",
            namespace_status="active",
            health_status="degraded",
            summary="Namespace is degraded",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="api-server",
                    kind="Deployment",
                    reason="CrashLoopBackOff",
                    restart_count=5,
                    rank=0,
                ),
                events=["Back-off restarting failed container"],
                logs=["panic: runtime error"],
                last_termination_reason="Error",
            ),
        ]
        skipped: list[str] = []

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=skipped,
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert isinstance(report, AdaptiveInvestigationReport)
        assert report.namespace == "default"
        assert report.namespace_status == "active"
        assert report.health_status == "degraded"
        assert report.overview_summary == "Namespace is degraded"
        assert len(report.investigated_resources) == 1
        assert len(report.root_cause_candidates) == 1
        assert report.has_more_failing is False
        assert report.remaining_failing_count == 0

    def test_empty_investigated_resources(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="empty-ns")
        overview = OverviewSnapshot(
            namespace="empty-ns",
            namespace_status="active",
            health_status="healthy",
            summary="All good",
        )

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=[],
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert len(report.root_cause_candidates) == 0
        assert len(report.recommended_actions) == 0

    def test_root_cause_sorted_by_confidence_descending(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="Degraded",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="unknown-pod",
                    kind="Pod",
                    reason="ExitCode:1",
                    restart_count=2,
                    rank=1,
                ),
                events=["container exited with code 1"],
                logs=[],
            ),
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="oom-pod",
                    kind="Pod",
                    reason="OOMKilled",
                    restart_count=3,
                    rank=0,
                ),
                events=["OOMKilled"],
                logs=["Out of memory error"],
            ),
        ]

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        candidates = report.root_cause_candidates
        assert len(candidates) == 2  # noqa: PLR2004
        assert candidates[0].confidence >= candidates[1].confidence

    def test_skip_duplicate_recommended_actions(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="Multiple OOM",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="pod-a",
                    kind="Pod",
                    reason="OOMKilled",
                    restart_count=1,
                    rank=0,
                ),
                events=["Out of memory"],
                logs=["memory exhausted"],
            ),
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="pod-b",
                    kind="Pod",
                    reason="OOMKilled",
                    restart_count=1,
                    rank=1,
                ),
                events=["Out of memory"],
                logs=["memory exhausted"],
            ),
        ]

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        assert len(report.recommended_actions) == 1

    def test_has_more_failing_and_remaining_count_preserved(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="Many failures",
        )

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=[],
            skipped_resources=["pod-z", "pod-y"],
            node_pressure_context="Node under disk pressure",
            has_more_failing=True,
            remaining_failing_count=5,
        )

        assert report.has_more_failing is True
        assert report.remaining_failing_count == 5  # noqa: PLR2004
        assert report.skipped_resources == ["pod-z", "pod-y"]
        assert report.node_pressure_context == "Node under disk pressure"

    def test_candidates_use_termination_reason_in_evidence(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="Terminated pod",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="terminated-pod",
                    kind="Pod",
                    reason="Error",
                    restart_count=1,
                    rank=0,
                ),
                events=[],
                logs=[],
                last_termination_reason="OOMKilled",
            ),
        ]

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        candidate = report.root_cause_candidates[0]
        any_has_term = any("termination reason" in e.lower() for e in candidate.evidence)
        any_has_oom = any("OOMKilled" in e for e in candidate.evidence)
        assert any_has_term or any_has_oom

    def test_candidate_unknown_gives_low_confidence(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="Unknown",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="mystery-pod",
                    kind="Pod",
                    reason="SomethingWentWrong",
                    restart_count=1,
                    rank=0,
                ),
                events=[],
                logs=[],
                last_termination_reason=None,
            ),
        ]

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        candidate = report.root_cause_candidates[0]
        assert candidate.confidence == 0.3  # noqa: PLR2004

    def test_candidate_known_gives_high_confidence(self) -> None:
        from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
            build_adaptive_investigation,
        )

        request = AdaptiveInvestigationRequest(namespace="ns")
        overview = OverviewSnapshot(
            namespace="ns",
            namespace_status="active",
            health_status="degraded",
            summary="OOM",
        )
        investigated = [
            ResourceInvestigation(
                resource=RankedFailingResource(
                    name="oom-pod",
                    kind="Pod",
                    reason="OOMKilled",
                    restart_count=5,
                    rank=0,
                ),
                events=["The pod was OOMKilled"],
                logs=["Out of memory: killed process"],
                last_termination_reason="OOMKilled",
            ),
        ]

        report = build_adaptive_investigation(
            request=request,
            overview=overview,
            investigated_resources=investigated,
            skipped_resources=[],
            node_pressure_context=None,
            has_more_failing=False,
            remaining_failing_count=0,
        )

        candidate = report.root_cause_candidates[0]
        assert candidate.confidence == 0.85  # noqa: PLR2004
