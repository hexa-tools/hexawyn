from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.use_case.finops.project_budget.command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.finops.project_budget.response import (
    ProjectBudgetResponse,
)
from hexawyn.domain.services.budget_projection.budget_projection_service import (
    BudgetProjectionService,
)


class ProjectBudgetUseCase:
    def __init__(self, budget_port: BudgetProjectionPort) -> None:
        self._port = budget_port
        self._engine = BudgetProjectionService()

    def execute(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore
