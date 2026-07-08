"""RED → GREEN — Layer 2: CostForecastEngine pure domain service."""

import pytest
from hexawyn.domain.services.cost_forecast.cost_forecast_engine import CostForecastEngine


def _daily(date: str, total: float, ns_costs: list[dict] | None = None) -> dict:
    return {"date": date, "total_usd": total, "namespace_costs": ns_costs or []}


def _engine() -> CostForecastEngine:
    return CostForecastEngine()


class TestCostForecastEngineProjection:
    def test_projected_total_equals_daily_rate_times_days_in_month(self) -> None:
        # Single data point: $50/day estimated
        daily_costs = [_daily("2026-06-22", 50.0)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        # current_spend = 50 * 22 = 1100, daily_avg = 50, projected = 50 * 30
        assert result.projected_total_usd == pytest.approx(1500.0, abs=0.01)

    def test_current_spend_extrapolated_from_single_data_point(self) -> None:
        daily_costs = [_daily("2026-06-22", 50.0)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.current_spend_usd == pytest.approx(1100.0, abs=0.01)

    def test_days_elapsed_and_remaining_set_correctly(self) -> None:
        daily_costs = [_daily("2026-06-22", 50.0)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.days_elapsed == 22
        assert result.days_remaining == 8

    def test_cluster_name_and_month_passed_through(self) -> None:
        daily_costs = [_daily("2026-06-22", 50.0)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="my-cluster",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.cluster_name == "my-cluster"
        assert result.month == "2026-06"

    def test_historical_days_used_equals_len_of_daily_costs(self) -> None:
        daily_costs = [_daily(f"2026-06-{i:02d}", 50.0) for i in range(16, 23)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.historical_days_used == 7


class TestCostForecastEngineTrend:
    def test_uniform_daily_costs_give_trend_factor_one(self) -> None:
        daily_costs = [_daily(f"2026-06-{i:02d}", 50.0) for i in range(16, 23)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.trend_factor == pytest.approx(1.0, abs=0.01)

    def test_accelerating_costs_give_trend_factor_above_one(self) -> None:
        # Last 3 days average much higher than overall average
        daily_costs = [
            _daily("2026-06-16", 40.0),
            _daily("2026-06-17", 40.0),
            _daily("2026-06-18", 40.0),
            _daily("2026-06-19", 40.0),
            _daily("2026-06-20", 80.0),
            _daily("2026-06-21", 80.0),
            _daily("2026-06-22", 80.0),
        ]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.trend_factor > 1.0

    def test_decelerating_costs_give_trend_factor_below_one(self) -> None:
        daily_costs = [
            _daily("2026-06-16", 80.0),
            _daily("2026-06-17", 80.0),
            _daily("2026-06-18", 80.0),
            _daily("2026-06-19", 80.0),
            _daily("2026-06-20", 40.0),
            _daily("2026-06-21", 40.0),
            _daily("2026-06-22", 40.0),
        ]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.trend_factor < 1.0

    def test_single_data_point_trend_is_one(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.trend_factor == pytest.approx(1.0, abs=0.001)


class TestCostForecastEngineMonthOverMonth:
    def test_delta_positive_when_more_expensive_than_previous(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            previous_month_usd=1000.0,
        )
        # projected = 50 * 30 = 1500, previous = 1000 → +50%
        assert result.month_over_month_delta == pytest.approx(50.0, abs=0.1)

    def test_delta_is_zero_when_no_previous_month(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            previous_month_usd=None,
        )
        assert result.previous_month_usd is None
        assert result.month_over_month_delta == 0.0


class TestCostForecastEngineTopDrivers:
    def test_top_drivers_sorted_by_cost_descending(self) -> None:
        ns_costs = [
            {"name": "prod", "cost_usd": 200.0},
            {"name": "ml", "cost_usd": 500.0},
            {"name": "staging", "cost_usd": 100.0},
        ]
        daily_costs = [_daily("2026-06-22", 800.0, ns_costs)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            top_n=3,
        )
        assert result.top_cost_drivers[0].name == "ml"
        assert result.top_cost_drivers[1].name == "prod"
        assert result.top_cost_drivers[2].name == "staging"

    def test_top_n_limits_drivers(self) -> None:
        ns_costs = [{"name": f"ns-{i}", "cost_usd": float(i * 10)} for i in range(10)]
        daily_costs = [_daily("2026-06-22", 450.0, ns_costs)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            top_n=3,
        )
        assert len(result.top_cost_drivers) == 3

    def test_resource_cost_percentage_computed(self) -> None:
        ns_costs = [{"name": "ml", "cost_usd": 400.0}, {"name": "api", "cost_usd": 400.0}]
        daily_costs = [_daily("2026-06-22", 800.0, ns_costs)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.top_cost_drivers[0].percentage == pytest.approx(50.0, abs=0.1)


class TestCostForecastEngineConfidence:
    def test_data_source_and_confidence_passed_through(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            data_source="aws",
            forecast_confidence="high",
        )
        assert result.data_source == "aws"
        assert result.forecast_confidence == "high"

    def test_default_confidence_is_low(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.forecast_confidence == "low"
        assert result.data_source == "estimated"
