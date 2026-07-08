from abc import ABC, abstractmethod

from hexawyn.domain.models.metric_correlation import CorrelationRequest, TimeSeries


class MetricCorrelationPort(ABC):
    @abstractmethod
    def fetch_primary_series(self, request: CorrelationRequest) -> TimeSeries: ...
    @abstractmethod
    def fetch_correlated_series(self, request: CorrelationRequest) -> TimeSeries: ...
