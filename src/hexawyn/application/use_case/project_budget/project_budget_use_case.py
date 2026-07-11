from __future__ import annotations

from hexawyn.application.ports.driving.project_budget.project_budget_command import (
    ProjectBudgetCommand,
)
from hexawyn.application.ports.driving.project_budget.project_budget_response import (
    ProjectBudgetResponse,
)
from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
    ProjectBudgetServicePort,
)


class ProjectBudgetUseCase:
    def __init__(self, service: ProjectBudgetServicePort) -> None:
        self._service = service

    def execute(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        return self._service.project(command)
