from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)
from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogCorrelationRequest,
    TraceLogSpan,
)


class OTelTraceLogAdapter(TraceLogCorrelationPort):
    def fetch_error_spans(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result

    def fetch_correlated_logs(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="log data not available without log backend",
            )
        ]
