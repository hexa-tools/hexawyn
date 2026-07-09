from abc import ABC, abstractmethod

from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest, TraceSpan

__all__ = ["LatencyDiagnosticRequest", "TraceQueryPort", "TraceSpan"]


class TraceQueryPort(ABC):
    @abstractmethod
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]: ...
    @abstractmethod
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int: ...
