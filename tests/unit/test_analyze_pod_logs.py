"""Unit tests for analyze_pod_logs domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.analyze_pod_logs import (
    AnalyzePodLogsRequest,
    AnalyzePodLogsResult,
    ConnectionIssue,
    LogPatternMatch,
    PodLogLine,
    PodRunSummary,
)
from hexawyn.domain.models.log import RankedEvent


class TestPodLogLine:
    def test_is_error_for_error_level(self) -> None:
        line = PodLogLine(timestamp="T1", level="ERROR", message="boom", run_index=0, is_json=False)
        assert line.is_error is True
        assert line.is_warning is False

    def test_is_warning_for_warn_level(self) -> None:
        line = PodLogLine(
            timestamp="T1", level="WARN", message="careful", run_index=0, is_json=False
        )
        assert line.is_warning is True
        assert line.is_error is False

    def test_info_is_neither(self) -> None:
        line = PodLogLine(timestamp="T1", level="INFO", message="ok", run_index=0, is_json=False)
        assert line.is_error is False
        assert line.is_warning is False

    def test_level_matching_is_case_insensitive(self) -> None:
        line = PodLogLine(timestamp="T1", level="error", message="boom", run_index=0, is_json=False)
        assert line.is_error is True


class TestConnectionIssue:
    def test_fields(self) -> None:
        issue = ConnectionIssue(
            category="connection_refused",
            message_sample="upstream connect error",
            count=3,
            confidence=0.65,
        )
        assert issue.category == "connection_refused"
        assert issue.count == 3


class TestLogPatternMatch:
    def test_fields(self) -> None:
        pattern = LogPatternMatch(pattern="connection refused", count=3, confidence=0.65)
        assert pattern.pattern == "connection refused"
        assert pattern.count == 3


class TestPodRunSummary:
    def test_fields(self) -> None:
        summary = PodRunSummary(run_index=1, line_count=42, error_count=2, warning_count=1)
        assert summary.run_index == 1
        assert summary.line_count == 42


class TestAnalyzePodLogsRequest:
    def test_defaults(self) -> None:
        req = AnalyzePodLogsRequest(pod_name="api-gateway-7f9b", namespace="prod")
        assert req.time_window_minutes == 30

    def test_explicit_window(self) -> None:
        req = AnalyzePodLogsRequest(
            pod_name="api-gateway-7f9b", namespace="prod", time_window_minutes=60
        )
        assert req.time_window_minutes == 60


class TestAnalyzePodLogsResult:
    def test_fields(self) -> None:
        result = AnalyzePodLogsResult(
            pod_name="api-gateway-7f9b",
            namespace="prod",
            time_window_minutes=30,
            strategy_used="smart_summary",
            total_lines=500,
            error_count=15,
            warning_count=2,
            patterns=[LogPatternMatch(pattern="connection timeout", count=15, confidence=0.9)],
            connection_timeouts=[
                ConnectionIssue(
                    category="connection_timeout",
                    message_sample="connection timeout to postgres:5432",
                    count=15,
                    confidence=0.9,
                )
            ],
            connection_refused=[],
            confidence=0.85,
            summary="High error rate",
            restarts_detected=False,
            runs=[PodRunSummary(run_index=0, line_count=500, error_count=15, warning_count=2)],
            sanitized_binary=False,
            token_reduction_percentage=95.0,
            degraded=False,
        )
        assert result.total_lines == 500
        assert result.error_count == 15
        assert len(result.connection_timeouts) == 1
        assert result.restarts_detected is False
        assert result.token_reduction_percentage == 95.0
        assert result.degraded is False

    def test_defaults_for_reduction_metrics(self) -> None:
        result = AnalyzePodLogsResult(
            pod_name="p",
            namespace="ns",
            time_window_minutes=30,
            strategy_used="smart_summary",
            total_lines=0,
            error_count=0,
            warning_count=0,
        )
        assert result.token_reduction_percentage == 0.0
        assert result.degraded is False
        assert result.ranked_events == []

    def test_ranked_events_field(self) -> None:
        result = AnalyzePodLogsResult(
            pod_name="p",
            namespace="ns",
            time_window_minutes=30,
            strategy_used="smart_summary",
            total_lines=1,
            error_count=1,
            warning_count=0,
            ranked_events=[RankedEvent(line="Error: connection refused", count=1, severity="high")],
        )
        assert len(result.ranked_events) == 1
        assert result.ranked_events[0].severity == "high"
