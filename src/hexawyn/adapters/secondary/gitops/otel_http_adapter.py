from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    TraceSpan,
)


class OTelHTTPAdapter(TraceQueryPort):
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(  # type: ignore
                    span_id=trace["traceID"][:16],
                    operation=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    status="error" if trace.get("hasErrors") else "ok",
                )
            ]
            result.append(spans)
        return result

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=100,
        )
        return len(traces)
