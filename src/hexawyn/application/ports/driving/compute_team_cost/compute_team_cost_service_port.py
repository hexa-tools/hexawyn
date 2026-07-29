from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_team_cost.command import (  # noqa: E501
    ComputeTeamCostCommand,
)
from hexawyn.application.use_case.finops.compute_team_cost.response import (  # noqa: E501
    ComputeTeamCostResponse,
)


class ComputeTeamCostServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse: ...
