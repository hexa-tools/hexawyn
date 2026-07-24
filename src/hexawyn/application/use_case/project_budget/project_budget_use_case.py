from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.use_case.project_budget.command import ProjectBudgetCommand
from hexawyn.application.use_case.project_budget.response import ProjectBudgetResponse


class ProjectBudgetUseCase:
    def __init__(self, port: BudgetProjectionPort) -> None:
        self._port = port

    def execute(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        return ProjectBudgetResponse()
