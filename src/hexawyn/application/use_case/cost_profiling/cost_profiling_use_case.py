from __future__ import annotations

from hexawyn.application.ports.driving.cost_profiling.cost_profiling_command import (
    CostProfilingCommand,
)
from hexawyn.application.ports.driving.cost_profiling.cost_profiling_response import (
    CostProfilingResponse,
)
from hexawyn.application.ports.driving.cost_profiling.cost_profiling_service_port import (
    CostProfilingServicePort,
)


class CostProfilingUseCase:
    def __init__(self, service: CostProfilingServicePort) -> None:
        self._svc = service

    def execute(self, cmd: CostProfilingCommand) -> CostProfilingResponse:
        return self._svc.profile(cmd)
