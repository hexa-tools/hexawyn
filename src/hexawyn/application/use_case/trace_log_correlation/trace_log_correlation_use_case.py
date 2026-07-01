from __future__ import annotations

from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_response import (
    TraceLogCorrelationResponse,
)
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_service_port import (
    TraceLogCorrelationServicePort,
)


class TraceLogCorrelationUseCase:
    def __init__(self, service: TraceLogCorrelationServicePort) -> None:
        self._svc = service

    def execute(self, cmd: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        return self._svc.correlate(cmd)
