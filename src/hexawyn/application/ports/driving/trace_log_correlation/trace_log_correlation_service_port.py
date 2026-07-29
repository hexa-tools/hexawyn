from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.trace_log_correlation.command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.use_case.observability.trace_log_correlation.response import (
    TraceLogCorrelationResponse,
)


class TraceLogCorrelationServicePort(ABC):
    @abstractmethod
    def correlate(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse: ...
