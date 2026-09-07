from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.project_budget.command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.finops.project_budget.project_budget_use_case import (  # noqa: E501
    ProjectBudgetUseCase,
)
from hexawyn.application.use_case.finops.project_budget.response import (
    ProjectBudgetResponse,
)


class TestProjectBudgetUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_monthly_cost_history.return_value = []

        use_case = ProjectBudgetUseCase(budget_port=port)
        result = use_case.execute(ProjectBudgetCommand())

        assert isinstance(result, ProjectBudgetResponse)
