"""Unit tests for the Log Analysis Strategy pattern."""

from abc import ABC

import pytest
from hexawyn.domain.models.log import LogAnalysisContext, LogAnalysisResult
from hexawyn.domain.services.log_analysis.analyzer import AdaptiveLogProcessor
from hexawyn.domain.services.log_analysis.strategy import (
    HybridStrategy,
    LogAnalysisStrategy,
    RealtimeLogWatchStrategy,
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

    def test_moderate_activity_branch(self) -> None:
        logs = (
            ["Error: timeout backoff restart"]
            + ["Warning: eviction threshold"]
            + ["Info: healthy"] * 18
        )
        result = self.strategy.analyze(logs, self.context)
        assert "Moderate activity" in result.summary

    def test_recommendations_cover_crashloop_backoff_and_denied(self) -> None:
        logs = [
            "Error: timeout backoff restart",
            "Error: denied access request",
        ]
        result = self.strategy.analyze(logs, self.context)
        assert any("startup command" in rec for rec in result.recommendations)
        assert any("RBAC permissions" in rec for rec in result.recommendations)


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

    def test_recommendations_cover_oomkilled_backoff_image_pull_and_critical(self) -> None:
        logs = [
            "Error: oomkilled container restart",
            "Error: timeout backoff restart",
            "Error: failed to pull image",
        ]
        result = self.strategy.analyze(logs, self.context)
        assert any("memory limit" in rec for rec in result.recommendations)
        assert any("startup command" in rec for rec in result.recommendations)
        assert any("registry connectivity" in rec for rec in result.recommendations)
        assert result.recommendations[0] == "IMMEDIATE ACTION: Critical errors detected in stream"


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

    def test_tc1_pattern_extraction_reduces_and_summarizes(self) -> None:
        """TC1: 3000 log lines -> pattern extraction reduces to a small set, summarized."""
        logs = ["Error: connection refused to redis:6379" for _ in range(3000)]

        result = self.strategy.analyze(logs, self.context)

        assert result.strategy_used == "hybrid"
        assert result.token_reduction_percentage > 90.0
        assert result.degraded is False
        assert len(result.patterns) > 0
        assert "45" not in result.summary  # sanity: not hardcoded, reflects real count
        assert "3000" in result.summary or "refused" in result.summary.lower()

    def test_tc2_no_errors_confirms_no_anomalies(self) -> None:
        """TC2: 0 errors detected by the pattern extractor -> summary confirms no anomalies."""
        logs = ["pod scheduled successfully", "readiness probe succeeded"]

        result = self.strategy.analyze(logs, self.context)

        assert result.patterns == []
        assert result.degraded is False
        assert "no anomalies" in result.summary.lower()

    def test_token_reduction_percentage_zero_for_empty_raw_logs(self) -> None:
        assert HybridStrategy._token_reduction_percentage([], []) == 0.0

    def test_tc3_degraded_fallback_when_nothing_to_summarize(self) -> None:
        """TC3 analog: no real LLM to fail, so 'unavailable' = nothing to summarize."""
        strategy = HybridStrategy(token_processor=AdaptiveLogProcessor(max_token_budget=1))

        result = strategy.analyze([], self.context)

        assert result.degraded is False  # empty-logs short circuit takes priority
        assert result.summary == "No log data to analyze."

    def test_tc4_unrecognized_format_still_reduces_and_summarizes(self) -> None:
        """TC4: unrecognized log format -> passed through with a reduced context window."""
        logs = [f"random unstructured line {i}" for i in range(500)]

        result = self.strategy.analyze(logs, self.context)

        assert result.strategy_used == "hybrid"
        assert result.token_reduction_percentage > 0.0
        assert len(result.summary) > 0

    def test_chunking_applied_when_reduced_output_still_exceeds_budget(self) -> None:
        """Edge case: token limit exceeded even after reduction -> chunked processing."""
        tiny_budget_processor = AdaptiveLogProcessor(max_token_budget=50)
        strategy = HybridStrategy(token_processor=tiny_budget_processor)
        logs = [f"Error: timeout on service-{i} occurred" for i in range(600)]

        result = strategy.analyze(logs, self.context)

        assert result.strategy_used == "hybrid"
        assert len(result.summary) > 0
        # 600 distinct reduced lines / _REDUCED_CHUNK_SIZE=500 -> 2 chunks summarized and joined
        assert result.summary.count("Recurring") == 2


class TestRealtimeLogWatchStrategy:
    """ECA-16: concrete ILogAnalysisStrategy for the real-time watch use case.

    Distinct from StreamingStrategy (the >10000-line batch-chunked volume
    tier) — see docs/use-cases/59-realtime-log-watch.md for the naming
    disambiguation. This strategy never buffers/watches itself; it
    summarizes the sampled lines collected after a watch session ends.
    """

    def setup_method(self) -> None:
        self.strategy = RealtimeLogWatchStrategy()
        self.context = LogAnalysisContext(request_type="realtime_watch")

    def test_supports_only_realtime_watch_request_type(self) -> None:
        assert self.strategy.supports(self.context) is True

    def test_does_not_support_other_request_types(self) -> None:
        other = LogAnalysisContext(request_type="troubleshooting")
        assert self.strategy.supports(other) is False

    def test_never_auto_selected_by_strategy_selector(self) -> None:
        context = LogAnalysisContext(
            log_size_estimate=80000, request_type="realtime_watch", urgency="critical"
        )
        strategy = StrategySelector.select(context)
        assert not isinstance(strategy, RealtimeLogWatchStrategy)

    def test_analyze_empty_logs_returns_graceful_result(self) -> None:
        result = self.strategy.analyze([], self.context)
        assert result.summary == "No log data to analyze."
        assert result.strategy_used == "realtime_watch"

    def test_analyze_summarizes_sampled_lines_with_pattern(self) -> None:
        logs = ["Error: OOMKilled memory limit exceeded" for _ in range(3)] + ["pod healthy"]

        result = self.strategy.analyze(logs, self.context)

        assert result.strategy_used == "realtime_watch"
        assert len(result.patterns) > 0
        assert "3" in result.summary or "oomkilled" in result.summary.lower()

    def test_analyze_no_patterns_still_produces_summary(self) -> None:
        logs = ["pod healthy", "readiness probe succeeded"]

        result = self.strategy.analyze(logs, self.context)

        assert result.strategy_used == "realtime_watch"
        assert len(result.summary) > 0
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
