from abc import ABC, abstractmethod

from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, LatencyPercentiles


class LatencyPercentilePort(ABC):
    @abstractmethod
    def fetch_percentiles(self, request: LatencyPercentileRequest) -> LatencyPercentiles: ...
