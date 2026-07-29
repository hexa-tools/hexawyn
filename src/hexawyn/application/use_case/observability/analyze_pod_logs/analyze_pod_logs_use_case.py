from __future__ import annotations

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.use_case.observability.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.response import (
    AnalyzePodLogsResponse,
    ConnectionIssueDict,
    LogPatternDict,
    PodRunSummaryDict,
    RankedEventDict,
)
from hexawyn.domain.models.analyze_pod_logs import (
    AnalyzePodLogsRequest,
    AnalyzePodLogsResult,
    ConnectionIssue,
)
from hexawyn.domain.services.log_analysis.pod_log_analyzer import analyze_pod_logs


class AnalyzePodLogsUseCase:
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port

    def execute(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
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
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def _to_connection_issue_dict(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )
