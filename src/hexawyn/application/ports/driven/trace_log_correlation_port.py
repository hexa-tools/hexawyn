from abc import ABC, abstractmethod

from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogCorrelationRequest,
    TraceLogSpan,
)


class TraceLogCorrelationPort(ABC):
    @abstractmethod
    def fetch_error_spans(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]: ...
    @abstractmethod
    def fetch_correlated_logs(self, trace_id: str) -> list[CorrelatedLog]: ...
