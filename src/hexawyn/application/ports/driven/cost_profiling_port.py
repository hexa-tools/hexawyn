from abc import ABC, abstractmethod

from hexawyn.domain.models.cost_profiling import CostProfilingRequest, EndpointCPUProfile


class CostProfilingPort(ABC):
    @abstractmethod
    def fetch_endpoint_cpu_metrics(
        self, request: CostProfilingRequest
    ) -> list[EndpointCPUProfile]: ...
