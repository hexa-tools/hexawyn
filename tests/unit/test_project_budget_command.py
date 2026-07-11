import dataclasses


class TestProjectBudgetCommand:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_command import (
            ProjectBudgetCommand,
        )

        command = ProjectBudgetCommand()

        assert command.horizon_months == 6
        assert command.history_months == 6
        assert command.budget_threshold_usd is None
        assert command.exclude_months == []

    def test_holds_values(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_command import (
            ProjectBudgetCommand,
        )

        command = ProjectBudgetCommand(
            horizon_months=12, budget_threshold_usd=12000.0, exclude_months=["2026-06"]
        )

        assert command.horizon_months == 12
        assert command.budget_threshold_usd == 12000.0
        assert command.exclude_months == ["2026-06"]
        assert dataclasses.is_dataclass(ProjectBudgetCommand)
