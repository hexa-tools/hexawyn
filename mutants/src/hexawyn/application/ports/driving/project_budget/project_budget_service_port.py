from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.project_budget.command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.finops.project_budget.response import (
    ProjectBudgetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ProjectBudgetServicePort(ABC):
    @abstractmethod
    def project(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse: ...
