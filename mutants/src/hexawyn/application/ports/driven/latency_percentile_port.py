from abc import ABC, abstractmethod

from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, LatencyPercentiles


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class LatencyPercentilePort(ABC):
    @abstractmethod
    def fetch_percentiles(self, request: LatencyPercentileRequest) -> LatencyPercentiles: ...
