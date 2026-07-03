"""Unit tests for search_resources_by_labels — pure domain orchestration.

Test data mirrors the ticket's own fixture: label_selector "app=payment,env=production",
payment-pod-abc12 (production, Running), payment-pod-def34 (staging, CrashLoopBackOff).
"""

from __future__ import annotations

from hexawyn.application.ports.driven.resource_search_port import MatchedResourceRaw
from hexawyn.domain.models.label_search import LabelSearchRequest
from hexawyn.domain.services.label_search.search import search_resources_by_labels


def _raw(
    name: str,
    namespace: str,
    kind: str = "pod",
    node: str | None = "worker-1",
    phase: str | None = "Running",
    ready: bool | None = True,
) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=name,
        namespace=namespace,
        kind=kind,
        node=node,
        phase=phase,
        ready=ready,
        labels={"app": "payment"},
    )


def _request(namespace: str | None = None) -> LabelSearchRequest:
    return LabelSearchRequest(label_selector="app=payment,env=production", namespace=namespace)


class TestThreePodsAcrossTwoNamespaces:
    """TC1: Labels app=payment,env=production → returns 3 pods across 2 namespaces."""

    def test_grouped_by_namespace(self) -> None:
        raw_matches = [
            _raw("payment-pod-abc12", "production"),
            _raw("payment-pod-ghi56", "production"),
            _raw("payment-pod-def34", "staging", phase="CrashLoopBackOff", ready=False),
        ]

        result = search_resources_by_labels(_request(), raw_matches)

        assert result.total_matched == 3
        assert len(result.groups) == 2
        by_ns = {group.namespace: group for group in result.groups}
        assert len(by_ns["production"].resources) == 2
        assert len(by_ns["staging"].resources) == 1


class TestNoMatches:
    """TC2: No resources match labels → empty result with clear message."""

    def test_empty_result_with_message(self) -> None:
        result = search_resources_by_labels(_request(), [])

        assert result.no_matches is True
        assert result.total_matched == 0
        assert result.groups == []
        assert "app=payment" in result.summary


class TestMixedResourceKinds:
    """TC3: Single label app=payment matches pods and services → both returned."""

    def test_pods_and_services_both_present(self) -> None:
        raw_matches = [
            _raw("payment-pod-abc12", "production"),
            _raw(
                "payment-service",
                "production",
                kind="service",
                node=None,
                phase=None,
                ready=None,
            ),
        ]

        result = search_resources_by_labels(_request(), raw_matches)

        kinds = {resource.kind for group in result.groups for resource in group.resources}
        assert kinds == {"pod", "service"}


class TestHealthFlagging:
    """TC4 (all healthy) and TC5 (one CrashLoopBackOff flagged)."""

    def test_all_running_pods_summary_shows_healthy(self) -> None:
        raw_matches = [_raw("pod-a", "production"), _raw("pod-b", "production")]

        result = search_resources_by_labels(_request(), raw_matches)

        assert "healthy" in result.summary.lower()
        assert all(resource.is_healthy for group in result.groups for resource in group.resources)

    def test_crashloopbackoff_pod_flagged(self) -> None:
        raw_matches = [
            _raw("payment-pod-abc12", "production"),
            _raw("payment-pod-def34", "staging", phase="CrashLoopBackOff", ready=False),
        ]

        result = search_resources_by_labels(_request(), raw_matches)

        unhealthy = [
            resource
            for group in result.groups
            for resource in group.resources
            if resource.is_healthy is False
        ]
        assert len(unhealthy) == 1
        assert unhealthy[0].name == "payment-pod-def34"
        assert "payment-pod-def34" in result.summary
        assert "CrashLoopBackOff" in result.summary


class TestNonPodResourceHasNoPhase:
    """Edge case: resource has labels but no status.phase (non-pod resources)."""

    def test_service_is_healthy_none_not_flagged(self) -> None:
        raw_matches = [
            _raw("payment-service", "production", kind="service", node=None, phase=None, ready=None)
        ]

        result = search_resources_by_labels(_request(), raw_matches)

        resource = result.groups[0].resources[0]
        assert resource.is_healthy is None
        assert "unhealthy" not in result.summary.lower()


class TestTruncation:
    """Edge case: large result set (>500 matching resources) → truncation with count."""

    def test_more_than_max_results_is_truncated(self) -> None:
        raw_matches = [_raw(f"pod-{i}", "production") for i in range(600)]

        result = search_resources_by_labels(_request(), raw_matches)

        assert result.total_matched == 600
        assert result.has_more is True
        assert result.remaining_count == 100
        total_returned = sum(len(group.resources) for group in result.groups)
        assert total_returned == 500
