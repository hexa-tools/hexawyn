from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.run_what_if_simulation.command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.use_case.cluster.run_what_if_simulation.response import (
    RunWhatIfSimulationResponse,
)


class RunWhatIfSimulationServicePort(ABC):
    @abstractmethod
    def simulate(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse: ...
