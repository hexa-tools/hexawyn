from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.application.use_case.cost_profiling.command import CostProfilingCommand
from hexawyn.application.use_case.cost_profiling.response import CostProfilingResponse


class CostProfilingUseCase:
    def __init__(self, port: CostProfilingPort) -> None:
        self._port = port

    def execute(self, command: CostProfilingCommand) -> CostProfilingResponse:
        return CostProfilingResponse()
