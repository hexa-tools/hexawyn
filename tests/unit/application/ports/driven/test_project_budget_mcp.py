"""RED → GREEN — MCP tool: project_budget."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.budget_projection_port import (
    BudgetProjectionPort,
    MonthlyCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


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


def _port(history: list[MonthlyCostRaw]) -> MagicMock:
    port = MagicMock(spec=BudgetProjectionPort)
    port.get_monthly_cost_history.return_value = history
    return port


class TestProjectBudgetTool:
    def test_returns_projection_with_scenarios(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_projection_adapter",
            return_value=_port(_steady(6)),
        ):
            from hexawyn.mcp.tools.project_budget import project_budget

            result = project_budget()

        assert len(result["projected_months"]) == 6
        assert result["growth_rate_pct"] > 0
        assert result["confidence"] == "high"
        month6 = result["projected_months"][5]
        assert month6["optimistic_usd"] < month6["realistic_usd"] < month6["pessimistic_usd"]
        assert result["error"] is None

    def test_budget_threshold_alert(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_projection_adapter",
            return_value=_port(_steady(6)),
        ):
            from hexawyn.mcp.tools.project_budget import project_budget

            result = project_budget(budget_threshold_usd=12000.0)

        assert result["budget_exceeded"] is True
        assert result["budget_breach_month"] is not None

    def test_low_confidence_warning_with_scarce_data(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_projection_adapter",
            return_value=_port([_month("2026-01", 8000.0)]),
        ):
            from hexawyn.mcp.tools.project_budget import project_budget

            result = project_budget()

        assert result["confidence"] == "low"
        assert result["warning"] != ""

    def test_category_breakdown_present(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_projection_adapter",
            return_value=_port(_steady(6)),
        ):
            from hexawyn.mcp.tools.project_budget import project_budget

            result = project_budget()

        assert set(result["projected_months"][0]["by_category"]) == {
            "compute",
            "storage",
            "network",
        }

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_projection_adapter",
            side_effect=ClusterUnreachableError("cost source down"),
        ):
            from hexawyn.mcp.tools.project_budget import project_budget

            result = project_budget()

        assert result["projected_months"] == []
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.project_budget import register

        assert callable(register)
