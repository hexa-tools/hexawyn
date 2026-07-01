from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_response import (
    RunWhatIfSimulationResponse,
)


class RunWhatIfSimulationServicePort(ABC):
    @abstractmethod
    def simulate(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse: ...
