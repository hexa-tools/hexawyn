from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.project_budget.project_budget_command import (
    ProjectBudgetCommand,
)
from hexawyn.application.ports.driving.project_budget.project_budget_response import (
    ProjectBudgetResponse,
)


class ProjectBudgetServicePort(ABC):
    @abstractmethod
    def project(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse: ...
