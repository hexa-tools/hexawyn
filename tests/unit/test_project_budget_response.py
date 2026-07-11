from hexawyn.domain.models.budget_projection import BudgetProjectionReport


class TestProjectBudgetResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_response import (
            ProjectBudgetResponse,
        )

        report = BudgetProjectionReport(
            current_monthly_usd=8000.0, growth_rate_pct=12.0, growth_model="linear"
        )
        response = ProjectBudgetResponse(result=report)

        assert response.result is report
        assert response.result.current_monthly_usd == 8000.0
