from abc import ABC, abstractmethod

from hexawyn.domain.models.metric_correlation import CorrelationRequest, TimeSeries


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MetricCorrelationPort(ABC):
    @abstractmethod
    def fetch_primary_series(self, request: CorrelationRequest) -> TimeSeries: ...
    @abstractmethod
    def fetch_correlated_series(self, request: CorrelationRequest) -> TimeSeries: ...
