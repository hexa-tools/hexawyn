"""Unit tests for the log analysis domain models."""

import dataclasses

from hexawyn.domain.models.log import LogAnalysisContext, LogAnalysisResult


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
