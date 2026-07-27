from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowTrace


class OTelPodTraceAdapter(SlowTraceSearchPort):
    def search_pod_traces(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(  # type: ignore
                    trace_id=trace["traceID"],
                    service="",
                    operation="",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    has_errors=bool(trace.get("hasErrors")),
                )
            )
        return result
