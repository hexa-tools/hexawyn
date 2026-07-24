from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.use_case.run_what_if_simulation.command import RunWhatIfSimulationCommand
from hexawyn.application.use_case.run_what_if_simulation.response import RunWhatIfSimulationResponse


class RunWhatIfSimulationUseCase:
    def __init__(self, port: WhatIfSimulationPort) -> None:
        self._port = port

    def execute(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        return RunWhatIfSimulationResponse()
