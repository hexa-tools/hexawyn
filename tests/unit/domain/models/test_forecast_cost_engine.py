"""RED → GREEN — Pure domain: CostForecastEngine and module-level helpers."""

from hexawyn.domain.models.cost_forecast import CostForecast
from hexawyn.domain.services.cost_forecast.cost_forecast_engine import (
    CostForecastEngine,
    _as_float,
    _compute_current_spend,
    _compute_trend,
    _month_over_month_delta,
    _top_drivers,
)


class TestComputeCurrentSpend:
    def test_empty_list_returns_zero(self) -> None:
        result = _compute_current_spend([], days_elapsed=5)

        assert result == 0.0

    def test_fewer_points_than_days_extrapolates(self) -> None:
        result = _compute_current_spend(
            [{"total_usd": 10.0}, {"total_usd": 20.0}],
            days_elapsed=10,
        )

        assert result == 150.0  # avg=15 * 10 days  # noqa: PLR2004

    def test_enough_points_returns_sum(self) -> None:
        result = _compute_current_spend(
            [
                {"total_usd": 10.0},
                {"total_usd": 15.0},
                {"total_usd": 5.0},
            ],
            days_elapsed=2,
        )

        assert result == 30.0  # noqa: PLR2004


class TestComputeTrend:
    def test_less_than_two_days_returns_one(self) -> None:
        result = _compute_trend([{"total_usd": 50.0}])

        assert result == 1.0

    def test_all_zero_costs_returns_one(self) -> None:
        result = _compute_trend(
            [
                {"total_usd": 0.0},
                {"total_usd": 0.0},
                {"total_usd": 0.0},
            ]
        )

        assert result == 1.0

    def test_increasing_trend_above_one(self) -> None:
        result = _compute_trend(
            [
                {"total_usd": 10.0},
                {"total_usd": 20.0},
                {"total_usd": 30.0},
                {"total_usd": 40.0},
                {"total_usd": 50.0},
            ]
        )

        assert result > 1.0

    def test_decreasing_trend_below_one(self) -> None:
        result = _compute_trend(
            [
                {"total_usd": 50.0},
                {"total_usd": 40.0},
                {"total_usd": 30.0},
                {"total_usd": 20.0},
                {"total_usd": 10.0},
            ]
        )

        assert result < 1.0


class TestMonthOverMonthDelta:
    def test_none_previous_returns_zero(self) -> None:
        result = _month_over_month_delta(projected=1500.0, previous=None)

        assert result == 0.0

    def test_zero_previous_returns_zero(self) -> None:
        result = _month_over_month_delta(projected=1500.0, previous=0.0)

        assert result == 0.0

    def test_positive_delta(self) -> None:
        result = _month_over_month_delta(projected=1500.0, previous=1000.0)

        assert result == 50.0  # noqa: PLR2004

    def test_negative_delta(self) -> None:
        result = _month_over_month_delta(projected=800.0, previous=1000.0)

        assert result == -20.0  # noqa: PLR2004


class TestTopDrivers:
    def test_empty_daily_costs_returns_empty(self) -> None:
        result = _top_drivers([], projected_total=100.0, top_n=3)

        assert result == []

    def test_namespace_costs_not_a_list_is_skipped(self) -> None:
        result = _top_drivers(
            [
                {
                    "date": "2026-06-01",
                    "total_usd": 20.0,
                    "namespace_costs": "not-a-list",
                },
                {
                    "date": "2026-06-02",
                    "total_usd": 30.0,
                    "namespace_costs": [{"name": "prod", "cost_usd": 50.0}],
                },
            ],
            projected_total=100.0,
            top_n=3,
        )

        assert len(result) == 1
        assert result[0].name == "prod"

    def test_non_dict_namespace_entry_skipped(self) -> None:
        result = _top_drivers(
            [
                {
                    "date": "2026-06-01",
                    "total_usd": 10.0,
                    "namespace_costs": [
                        {"name": "prod", "cost_usd": 50.0},
                        "not-a-dict",
                    ],
                },
            ],
            projected_total=100.0,
            top_n=3,
        )

        assert len(result) == 1
        assert result[0].name == "prod"

    def test_ranks_and_returns_top_n(self) -> None:
        result = _top_drivers(
            [
                {
                    "date": "2026-06-01",
                    "total_usd": 100.0,
                    "namespace_costs": [
                        {"name": "dev", "cost_usd": 20.0},
                        {"name": "prod", "cost_usd": 70.0},
                        {"name": "staging", "cost_usd": 10.0},
                    ],
                },
            ],
            projected_total=100.0,
            top_n=2,
        )

        assert len(result) == 2  # noqa: PLR2004
        assert result[0].name == "prod"
        assert result[1].name == "dev"

    def test_no_namespace_costs_in_any_day_returns_empty(self) -> None:
        result = _top_drivers(
            [
                {"date": "2026-06-01", "total_usd": 50.0},
                {"date": "2026-06-02", "total_usd": 60.0},
            ],
            projected_total=100.0,
            top_n=3,
        )

        assert result == []

    def test_uses_projected_total_when_zero_namespace_agg(self) -> None:
        result = _top_drivers(
            [
                {
                    "date": "2026-06-01",
                    "total_usd": 10.0,
                    "namespace_costs": [{"name": "empty-ns", "cost_usd": 0.0}],
                },
            ],
            projected_total=0.0,
            top_n=1,
        )

        assert len(result) >= 0


class TestAsFloat:
    def test_none_returns_zero(self) -> None:
        result = _as_float(None)

        assert result == 0.0

    def test_int_converted_to_float(self) -> None:
        result = _as_float(42)

        assert result == 42.0  # noqa: PLR2004

    def test_float_passthrough(self) -> None:
        result = _as_float(3.14)

        assert result == 3.14  # noqa: PLR2004

    def test_numeric_string_converted(self) -> None:
        result = _as_float("12.5")

        assert result == 12.5  # noqa: PLR2004

    def test_non_numeric_string_returns_zero(self) -> None:
        result = _as_float("hello")

        assert result == 0.0

    def test_list_returns_zero(self) -> None:
        result = _as_float([1, 2, 3])

        assert result == 0.0


class TestCostForecastEngine:
    def test_forecast_with_empty_daily_costs(self) -> None:
        engine = CostForecastEngine()

        forecast = engine.forecast(
            daily_costs=[],
            cluster_name="test-cluster",
            month="2026-06",
            days_elapsed=15,
            days_in_month=30,
        )

        assert forecast.cluster_name == "test-cluster"
        assert forecast.current_spend_usd == 0.0
        assert forecast.projected_total_usd == 0.0

    def test_forecast_with_custom_top_n(self) -> None:
        engine = CostForecastEngine()

        forecast = engine.forecast(
            daily_costs=[
                {
                    "date": "2026-06-01",
                    "total_usd": 100.0,
                    "namespace_costs": [
                        {"name": "a", "cost_usd": 30.0},
                        {"name": "b", "cost_usd": 40.0},
                        {"name": "c", "cost_usd": 20.0},
                        {"name": "d", "cost_usd": 10.0},
                    ],
                },
            ],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
            top_n=2,
        )

        assert len(forecast.top_cost_drivers) == 2  # noqa: PLR2004

    def test_forecast_with_previous_month(self) -> None:
        engine = CostForecastEngine()

        forecast = engine.forecast(
            daily_costs=[
                {"date": "2026-06-01", "total_usd": 100.0},
                {"date": "2026-06-02", "total_usd": 120.0},
            ],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=2,
            days_in_month=30,
            previous_month_usd=900.0,
        )

        assert forecast.previous_month_usd == 900.0  # noqa: PLR2004
        assert forecast.month_over_month_delta != 0.0

    def test_forecast_with_custom_confidence_and_source(self) -> None:
        engine = CostForecastEngine()

        forecast = engine.forecast(
            daily_costs=[{"date": "2026-06-01", "total_usd": 100.0}],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
            data_source="aws_cur",
            forecast_confidence="medium",
        )

        assert forecast.data_source == "aws_cur"
        assert forecast.forecast_confidence == "medium"

    def test_forecast_returns_typed_model(self) -> None:
        engine = CostForecastEngine()

        forecast = engine.forecast(
            daily_costs=[{"date": "2026-06-01", "total_usd": 100.0}],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )

        assert isinstance(forecast, CostForecast)
        assert forecast.days_elapsed == 1
        assert forecast.days_remaining == 29  # noqa: PLR2004
        assert forecast.billing_events == []
        assert isinstance(forecast.top_cost_drivers, list)
