from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.application.use_case.latency_diagnostic.command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.use_case.latency_diagnostic.response import (
    LatencyDiagnosticResponse,
)
from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_service_port import (
    LatencyDiagnosticServicePort,
)
from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    LatencyDiagnosticResult,
)


class LatencyDiagnosticService(LatencyDiagnosticServicePort):
    def __init__(self, port: TraceQueryPort) -> None:
        self._port = port

    def diagnose(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )
