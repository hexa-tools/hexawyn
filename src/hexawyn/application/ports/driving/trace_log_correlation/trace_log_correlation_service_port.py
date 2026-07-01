from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_response import (
    TraceLogCorrelationResponse,
)


class TraceLogCorrelationServicePort(ABC):
    @abstractmethod
    def correlate(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse: ...
