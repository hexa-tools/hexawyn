from __future__ import annotations

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    AnalyzePodLogsResponse,
    ConnectionIssueDict,
    LogPatternDict,
    PodRunSummaryDict,
    RankedEventDict,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_service_port import (
    AnalyzePodLogsServicePort,
)
from hexawyn.domain.models.analyze_pod_logs import (
    AnalyzePodLogsRequest,
    AnalyzePodLogsResult,
    ConnectionIssue,
)
from hexawyn.domain.services.log_analysis.pod_log_analyzer import analyze_pod_logs


class AnalyzePodLogsService(AnalyzePodLogsServicePort):
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port

    def analyze(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)


def _to_response(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,
        token_reduction_percentage=result.token_reduction_percentage,
        degraded=result.degraded,
        patterns=[
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],
        runs=[
            PodRunSummaryDict(
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)
            for e in result.ranked_events
        ],
    )


def _to_connection_issue_dict(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )
