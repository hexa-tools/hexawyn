from abc import ABC, abstractmethod

from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowTrace


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SlowTraceSearchPort(ABC):
    @abstractmethod
    def search_pod_traces(self, request: SlowestTracesRequest) -> list[SlowTrace]: ...
