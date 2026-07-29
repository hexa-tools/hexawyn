from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
    BudgetProjectionAdapter,
    _month_of,
    _to_monthly_raw,
)


class TestBudgetProjectionAdapter:
    def test_empty(self) -> None:
        port = Mock()
        port.get_daily_costs.return_value = []
        assert BudgetProjectionAdapter(cost_forecast_port=port).get_monthly_cost_history(1) == []

    def test_single_month(self) -> None:
        port = Mock()
        port.get_daily_costs.return_value = [
            {"date": "2026-07-01", "total_usd": 10.0},
        ]
        result = BudgetProjectionAdapter(cost_forecast_port=port).get_monthly_cost_history(1)
        assert len(result) == 1
        assert result[0]["month"] == "2026-07"

    def test_multi_month(self) -> None:
        port = Mock()
        port.get_daily_costs.return_value = [
            {"date": "2026-07-01", "total_usd": 10.0},
            {"date": "2026-08-01", "total_usd": 20.0},
        ]
        result = BudgetProjectionAdapter(cost_forecast_port=port).get_monthly_cost_history(2)
        assert len(result) == 2  # noqa: PLR2004


class TestMonthOf:
    def test_valid(self) -> None:
        assert _month_of("2026-07-15") == "2026-07"

    def test_invalid_empty(self) -> None:
        assert _month_of("") is None

    def test_invalid_no_dash(self) -> None:
        assert _month_of("2026") is None

    def test_invalid_non_digit(self) -> None:
        assert _month_of("abc-def") is None


class TestToMonthlyRaw:
    def test_correct_split(self) -> None:
        raw = _to_monthly_raw("2026-07", 100.0)
        assert raw["total_usd"] == 100.0  # noqa: PLR2004
        assert raw["compute_usd"] == 60.0  # noqa: PLR2004
        assert raw["storage_usd"] == 25.0  # noqa: PLR2004
        assert raw["network_usd"] == 15.0  # noqa: PLR2004

    def test_zero_cost(self) -> None:
        raw = _to_monthly_raw("2026-07", 0.0)
        assert raw["total_usd"] == 0.0
