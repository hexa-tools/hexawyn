"""Unit tests for the pod_log_analyzer domain service (Strategy pattern entry point)."""

from __future__ import annotations

from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine
from hexawyn.domain.services.log_analysis.pod_log_analyzer import analyze_pod_logs


def _line(message: str, level: str = "INFO", run_index: int = 0) -> PodLogLine:
    return PodLogLine(
        timestamp="T1", level=level, message=message, run_index=run_index, is_json=False
    )


class TestAnalyzePodLogsSmartStrategy:
    """TC1: 500 lines, 3 recurring 'connection refused' errors → SMART strategy."""

    def test_selects_smart_strategy_under_1000_lines(self) -> None:
        lines = [_line("pod healthy", level="INFO") for _ in range(497)]
        lines += [_line("connection refused", level="ERROR") for _ in range(3)]
        request = AnalyzePodLogsRequest(pod_name="api-gateway-7f9b", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.strategy_used == "smart_summary"
        assert result.total_lines == 500
        assert result.error_count == 3
        assert len(result.connection_refused) == 1
        assert result.connection_refused[0].count == 3


class TestAnalyzePodLogsStreamingStrategy:
    """TC2: 15000 lines → STREAMING strategy auto-selected, analysis streamed."""

    def test_selects_streaming_strategy_above_10000_lines(self) -> None:
        lines = [_line("connection timeout to postgres:5432", level="ERROR") for _ in range(15000)]
        request = AnalyzePodLogsRequest(pod_name="worker-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.strategy_used == "streaming"
        assert result.total_lines == 15000
        assert len(result.connection_timeouts) == 1
        assert result.connection_timeouts[0].count == 15000


class TestAnalyzePodLogsHybridStrategy:
    def test_selects_hybrid_strategy_in_mid_range(self) -> None:
        lines = [_line("Error: OOMKilled container api") for _ in range(5000)]
        request = AnalyzePodLogsRequest(pod_name="mid-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.strategy_used == "hybrid"

    def test_hybrid_strategy_propagates_token_reduction_metrics(self) -> None:
        """ECA-15: pattern extraction + summarization metrics reach AnalyzePodLogsResult."""
        lines = [
            _line("Error: connection refused to redis:6379", level="ERROR") for _ in range(5000)
        ]
        request = AnalyzePodLogsRequest(pod_name="mid-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.strategy_used == "hybrid"
        assert result.token_reduction_percentage > 90.0
        assert result.degraded is False
        assert result.total_lines == 5000


class TestAnalyzePodLogsNoAnomalies:
    """TC3: pod with no errors in the window → 'no anomalies detected' report."""

    def test_no_errors_returns_no_anomalies_report(self) -> None:
        lines = [_line("pod scheduled successfully"), _line("readiness probe succeeded")]
        request = AnalyzePodLogsRequest(pod_name="quiet-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.summary == "No anomalies detected"
        assert result.patterns == []
        assert result.error_count == 0
        assert result.warning_count == 0
        assert result.confidence == 0.0

    def test_empty_logs_returns_no_anomalies_report(self) -> None:
        request = AnalyzePodLogsRequest(pod_name="new-pod", namespace="prod")

        result = analyze_pod_logs(request, [])

        assert result.summary == "No anomalies detected"
        assert result.total_lines == 0
        assert result.runs == []
        assert result.restarts_detected is False


class TestAnalyzePodLogsRestartSplit:
    """Edge case: pod restarted mid-window — logs from both runs analyzed separately."""

    def test_detects_restart_and_splits_runs(self) -> None:
        lines = [_line("Error: OOMKilled", level="ERROR", run_index=1) for _ in range(3)]
        lines += [_line("pod started", level="INFO", run_index=0) for _ in range(2)]
        request = AnalyzePodLogsRequest(pod_name="flaky-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.restarts_detected is True
        assert len(result.runs) == 2
        run_by_index = {run.run_index: run for run in result.runs}
        assert run_by_index[1].error_count == 3
        assert run_by_index[0].line_count == 2

    def test_single_run_does_not_flag_restart(self) -> None:
        lines = [_line("ok", run_index=0) for _ in range(10)]
        request = AnalyzePodLogsRequest(pod_name="stable-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.restarts_detected is False
        assert len(result.runs) == 1


class TestAnalyzePodLogsSanitization:
    def test_flags_sanitized_binary_content(self) -> None:
        lines = [_line("Error: �� corrupted frame", level="ERROR")]
        request = AnalyzePodLogsRequest(pod_name="binary-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.sanitized_binary is True

    def test_no_flag_for_clean_content(self) -> None:
        lines = [_line("Error: clean message", level="ERROR")]
        request = AnalyzePodLogsRequest(pod_name="clean-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert result.sanitized_binary is False


class TestAnalyzePodLogsPatternConfidence:
    def test_each_pattern_has_a_confidence_score(self) -> None:
        lines = [_line("Error: OOMKilled container api", level="ERROR") for _ in range(5)]
        request = AnalyzePodLogsRequest(pod_name="oom-pod", namespace="prod")

        result = analyze_pod_logs(request, lines)

        assert len(result.patterns) > 0
        for pattern in result.patterns:
            assert 0.0 <= pattern.confidence <= 1.0
            assert pattern.count > 0
