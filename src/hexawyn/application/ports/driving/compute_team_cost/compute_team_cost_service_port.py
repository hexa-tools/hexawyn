from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_response import (
    ComputeTeamCostResponse,
)


class ComputeTeamCostServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse: ...
