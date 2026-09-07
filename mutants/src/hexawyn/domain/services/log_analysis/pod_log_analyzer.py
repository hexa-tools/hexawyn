from datetime import UTC, datetime

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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_pod_logs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_pod_logs__mutmut)
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_orig(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_1(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = None
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_2(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = None
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_3(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = _summarize_runs(None)
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_4(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = _summarize_runs(log_lines)
    restarts_detected = None

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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_5(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = _summarize_runs(log_lines)
    restarts_detected = len(runs) >= 1

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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_6(
    request: AnalyzePodLogsRequest, log_lines: list[PodLogLine]
) -> AnalyzePodLogsResult:
    """Domain service — entry point for the log-analysis Strategy pattern.

    Depends on LogAnalysisStrategy (the ILogAnalysisStrategy port) only,
    never on a concrete strategy class, except inside
    select_strategy_by_volume (the one Factory-role instantiation point).
    """
    total_lines = len(log_lines)
    runs = _summarize_runs(log_lines)
    restarts_detected = len(runs) > 2

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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_7(
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

    error_count = None
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_8(
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

    error_count = sum(None)
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_9(
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

    error_count = sum(2 for line in log_lines if line.is_error)
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_10(
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
    warning_count = None
    connection_timeouts, connection_refused = categorize_connection_issues(log_lines)
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_11(
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
    warning_count = sum(None)
    connection_timeouts, connection_refused = categorize_connection_issues(log_lines)
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_12(
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
    warning_count = sum(2 for line in log_lines if line.is_warning)
    connection_timeouts, connection_refused = categorize_connection_issues(log_lines)
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_13(
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
    connection_timeouts, connection_refused = None
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_14(
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
    connection_timeouts, connection_refused = categorize_connection_issues(None)
    sanitized_binary = any("�" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_15(
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
    sanitized_binary = None

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_16(
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
    sanitized_binary = any(None)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_17(
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
    sanitized_binary = any("XX�XX" in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_18(
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
    sanitized_binary = any("�" not in line.message for line in log_lines)

    strategy = select_strategy_by_volume(total_lines)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_19(
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

    strategy = None
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_20(
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

    strategy = select_strategy_by_volume(None)
    context = LogAnalysisContext(
        log_size_estimate=total_lines,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_21(
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
    context = None
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_22(
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
        log_size_estimate=None,
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_23(
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
        pod_name=None,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_24(
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
        namespace=None,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_25(
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
        request_type=None,
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_26(
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
        urgency=None,
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_27(
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
        observed_at=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_28(
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
        pod_name=request.pod_name,
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_29(
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
        namespace=request.namespace,
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_30(
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
        request_type="troubleshooting",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_31(
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
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_32(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_33(
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_34(
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
        request_type="XXtroubleshootingXX",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_35(
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
        request_type="TROUBLESHOOTING",
        urgency="medium",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_36(
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
        urgency="XXmediumXX",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_37(
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
        urgency="MEDIUM",
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_38(
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
        observed_at=datetime.now(None).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_39(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = None
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_40(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = None

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_41(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(None, context)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_42(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, None)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_43(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(context)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_44(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, )

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_45(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = None

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_46(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(None)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_47(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts and connection_refused)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_48(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count and connection_timeouts or connection_refused)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_49(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count and warning_count or connection_timeouts or connection_refused)

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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_50(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if has_anomalies:
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_51(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_52(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_53(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_54(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            strategy_used=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_55(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            total_lines=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_56(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            error_count=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_57(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            warning_count=None,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_58(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            patterns=None,
            connection_timeouts=[],
            connection_refused=[],
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_59(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            connection_timeouts=None,
            connection_refused=[],
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_60(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            connection_refused=None,
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_61(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            confidence=None,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_62(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            summary=None,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_63(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            restarts_detected=None,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_64(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            runs=None,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_65(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            sanitized_binary=None,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_66(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            token_reduction_percentage=None,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_67(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            degraded=None,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_68(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_69(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_70(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_71(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_72(
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
        observed_at=datetime.now(UTC).isoformat(),
    )
    messages = [line.message for line in log_lines]
    analysis = strategy.analyze(messages, context)

    has_anomalies = bool(error_count or warning_count or connection_timeouts or connection_refused)

    if not has_anomalies:
        return AnalyzePodLogsResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_73(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_74(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_75(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_76(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            connection_timeouts=[],
            connection_refused=[],
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_77(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            connection_refused=[],
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_78(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            confidence=0.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_79(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_80(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_81(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_82(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_83(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_84(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_85(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_86(
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
        observed_at=datetime.now(UTC).isoformat(),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_87(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            confidence=1.0,
            summary=_NO_ANOMALIES_SUMMARY,
            restarts_detected=restarts_detected,
            runs=runs,
            sanitized_binary=sanitized_binary,
            token_reduction_percentage=analysis.token_reduction_percentage,
            degraded=analysis.degraded,
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_88(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = None

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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_89(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_90(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_91(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(pattern, messages),
            confidence=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_92(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_93(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_94(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(pattern, messages),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_95(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(None, messages),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_96(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(pattern, None),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_97(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(messages),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_98(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
        )

    patterns = [
        LogPatternMatch(
            pattern=pattern,
            count=_count_occurrences(pattern, ),
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_99(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        pod_name=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_100(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        namespace=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_101(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        time_window_minutes=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_102(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        strategy_used=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_103(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        total_lines=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_104(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        error_count=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_105(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        warning_count=None,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_106(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        patterns=None,
        connection_timeouts=connection_timeouts,
        connection_refused=connection_refused,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_107(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        connection_timeouts=None,
        connection_refused=connection_refused,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_108(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        connection_refused=None,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_109(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        confidence=None,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_110(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        summary=None,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_111(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        restarts_detected=None,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_112(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        runs=None,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_113(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        sanitized_binary=None,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_114(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        token_reduction_percentage=None,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_115(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        degraded=None,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_116(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=None,
    )


def x_analyze_pod_logs__mutmut_117(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_118(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_119(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_120(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_121(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_122(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_123(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_124(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        connection_timeouts=connection_timeouts,
        connection_refused=connection_refused,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_125(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        connection_refused=connection_refused,
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_126(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        confidence=analysis.confidence,
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_127(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        summary=analysis.summary,
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_128(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        restarts_detected=restarts_detected,
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_129(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        runs=runs,
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_130(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        sanitized_binary=sanitized_binary,
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_131(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        token_reduction_percentage=analysis.token_reduction_percentage,
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_132(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        degraded=analysis.degraded,
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_133(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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
        ranked_events=analysis.ranked_events,
    )


def x_analyze_pod_logs__mutmut_134(
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
        observed_at=datetime.now(UTC).isoformat(),
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
            ranked_events=analysis.ranked_events,
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

mutants_x_analyze_pod_logs__mutmut['_mutmut_orig'] = x_analyze_pod_logs__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_1'] = x_analyze_pod_logs__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_2'] = x_analyze_pod_logs__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_3'] = x_analyze_pod_logs__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_4'] = x_analyze_pod_logs__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_5'] = x_analyze_pod_logs__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_6'] = x_analyze_pod_logs__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_7'] = x_analyze_pod_logs__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_8'] = x_analyze_pod_logs__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_9'] = x_analyze_pod_logs__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_10'] = x_analyze_pod_logs__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_11'] = x_analyze_pod_logs__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_12'] = x_analyze_pod_logs__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_13'] = x_analyze_pod_logs__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_14'] = x_analyze_pod_logs__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_15'] = x_analyze_pod_logs__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_16'] = x_analyze_pod_logs__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_17'] = x_analyze_pod_logs__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_18'] = x_analyze_pod_logs__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_19'] = x_analyze_pod_logs__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_20'] = x_analyze_pod_logs__mutmut_20 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_21'] = x_analyze_pod_logs__mutmut_21 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_22'] = x_analyze_pod_logs__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_23'] = x_analyze_pod_logs__mutmut_23 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_24'] = x_analyze_pod_logs__mutmut_24 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_25'] = x_analyze_pod_logs__mutmut_25 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_26'] = x_analyze_pod_logs__mutmut_26 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_27'] = x_analyze_pod_logs__mutmut_27 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_28'] = x_analyze_pod_logs__mutmut_28 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_29'] = x_analyze_pod_logs__mutmut_29 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_30'] = x_analyze_pod_logs__mutmut_30 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_31'] = x_analyze_pod_logs__mutmut_31 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_32'] = x_analyze_pod_logs__mutmut_32 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_33'] = x_analyze_pod_logs__mutmut_33 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_34'] = x_analyze_pod_logs__mutmut_34 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_35'] = x_analyze_pod_logs__mutmut_35 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_36'] = x_analyze_pod_logs__mutmut_36 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_37'] = x_analyze_pod_logs__mutmut_37 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_38'] = x_analyze_pod_logs__mutmut_38 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_39'] = x_analyze_pod_logs__mutmut_39 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_40'] = x_analyze_pod_logs__mutmut_40 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_41'] = x_analyze_pod_logs__mutmut_41 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_42'] = x_analyze_pod_logs__mutmut_42 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_43'] = x_analyze_pod_logs__mutmut_43 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_44'] = x_analyze_pod_logs__mutmut_44 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_45'] = x_analyze_pod_logs__mutmut_45 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_46'] = x_analyze_pod_logs__mutmut_46 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_47'] = x_analyze_pod_logs__mutmut_47 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_48'] = x_analyze_pod_logs__mutmut_48 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_49'] = x_analyze_pod_logs__mutmut_49 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_50'] = x_analyze_pod_logs__mutmut_50 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_51'] = x_analyze_pod_logs__mutmut_51 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_52'] = x_analyze_pod_logs__mutmut_52 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_53'] = x_analyze_pod_logs__mutmut_53 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_54'] = x_analyze_pod_logs__mutmut_54 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_55'] = x_analyze_pod_logs__mutmut_55 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_56'] = x_analyze_pod_logs__mutmut_56 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_57'] = x_analyze_pod_logs__mutmut_57 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_58'] = x_analyze_pod_logs__mutmut_58 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_59'] = x_analyze_pod_logs__mutmut_59 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_60'] = x_analyze_pod_logs__mutmut_60 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_61'] = x_analyze_pod_logs__mutmut_61 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_62'] = x_analyze_pod_logs__mutmut_62 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_63'] = x_analyze_pod_logs__mutmut_63 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_64'] = x_analyze_pod_logs__mutmut_64 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_65'] = x_analyze_pod_logs__mutmut_65 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_66'] = x_analyze_pod_logs__mutmut_66 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_67'] = x_analyze_pod_logs__mutmut_67 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_68'] = x_analyze_pod_logs__mutmut_68 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_69'] = x_analyze_pod_logs__mutmut_69 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_70'] = x_analyze_pod_logs__mutmut_70 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_71'] = x_analyze_pod_logs__mutmut_71 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_72'] = x_analyze_pod_logs__mutmut_72 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_73'] = x_analyze_pod_logs__mutmut_73 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_74'] = x_analyze_pod_logs__mutmut_74 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_75'] = x_analyze_pod_logs__mutmut_75 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_76'] = x_analyze_pod_logs__mutmut_76 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_77'] = x_analyze_pod_logs__mutmut_77 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_78'] = x_analyze_pod_logs__mutmut_78 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_79'] = x_analyze_pod_logs__mutmut_79 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_80'] = x_analyze_pod_logs__mutmut_80 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_81'] = x_analyze_pod_logs__mutmut_81 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_82'] = x_analyze_pod_logs__mutmut_82 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_83'] = x_analyze_pod_logs__mutmut_83 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_84'] = x_analyze_pod_logs__mutmut_84 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_85'] = x_analyze_pod_logs__mutmut_85 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_86'] = x_analyze_pod_logs__mutmut_86 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_87'] = x_analyze_pod_logs__mutmut_87 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_88'] = x_analyze_pod_logs__mutmut_88 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_89'] = x_analyze_pod_logs__mutmut_89 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_90'] = x_analyze_pod_logs__mutmut_90 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_91'] = x_analyze_pod_logs__mutmut_91 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_92'] = x_analyze_pod_logs__mutmut_92 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_93'] = x_analyze_pod_logs__mutmut_93 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_94'] = x_analyze_pod_logs__mutmut_94 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_95'] = x_analyze_pod_logs__mutmut_95 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_96'] = x_analyze_pod_logs__mutmut_96 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_97'] = x_analyze_pod_logs__mutmut_97 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_98'] = x_analyze_pod_logs__mutmut_98 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_99'] = x_analyze_pod_logs__mutmut_99 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_100'] = x_analyze_pod_logs__mutmut_100 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_101'] = x_analyze_pod_logs__mutmut_101 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_102'] = x_analyze_pod_logs__mutmut_102 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_103'] = x_analyze_pod_logs__mutmut_103 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_104'] = x_analyze_pod_logs__mutmut_104 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_105'] = x_analyze_pod_logs__mutmut_105 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_106'] = x_analyze_pod_logs__mutmut_106 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_107'] = x_analyze_pod_logs__mutmut_107 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_108'] = x_analyze_pod_logs__mutmut_108 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_109'] = x_analyze_pod_logs__mutmut_109 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_110'] = x_analyze_pod_logs__mutmut_110 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_111'] = x_analyze_pod_logs__mutmut_111 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_112'] = x_analyze_pod_logs__mutmut_112 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_113'] = x_analyze_pod_logs__mutmut_113 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_114'] = x_analyze_pod_logs__mutmut_114 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_115'] = x_analyze_pod_logs__mutmut_115 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_116'] = x_analyze_pod_logs__mutmut_116 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_117'] = x_analyze_pod_logs__mutmut_117 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_118'] = x_analyze_pod_logs__mutmut_118 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_119'] = x_analyze_pod_logs__mutmut_119 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_120'] = x_analyze_pod_logs__mutmut_120 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_121'] = x_analyze_pod_logs__mutmut_121 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_122'] = x_analyze_pod_logs__mutmut_122 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_123'] = x_analyze_pod_logs__mutmut_123 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_124'] = x_analyze_pod_logs__mutmut_124 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_125'] = x_analyze_pod_logs__mutmut_125 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_126'] = x_analyze_pod_logs__mutmut_126 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_127'] = x_analyze_pod_logs__mutmut_127 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_128'] = x_analyze_pod_logs__mutmut_128 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_129'] = x_analyze_pod_logs__mutmut_129 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_130'] = x_analyze_pod_logs__mutmut_130 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_131'] = x_analyze_pod_logs__mutmut_131 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_132'] = x_analyze_pod_logs__mutmut_132 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_133'] = x_analyze_pod_logs__mutmut_133 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_134'] = x_analyze_pod_logs__mutmut_134 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summarize_runs__mutmut)
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


def x__summarize_runs__mutmut_orig(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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


def x__summarize_runs__mutmut_1(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if log_lines:
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


def x__summarize_runs__mutmut_2(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = None
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


def x__summarize_runs__mutmut_3(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(None)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_4(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(None, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_5(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, None).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_6(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault([]).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_7(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, ).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_8(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=None,
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_9(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=None,
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_10(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=None,
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_11(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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
            warning_count=None,
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_12(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            line_count=len(lines),
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_13(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            error_count=sum(1 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_14(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_15(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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
            )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_16(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(None),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_17(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
    if not log_lines:
        return []
    by_run: dict[int, list[PodLogLine]] = {}
    for line in log_lines:
        by_run.setdefault(line.run_index, []).append(line)
    return [
        PodRunSummary(
            run_index=run_index,
            line_count=len(lines),
            error_count=sum(2 for line in lines if line.is_error),
            warning_count=sum(1 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_18(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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
            warning_count=sum(None),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_19(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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
            warning_count=sum(2 for line in lines if line.is_warning),
        )
        for run_index, lines in sorted(by_run.items())
    ]


def x__summarize_runs__mutmut_20(log_lines: list[PodLogLine]) -> list[PodRunSummary]:
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
        for run_index, lines in sorted(None)
    ]

mutants_x__summarize_runs__mutmut['_mutmut_orig'] = x__summarize_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_1'] = x__summarize_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_2'] = x__summarize_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_3'] = x__summarize_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_4'] = x__summarize_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_5'] = x__summarize_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_6'] = x__summarize_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_7'] = x__summarize_runs__mutmut_7 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_8'] = x__summarize_runs__mutmut_8 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_9'] = x__summarize_runs__mutmut_9 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_10'] = x__summarize_runs__mutmut_10 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_11'] = x__summarize_runs__mutmut_11 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_12'] = x__summarize_runs__mutmut_12 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_13'] = x__summarize_runs__mutmut_13 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_14'] = x__summarize_runs__mutmut_14 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_15'] = x__summarize_runs__mutmut_15 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_16'] = x__summarize_runs__mutmut_16 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_17'] = x__summarize_runs__mutmut_17 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_18'] = x__summarize_runs__mutmut_18 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_19'] = x__summarize_runs__mutmut_19 # type: ignore # mutmut generated
mutants_x__summarize_runs__mutmut['x__summarize_runs__mutmut_20'] = x__summarize_runs__mutmut_20 # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__count_occurrences__mutmut)
def _count_occurrences(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern.lower() in message.lower())


def x__count_occurrences__mutmut_orig(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern.lower() in message.lower())


def x__count_occurrences__mutmut_1(pattern: str, messages: list[str]) -> int:
    return sum(None)


def x__count_occurrences__mutmut_2(pattern: str, messages: list[str]) -> int:
    return sum(2 for message in messages if pattern.lower() in message.lower())


def x__count_occurrences__mutmut_3(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern.upper() in message.lower())


def x__count_occurrences__mutmut_4(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern.lower() not in message.lower())


def x__count_occurrences__mutmut_5(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern.lower() in message.upper())

mutants_x__count_occurrences__mutmut['_mutmut_orig'] = x__count_occurrences__mutmut_orig # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut['x__count_occurrences__mutmut_1'] = x__count_occurrences__mutmut_1 # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut['x__count_occurrences__mutmut_2'] = x__count_occurrences__mutmut_2 # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut['x__count_occurrences__mutmut_3'] = x__count_occurrences__mutmut_3 # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut['x__count_occurrences__mutmut_4'] = x__count_occurrences__mutmut_4 # type: ignore # mutmut generated
mutants_x__count_occurrences__mutmut['x__count_occurrences__mutmut_5'] = x__count_occurrences__mutmut_5 # type: ignore # mutmut generated
