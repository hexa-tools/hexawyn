from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_team_cost.command import (  # noqa: E501
    ComputeTeamCostCommand,
)
from hexawyn.application.use_case.finops.compute_team_cost.response import (  # noqa: E501
    ComputeTeamCostResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeTeamCostServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse: ...
