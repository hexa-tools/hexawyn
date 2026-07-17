from unittest.mock import MagicMock

from hexawyn.application.ports.driven.budget_projection_port import (
    BudgetProjectionPort,
    MonthlyCostRaw,
)
from hexawyn.application.ports.driving.project_budget.project_budget_command import (
    ProjectBudgetCommand,
)


def _month(label: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=label,
        total_usd=total,
        compute_usd=total * 0.6,
        storage_usd=total * 0.25,
        network_usd=total * 0.15,
    )


def _steady(count: int) -> list[MonthlyCostRaw]:
    history: list[MonthlyCostRaw] = []
    value = 8000.0
    for index in range(count):
        history.append(_month(f"2026-{index + 1:02d}", round(value, 2)))
        value *= 1.12
    return history


class TestProjectBudgetService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
            ProjectBudgetServicePort,
        )
        from hexawyn.application.service.project_budget_service import (
            ProjectBudgetService,
        )

        service = ProjectBudgetService(budget_port=MagicMock(spec=BudgetProjectionPort))

        assert isinstance(service, ProjectBudgetServicePort)

    def test_project_returns_report(self) -> None:
        from hexawyn.application.service.project_budget_service import (
            ProjectBudgetService,
        )

        port = MagicMock(spec=BudgetProjectionPort)
        port.get_monthly_cost_history.return_value = _steady(6)
        service = ProjectBudgetService(budget_port=port)

        response = service.project(ProjectBudgetCommand(horizon_months=6))

        port.get_monthly_cost_history.assert_called_once_with(6)
        assert len(response.result.projected_months) == 6
        assert response.result.confidence == "high"

    def test_project_passes_budget_threshold(self) -> None:
        from hexawyn.application.service.project_budget_service import (
            ProjectBudgetService,
        )

        port = MagicMock(spec=BudgetProjectionPort)
        port.get_monthly_cost_history.return_value = _steady(6)
        service = ProjectBudgetService(budget_port=port)

        response = service.project(
            ProjectBudgetCommand(horizon_months=6, budget_threshold_usd=12000.0)
        )

        assert response.result.budget_exceeded is True

    def test_project_requests_history_months(self) -> None:
        from hexawyn.application.service.project_budget_service import (
            ProjectBudgetService,
        )

        port = MagicMock(spec=BudgetProjectionPort)
        port.get_monthly_cost_history.return_value = _steady(3)
        service = ProjectBudgetService(budget_port=port)

        service.project(ProjectBudgetCommand(history_months=3))

        port.get_monthly_cost_history.assert_called_once_with(3)

    def test_project_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.project_budget_service import (
            ProjectBudgetService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=BudgetProjectionPort)
        port.get_monthly_cost_history.side_effect = ClusterUnreachableError("down")
        service = ProjectBudgetService(budget_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.project(ProjectBudgetCommand())
