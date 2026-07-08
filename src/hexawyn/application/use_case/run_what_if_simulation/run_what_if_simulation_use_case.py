from __future__ import annotations

from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_service_port import (
    RunWhatIfSimulationServicePort,
)


class RunWhatIfSimulationUseCase:
    def __init__(self, service: RunWhatIfSimulationServicePort) -> None:
        self._service = service

    def execute(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        return self._service.simulate(command)
