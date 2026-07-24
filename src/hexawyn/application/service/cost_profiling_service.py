from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.application.use_case.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.cost_profiling.response import (
    CostProfilingResponse,
)
from hexawyn.application.ports.driving.cost_profiling.cost_profiling_service_port import (
    CostProfilingServicePort,
)
from hexawyn.domain.models.cost_profiling import CostProfilingRequest, CostProfilingResult


class CostProfilingService(CostProfilingServicePort):
    def __init__(self, port: CostProfilingPort) -> None:
        self._port = port

    def profile(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )
