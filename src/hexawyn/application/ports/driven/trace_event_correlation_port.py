from abc import ABC, abstractmethod

from hexawyn.domain.models.trace_k8s_events import K8sEvent, TraceEventCorrelationRequest


class TraceEventCorrelationPort(ABC):
    @abstractmethod
    def fetch_k8s_events(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]: ...
    @abstractmethod
    def fetch_slowest_span(self, request: TraceEventCorrelationRequest) -> str | None: ...
