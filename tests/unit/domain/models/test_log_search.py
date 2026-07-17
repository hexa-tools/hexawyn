"""Unit tests for pod-log-search domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.log_search import (
    LogSearchRequest,
    LogSearchResult,
    MatchedLogLine,
    PodLogMatch,
    ServiceGroup,
    SkippedNamespace,
    SkippedPod,
)


class TestMatchedLogLine:
    def test_exact_match_fields(self) -> None:
        line = MatchedLogLine(
            timestamp="2024-01-01T10:32:15Z",
            message="ERROR: connection refused to postgres at 10:32:15",
            match_type="exact",
        )
        assert line.match_type == "exact"

    def test_semantic_match_fields(self) -> None:
        line = MatchedLogLine(timestamp="", message="db timeout", match_type="semantic")
        assert line.match_type == "semantic"


class TestPodLogMatch:
    def test_fields(self) -> None:
        match = PodLogMatch(
            pod_name="checkout-pod-xyz",
            namespace="production",
            container="checkout-app",
            matching_lines=[MatchedLogLine(timestamp="t", message="m", match_type="exact")],
        )
        assert match.container == "checkout-app"
        assert len(match.matching_lines) == 1


class TestServiceGroup:
    def test_fields(self) -> None:
        match = PodLogMatch(
            pod_name="checkout-pod-xyz", namespace="production", container="checkout-app"
        )
        group = ServiceGroup(service_name="checkout", namespace="production", pods=[match])
        assert group.service_name == "checkout"
        assert len(group.pods) == 1


class TestSkippedPod:
    def test_fields(self) -> None:
        skipped = SkippedPod(
            pod_name="pending-pod", namespace="production", reason="Pending: no logs available"
        )
        assert "Pending" in skipped.reason


class TestSkippedNamespace:
    def test_fields(self) -> None:
        skipped = SkippedNamespace(namespace="kube-system", reason="RBAC denied")
        assert skipped.namespace == "kube-system"


class TestLogSearchRequest:
    def test_defaults(self) -> None:
        request = LogSearchRequest(pattern="connection refused to postgres")
        assert request.is_regex is False
        assert request.namespace is None
        assert request.time_window_minutes == 60

    def test_custom_values(self) -> None:
        request = LogSearchRequest(
            pattern="foo.*bar", is_regex=True, namespace="production", time_window_minutes=15
        )
        assert request.is_regex is True
        assert request.namespace == "production"
        assert request.time_window_minutes == 15


class TestLogSearchResult:
    def test_defaults(self) -> None:
        result = LogSearchResult(
            pattern="connection refused to postgres",
            time_window_minutes=60,
            namespaces_total=1,
        )
        assert result.groups == []
        assert result.pods_affected == 0
        assert result.services_affected == 0
        assert result.skipped_pods == []
        assert result.skipped_namespaces == []
        assert result.scanned_namespaces == []
        assert result.no_matches is False
        assert result.summary == ""

    def test_with_groups(self) -> None:
        match = PodLogMatch(
            pod_name="checkout-pod-xyz", namespace="production", container="checkout-app"
        )
        group = ServiceGroup(service_name="checkout", namespace="production", pods=[match])
        result = LogSearchResult(
            pattern="app",
            time_window_minutes=60,
            namespaces_total=1,
            groups=[group],
            pods_affected=1,
            services_affected=1,
        )
        assert len(result.groups) == 1
        assert result.pods_affected == 1
