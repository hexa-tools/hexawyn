from abc import ABC, abstractmethod

from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowTrace


class SlowTraceSearchPort(ABC):
    @abstractmethod
    def search_pod_traces(self, request: SlowestTracesRequest) -> list[SlowTrace]: ...
