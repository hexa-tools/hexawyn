from __future__ import annotations

from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.domain.models.cost_profiling import CostProfilingRequest, EndpointCPUProfile


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class OTelCostProfilingAdapter(CostProfilingPort):
    def fetch_endpoint_cpu_metrics(self, request: CostProfilingRequest) -> list[EndpointCPUProfile]:
        return []
