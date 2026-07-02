from hexawyn.domain.models.analyze_pod_logs import (
    AnalyzePodLogsRequest,
    AnalyzePodLogsResult,
    LogPatternMatch,
    PodLogLine,
    PodRunSummary,
)
from hexawyn.domain.models.log import LogAnalysisContext
from hexawyn.domain.services.log_analysis.patterns import categorize_connection_issues
from hexawyn.domain.services.log_analysis.volume_selector import select_strategy_by_volume

_NO_ANOMALIES_SUMMARY = "No anomalies detected"


def analyze_pod_logs(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = _summarize_runs(log_lines)
    restarts_detected = len(runs) > 1

    error_count = sum(1 for line in log_lines if line.is_error)
    warning_count = sum(1 for line in log_lines if line.is_warning)
    connection_timeouts, connection_refused = categorize_connection_issues(log_lines)
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            strategy_used=analysis.strategy_used,
            total_lines=total_lines,
            error_count=error_count,
            warning_count=warning_count,
            patterns=[],
            connection_timeouts=[],
            connection_refused=[],
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(pattern, messages),
            confidence=analysis.confidence,
        )
        for pattern in analysis.patterns
    ]

    return AnalyzePodLogsResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        strategy_used=analysis.strategy_used,
        total_lines=total_lines,
        error_count=error_count,
        warning_count=warning_count,
        patterns=patterns,
        connection_timeouts=connection_timeouts,
        connection_refused=connection_refused,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
    )


def _summarize_runs(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def _count_occurrences(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern in message.lower())
