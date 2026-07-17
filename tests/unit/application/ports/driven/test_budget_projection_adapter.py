from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.ports.driven.cost_forecast_port import (
    CostForecastPort,
    DailyCostData,
)


def _day(date: str, total: float) -> DailyCostData:
    return DailyCostData(date=date, total_usd=total, namespace_costs=[])


class TestPortImplementation:
    def test_is_a_budget_projection_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        assert isinstance(
            BudgetProjectionAdapter(cost_forecast_port=MagicMock(spec=CostForecastPort)),
            BudgetProjectionPort,
        )


class TestGetMonthlyCostHistory:
    def test_aggregates_daily_costs_into_months(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = [
            _day("2026-05-01", 100.0),
            _day("2026-05-02", 100.0),
            _day("2026-06-01", 200.0),
        ]
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        history = adapter.get_monthly_cost_history(months=2)

        may = next(m for m in history if m["month"] == "2026-05")
        june = next(m for m in history if m["month"] == "2026-06")
        assert may["total_usd"] == 200.0
        assert june["total_usd"] == 200.0

    def test_months_sorted_oldest_first(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = [
            _day("2026-06-01", 200.0),
            _day("2026-04-01", 100.0),
            _day("2026-05-01", 150.0),
        ]
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        history = adapter.get_monthly_cost_history(months=3)

        assert [m["month"] for m in history] == ["2026-04", "2026-05", "2026-06"]

    def test_category_split_sums_to_total(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = [_day("2026-05-01", 1000.0)]
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        month = adapter.get_monthly_cost_history(months=1)[0]

        total_split = month["compute_usd"] + month["storage_usd"] + month["network_usd"]
        assert abs(total_split - month["total_usd"]) < 0.5

    def test_requests_history_window_in_days(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = []
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        adapter.get_monthly_cost_history(months=6)

        port.get_daily_costs.assert_called_once_with(180)

    def test_empty_costs_returns_empty_history(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = []
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        assert adapter.get_monthly_cost_history(months=6) == []

    def test_malformed_date_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
            BudgetProjectionAdapter,
        )

        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = [_day("bad", 100.0), _day("2026-05-02", 50.0)]
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)

        history = adapter.get_monthly_cost_history(months=1)

        assert len(history) == 1
        assert history[0]["month"] == "2026-05"
