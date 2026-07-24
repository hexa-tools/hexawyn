from dataclasses import asdict

from hexawyn.application.ports.driven.trace_log_correlation_port import TraceLogCorrelationPort
from hexawyn.application.use_case.trace_log_correlation.command import TraceLogCorrelationCommand
from hexawyn.application.use_case.trace_log_correlation.response import TraceLogCorrelationResponse


class TraceLogCorrelationUseCase:
    def __init__(self, port: TraceLogCorrelationPort) -> None:
        self._port = port

    def execute(self, c: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        results = self._port.correlate(trace_id=c.trace_id)
        return TraceLogCorrelationResponse(correlations=[asdict(r) for r in results])
