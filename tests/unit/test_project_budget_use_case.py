from unittest.mock import MagicMock

from hexawyn.application.ports.driving.project_budget.project_budget_command import (
    ProjectBudgetCommand,
)
from hexawyn.application.ports.driving.project_budget.project_budget_response import (
    ProjectBudgetResponse,
)
from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
    ProjectBudgetServicePort,
)
from hexawyn.domain.models.budget_projection import BudgetProjectionReport


class TestProjectBudgetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.project_budget.project_budget_use_case import (
            ProjectBudgetUseCase,
        )

        service = MagicMock(spec=ProjectBudgetServicePort)
        expected = ProjectBudgetResponse(
            result=BudgetProjectionReport(
                current_monthly_usd=8000.0, growth_rate_pct=12.0, growth_model="linear"
            )
        )
        service.project.return_value = expected
        use_case = ProjectBudgetUseCase(service=service)
        command = ProjectBudgetCommand()

        response = use_case.execute(command)

        service.project.assert_called_once_with(command)
        assert response is expected
