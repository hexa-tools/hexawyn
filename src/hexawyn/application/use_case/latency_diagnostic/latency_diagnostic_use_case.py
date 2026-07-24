from __future__ import annotations

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.application.use_case.latency_diagnostic.command import LatencyDiagnosticCommand
from hexawyn.application.use_case.latency_diagnostic.response import LatencyDiagnosticResponse
from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    LatencyDiagnosticResult,
)


class LatencyDiagnosticUseCase:
    def __init__(self, port: TraceQueryPort) -> None:
        self._port = port

    def execute(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        request = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        slow_spans = self._port.fetch_slow_spans(request)
        total_traces = self._port.fetch_total_traces(request)
        result = LatencyDiagnosticResult.compute(request, slow_spans, total_traces)

        bottlenecks: list[dict[str, object]] = [
            {
                "span_name": b.span_name,
                "occurrence_count": b.occurrence_count,
                "avg_duration_ms": b.avg_duration_ms,
            }
            for b in result.bottlenecks
        ]
        slowest: dict[str, object] | None = None
        if result.slowest_span:
            slowest = {
                "trace_id": result.slowest_span.trace_id,
                "span_name": result.slowest_span.span_name,
                "duration_ms": result.slowest_span.duration_ms,
            }

        return LatencyDiagnosticResponse(
            service_name=result.service_name,
            slow_trace_count=result.slow_trace_count,
            total_traces=result.total_traces,
            bottlenecks=bottlenecks,
            slowest_span=slowest,
        )
