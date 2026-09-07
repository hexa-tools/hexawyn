from abc import ABC, abstractmethod

from hexawyn.domain.models.trace_k8s_events import K8sEvent, TraceEventCorrelationRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TraceEventCorrelationPort(ABC):
    @abstractmethod
    def fetch_k8s_events(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]: ...
    @abstractmethod
    def fetch_slowest_span(self, request: TraceEventCorrelationRequest) -> str | None: ...
