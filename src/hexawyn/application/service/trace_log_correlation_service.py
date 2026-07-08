from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_log_correlation_port import TraceLogCorrelationPort
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_response import (
    TraceLogCorrelationResponse,
)
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_service_port import (
    TraceLogCorrelationServicePort,
)
from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest, TraceLogResult


class TraceLogCorrelationService(TraceLogCorrelationServicePort):
    def __init__(self, port: TraceLogCorrelationPort) -> None:
        self._port = port

    def correlate(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],
            correlated_logs=[asdict(c) for c in r.correlated_logs],
        )
