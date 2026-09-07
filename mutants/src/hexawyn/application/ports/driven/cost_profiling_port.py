from abc import ABC, abstractmethod

from hexawyn.domain.models.cost_profiling import CostProfilingRequest, EndpointCPUProfile


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CostProfilingPort(ABC):
    @abstractmethod
    def fetch_endpoint_cpu_metrics(
        self, request: CostProfilingRequest
    ) -> list[EndpointCPUProfile]: ...
