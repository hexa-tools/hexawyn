"""Unit tests for the log analysis domain models."""

import dataclasses

from hexawyn.domain.models.log import (
    DeduplicatedLine,
    LogAnalysisContext,
    LogAnalysisResult,
    PatternClassification,
    RankedEvent,
)


class TestLogAnalysisContext:
    def test_default_values(self) -> None:
        ctx = LogAnalysisContext()
        assert ctx.log_size_estimate == 0
        assert ctx.pod_name == ""
        assert ctx.namespace == "default"
        assert ctx.request_type == "troubleshooting"
        assert ctx.urgency == "low"
        assert ctx.time_sensitive is False
        assert ctx.follow_up_analysis is False
        assert ctx.observed_at == ""
        assert ctx.include_noise is False

    def test_critical_troubleshooting(self) -> None:
        ctx = LogAnalysisContext(
            log_size_estimate=80000,
            pod_name="payments-api-7d8f9",
            namespace="production",
            request_type="troubleshooting",
            urgency="critical",
            time_sensitive=True,
        )
        assert ctx.log_size_estimate == 80000
        assert ctx.urgency == "critical"
        assert ctx.time_sensitive is True

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(LogAnalysisContext)


class TestLogAnalysisResult:
    def test_defaults(self) -> None:
        result = LogAnalysisResult()
        assert result.summary == ""
        assert result.patterns == []
        assert result.recommendations == []
        assert result.severity == ""
        assert result.confidence == 0.0
        assert result.strategy_used == ""
        assert result.token_reduction_percentage == 0.0
        assert result.degraded is False
        assert result.ranked_events == []

    def test_full_result(self) -> None:
        result = LogAnalysisResult(
            summary="OOMKilled detected in 3 pods",
            patterns=["memory pressure", "CrashLoopBackOff"],
            recommendations=["Increase memory limit to 512Mi"],
            severity="critical",
            confidence=0.92,
            strategy_used="smart_summary",
        )
        assert len(result.patterns) == 2
        assert result.confidence == 0.92
        assert result.strategy_used == "smart_summary"

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(LogAnalysisResult)

    def test_hybrid_result_with_reduction_metrics(self) -> None:
        result = LogAnalysisResult(
            summary="Recurring connection refused pattern detected 45 times.",
            patterns=["connection refused"],
            strategy_used="hybrid",
            token_reduction_percentage=95.0,
            degraded=False,
        )
        assert result.token_reduction_percentage == 95.0
        assert result.degraded is False


class TestPatternClassification:
    def test_fields(self) -> None:
        classification = PatternClassification(
            pattern="connection refused",
            count=45,
            sample_line="upstream connect error: connection refused",
        )
        assert classification.pattern == "connection refused"
        assert classification.count == 45
        assert "refused" in classification.sample_line

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(PatternClassification)


class TestDeduplicatedLine:
    def test_fields(self) -> None:
        line = DeduplicatedLine(line="GET /health HTTP/1.1 200", count=1750)
        assert line.line == "GET /health HTTP/1.1 200"
        assert line.count == 1750

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(DeduplicatedLine)


class TestRankedEvent:
    def test_fields(self) -> None:
        event = RankedEvent(line="OOMKilled: memory limit exceeded", count=1, severity="critical")
        assert event.line == "OOMKilled: memory limit exceeded"
        assert event.count == 1
        assert event.severity == "critical"

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(RankedEvent)

    def test_frozen_prevents_mutation(self) -> None:
        event = RankedEvent(line="line", count=1, severity="low")
        with __import__("pytest").raises(dataclasses.FrozenInstanceError):
            event.count = 2  # type: ignore[misc]


class TestLogAnalysisResultEdgeCases:
    def test_confidence_boundary_zero(self) -> None:
        result = LogAnalysisResult(confidence=0.0)
        assert result.confidence == 0.0

    def test_confidence_boundary_one(self) -> None:
        result = LogAnalysisResult(confidence=1.0)
        assert result.confidence == 1.0

    def test_confidence_above_one_accepted(self) -> None:
        result = LogAnalysisResult(confidence=1.5)
        assert result.confidence == 1.5

    def test_confidence_negative_accepted(self) -> None:
        result = LogAnalysisResult(confidence=-0.5)
        assert result.confidence == -0.5

    def test_token_reduction_zero(self) -> None:
        result = LogAnalysisResult(token_reduction_percentage=0.0)
        assert result.token_reduction_percentage == 0.0

    def test_token_reduction_hundred(self) -> None:
        result = LogAnalysisResult(token_reduction_percentage=100.0)
        assert result.token_reduction_percentage == 100.0

    def test_token_reduction_above_hundred_accepted(self) -> None:
        result = LogAnalysisResult(token_reduction_percentage=150.0)
        assert result.token_reduction_percentage == 150.0

    def test_degraded_true(self) -> None:
        result = LogAnalysisResult(degraded=True, strategy_used="degraded_fallback")
        assert result.degraded is True

    def test_ranked_events_mutable_list(self) -> None:
        event = RankedEvent(line="err", count=1, severity="high")
        result = LogAnalysisResult(ranked_events=[event])
        assert len(result.ranked_events) == 1
        assert result.ranked_events[0].severity == "high"

    def test_empty_severity_accepted(self) -> None:
        result = LogAnalysisResult(severity="")
        assert result.severity == ""

    def test_empty_strategy_used_accepted(self) -> None:
        result = LogAnalysisResult(strategy_used="")
        assert result.strategy_used == ""


class TestLogAnalysisContextEdgeCases:
    def test_include_noise_true(self) -> None:
        ctx = LogAnalysisContext(include_noise=True)
        assert ctx.include_noise is True

    def test_follow_up_analysis_true(self) -> None:
        ctx = LogAnalysisContext(follow_up_analysis=True)
        assert ctx.follow_up_analysis is True

    def test_log_size_zero(self) -> None:
        ctx = LogAnalysisContext(log_size_estimate=0)
        assert ctx.log_size_estimate == 0

    def test_log_size_large(self) -> None:
        ctx = LogAnalysisContext(log_size_estimate=10_000_000)
        assert ctx.log_size_estimate == 10_000_000

    def test_observed_at_populated(self) -> None:
        ctx = LogAnalysisContext(observed_at="2026-07-17T12:00:00Z")
        assert ctx.observed_at == "2026-07-17T12:00:00Z"

    def test_all_fields_custom(self) -> None:
        ctx = LogAnalysisContext(
            log_size_estimate=50000,
            pod_name="api-7d8f9",
            namespace="staging",
            request_type="audit",
            urgency="high",
            time_sensitive=True,
            follow_up_analysis=True,
            observed_at="2026-07-17T08:00:00Z",
            include_noise=True,
        )
        assert ctx.log_size_estimate == 50000
        assert ctx.request_type == "audit"
        assert ctx.urgency == "high"
        assert ctx.include_noise is True


class TestDeduplicatedLineEdgeCases:
    def test_frozen_prevents_mutation(self) -> None:
        line = DeduplicatedLine(line="msg", count=1)
        with __import__("pytest").raises(dataclasses.FrozenInstanceError):
            line.count = 2  # type: ignore[misc]

    def test_count_zero_accepted(self) -> None:
        line = DeduplicatedLine(line="", count=0)
        assert line.count == 0


class TestPatternClassificationEdgeCases:
    def test_frozen_prevents_mutation(self) -> None:
        pc = PatternClassification(pattern="err", count=1, sample_line="line")
        with __import__("pytest").raises(dataclasses.FrozenInstanceError):
            pc.count = 2  # type: ignore[misc]

    def test_empty_pattern_accepted(self) -> None:
        pc = PatternClassification(pattern="", count=0, sample_line="")
        assert pc.pattern == ""
