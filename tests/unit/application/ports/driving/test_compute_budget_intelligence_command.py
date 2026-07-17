import dataclasses


class TestComputeBudgetIntelligenceCommand:
    def test_holds_period(self) -> None:
        from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
            ComputeBudgetIntelligenceCommand,
        )

        command = ComputeBudgetIntelligenceCommand(period="current")
        assert command.period == "current"
        assert dataclasses.is_dataclass(ComputeBudgetIntelligenceCommand)
