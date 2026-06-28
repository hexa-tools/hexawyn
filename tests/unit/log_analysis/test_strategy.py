"""Unit tests for the Log Analysis Strategy pattern."""

from abc import ABC

import pytest
from hexawyn.domain.models.log import LogAnalysisContext, LogAnalysisResult
from hexawyn.domain.services.log_analysis.strategy import (
    HybridStrategy,
    LogAnalysisStrategy,
    SmartSummaryStrategy,
    StrategySelector,
    StreamingStrategy,
)


class TestLogAnalysisStrategyABC:
    def test_cannot_instantiate_abc(self) -> None:
        with pytest.raises(TypeError):
            LogAnalysisStrategy()  # type: ignore[abstract]

    def test_is_abc(self) -> None:
        assert issubclass(LogAnalysisStrategy, ABC)


class TestSmartSummaryStrategy:
    def setup_method(self) -> None:
        self.strategy = SmartSummaryStrategy()
        self.context = LogAnalysisContext(
            log_size_estimate=80000,
            pod_name="api-pod",
            namespace="prod",
            request_type="monitoring",
            urgency="medium",
        )

    def test_supports_large_logs(self) -> None:
        assert self.strategy.supports(self.context) is True

    def test_does_not_support_small_logs(self) -> None:
        small_ctx = LogAnalysisContext(log_size_estimate=2000)
        assert self.strategy.supports(small_ctx) is False

    def test_does_not_support_critical_with_time_sensitivity(self) -> None:
        critical_ctx = LogAnalysisContext(
            log_size_estimate=80000, urgency="critical", time_sensitive=True
        )
        assert self.strategy.supports(critical_ctx) is False

    def test_analyze_returns_result_with_summary(self) -> None:
        logs = [
            "Error: OOMKilled container api",
            "Warning: Memory pressure on node-1",
            "Error: OOMKilled container worker",
            "Info: Pod scheduled successfully",
        ]
        result = self.strategy.analyze(logs, self.context)
        assert isinstance(result, LogAnalysisResult)
        assert result.strategy_used == "smart_summary"
        assert len(result.patterns) > 0
        assert len(result.recommendations) > 0
        assert result.confidence >= 0.0

    def test_analyze_empty_logs_returns_graceful_result(self) -> None:
        result = self.strategy.analyze([], self.context)
        assert result.summary == "No log data to analyze."
        assert result.patterns == []
        assert result.confidence == 0.0


class TestStreamingStrategy:
    def setup_method(self) -> None:
        self.strategy = StreamingStrategy()
        self.context = LogAnalysisContext(
            log_size_estimate=12000,
            pod_name="api-pod",
            namespace="prod",
            request_type="troubleshooting",
            urgency="critical",
            time_sensitive=True,
        )

    def test_supports_critical_and_time_sensitive(self) -> None:
        assert self.strategy.supports(self.context) is True

    def test_supports_large_troubleshooting(self) -> None:
        ctx = LogAnalysisContext(log_size_estimate=25000, request_type="troubleshooting")
        assert self.strategy.supports(ctx) is True

    def test_does_not_support_small_monitoring(self) -> None:
        ctx = LogAnalysisContext(log_size_estimate=3000, request_type="monitoring")
        assert self.strategy.supports(ctx) is False

    def test_analyze_returns_chunked_result(self) -> None:
        logs = [
            "Error: CrashLoopBackOff container worker",
            "Warning: Failed to pull image",
            "Error: CrashLoopBackOff container worker",
            "Info: Image pulled successfully",
            "Error: CrashLoopBackOff container worker",
            "Warning: Back-off restarting failed container",
        ]
        result = self.strategy.analyze(logs, self.context)
        assert isinstance(result, LogAnalysisResult)
        assert result.strategy_used == "streaming"
        assert result.confidence >= 0.0

    def test_analyze_empty_logs_returns_graceful_result(self) -> None:
        result = self.strategy.analyze([], self.context)
        assert result.summary == "No log data to analyze."
        assert result.patterns == []


class TestHybridStrategy:
    def setup_method(self) -> None:
        self.strategy = HybridStrategy()
        self.context = LogAnalysisContext(
            log_size_estimate=60000,
            pod_name="api-pod",
            namespace="prod",
            request_type="investigation",
            urgency="high",
            follow_up_analysis=True,
        )

    def test_supports_investigation_with_large_logs(self) -> None:
        assert self.strategy.supports(self.context) is True

    def test_supports_follow_up_with_large_logs(self) -> None:
        ctx = LogAnalysisContext(
            log_size_estimate=30000,
            request_type="troubleshooting",
            follow_up_analysis=True,
        )
        assert self.strategy.supports(ctx) is True

    def test_does_not_support_small_simple(self) -> None:
        ctx = LogAnalysisContext(log_size_estimate=1000)
        assert self.strategy.supports(ctx) is False

    def test_analyze_combines_summary_and_streaming(self) -> None:
        logs = [
            "Error: OOMKilled container api",
            "Error: OOMKilled container worker",
            "Warning: Memory pressure on node-1",
            "Info: Pod scheduled successfully",
            "Warning: Eviction threshold reached",
        ]
        result = self.strategy.analyze(logs, self.context)
        assert isinstance(result, LogAnalysisResult)
        assert result.strategy_used == "hybrid"
        assert len(result.summary) > 0

    def test_analyze_empty_logs_returns_graceful_result(self) -> None:
        result = self.strategy.analyze([], self.context)
        assert result.summary == "No log data to analyze."
        assert result.patterns == []


class TestStrategySelector:
    def test_selects_smart_summary_for_large_monitoring(self) -> None:
        context = LogAnalysisContext(
            log_size_estimate=80000,
            request_type="monitoring",
            urgency="low",
        )
        strategy = StrategySelector.select(context)
        assert isinstance(strategy, SmartSummaryStrategy)

    def test_selects_streaming_for_critical_time_sensitive(self) -> None:
        context = LogAnalysisContext(
            log_size_estimate=10000,
            request_type="troubleshooting",
            urgency="critical",
            time_sensitive=True,
        )
        strategy = StrategySelector.select(context)
        assert isinstance(strategy, StreamingStrategy)

    def test_selects_hybrid_for_investigation(self) -> None:
        context = LogAnalysisContext(
            log_size_estimate=50000,
            request_type="investigation",
            urgency="high",
        )
        strategy = StrategySelector.select(context)
        assert isinstance(strategy, HybridStrategy)

    def test_defaults_to_smart_summary(self) -> None:
        context = LogAnalysisContext(log_size_estimate=2000)
        strategy = StrategySelector.select(context)
        assert isinstance(strategy, SmartSummaryStrategy)

    def test_select_is_class_method(self) -> None:
        assert callable(StrategySelector.select)
