from abc import ABC, abstractmethod

from hexawyn.application.use_case.project_budget.command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.project_budget.response import (
    ProjectBudgetResponse,
)


class ProjectBudgetServicePort(ABC):
    @abstractmethod
    def project(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse: ...
