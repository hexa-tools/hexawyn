"""RED → GREEN — Layer 2: CostForecastEngine pure domain service."""

import pytest
from hexawyn.domain.models.cost_forecast import CostForecast, ResourceCost
from hexawyn.domain.services.cost_forecast.cost_forecast_engine import (
    CostForecastEngine,
    _compute_current_spend,
    _compute_trend,
    _month_over_month_delta,
    _top_drivers,
)


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
        assert result.days_elapsed == 22  # noqa: PLR2004
        assert result.days_remaining == 8  # noqa: PLR2004

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
        assert result.historical_days_used == 7  # noqa: PLR2004


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
        assert len(result.top_cost_drivers) == 3  # noqa: PLR2004

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


class TestCostForecastEngineEdgeCases:
    def test_empty_daily_costs_returns_zeros(self) -> None:
        result = _engine().forecast(
            daily_costs=[],
            cluster_name="empty",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.current_spend_usd == 0.0
        assert result.projected_total_usd == 0.0
        assert result.trend_factor == 1.0
        assert result.top_cost_drivers == []
        assert result.historical_days_used == 0

    def test_zero_days_elapsed_produces_zero_daily_avg(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-01", 100.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=0,
            days_in_month=30,
        )
        assert result.days_elapsed == 0
        assert result.days_remaining == 30  # noqa: PLR2004

    def test_days_elapsed_exceeds_days_in_month(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-30", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=31,
            days_in_month=30,
        )
        assert result.days_elapsed == 31  # noqa: PLR2004
        assert result.days_remaining < 0

    def test_previous_month_zero_is_treated_same_as_none(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            previous_month_usd=0.0,
        )
        assert result.month_over_month_delta == 0.0

    def test_all_zero_daily_totals_yields_trend_one(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily(f"2026-06-{i:02d}", 0.0) for i in range(16, 23)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.trend_factor == 1.0
        assert result.projected_total_usd == 0.0

    def test_top_n_zero_returns_empty_drivers(self) -> None:
        ns_costs = [{"name": "prod", "cost_usd": 200.0}]
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 200.0, ns_costs)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            top_n=0,
        )
        assert result.top_cost_drivers == []

    def test_top_n_negative_returns_empty_drivers(self) -> None:
        ns_costs = [{"name": "prod", "cost_usd": 200.0}]
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 200.0, ns_costs)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
            top_n=-1,
        )
        assert result.top_cost_drivers == []

    def test_single_data_point_projected_equals_daily_times_days(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-01", 100.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )
        assert result.projected_total_usd == pytest.approx(3000.0, abs=0.01)

    def test_february_28_days(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-02-14", 50.0)],
            cluster_name="prod",
            month="2026-02",
            days_elapsed=14,
            days_in_month=28,
        )
        assert result.days_remaining == 14  # noqa: PLR2004
        assert result.projected_total_usd == pytest.approx(1400.0, abs=0.01)

    def test_billing_events_list_is_always_empty(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-22", 50.0)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert result.billing_events == []

    def test_namespace_costs_with_malformed_entries(self) -> None:
        ns_costs = [{"name": "good", "cost_usd": 100.0}, "not_a_dict", None]
        daily_costs = [_daily("2026-06-22", 100.0, ns_costs)]  # type: ignore[arg-type]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_in_month=30,
        )
        assert len(result.top_cost_drivers) == 1
        assert result.top_cost_drivers[0].name == "good"


class TestExactForecastPayload:
    def test_full_payload_matches_expected(self) -> None:
        daily_costs = [
            _daily(
                f"2026-06-{day:02d}",
                value,
                [{"name": "pay", "cost_usd": 0.6}, {"name": "web", "cost_usd": 0.4}],
            )
            for day, value in zip(range(1, 6), [1.0, 2.0, 3.0, 5.0, 8.0], strict=True)
        ]

        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=5,
            days_in_month=30,
            top_n=3,
            previous_month_usd=100.0,
        )

        assert result == CostForecast(
            cluster_name="prod",
            month="2026-06",
            days_elapsed=5,
            days_remaining=25,
            current_spend_usd=19.0,
            projected_total_usd=152.33,
            previous_month_usd=100.0,
            month_over_month_delta=52.33,
            trend_factor=1.4035,
            top_cost_drivers=[
                ResourceCost(
                    name="pay",
                    kind="namespace",
                    monthly_cost_usd=18.0,
                    percentage=60.0,
                ),
                ResourceCost(
                    name="web",
                    kind="namespace",
                    monthly_cost_usd=12.0,
                    percentage=40.0,
                ),
            ],
            billing_events=[],
            forecast_confidence="low",
            historical_days_used=5,
            data_source="estimated",
        )


class TestComputeTrendHelpers:
    def test_trend_two_data_points_returns_one(self) -> None:
        daily_costs = [_daily("d1", 10.0), _daily("d2", 20.0)]
        assert _compute_trend(daily_costs) == 1.0

    def test_trend_zero_totals_returns_one(self) -> None:
        daily_costs = [_daily(f"d{i}", 0.0) for i in range(3)]
        assert _compute_trend(daily_costs) == 1.0

    def test_trend_one_data_point_returns_one(self) -> None:
        assert _compute_trend([_daily("d1", 10.0)]) == 1.0


class TestComputeCurrentSpendHelpers:
    def test_current_spend_empty_returns_zero(self) -> None:
        assert _compute_current_spend([], 5) == 0.0

    def test_current_spend_exact_days_matches_sum(self) -> None:
        daily_costs = [_daily(f"d{i}", 10.0) for i in range(3)]
        assert _compute_current_spend(daily_costs, 3) == 30.0  # noqa: PLR2004

    def test_current_spend_more_points_than_days_matches_sum(self) -> None:
        daily_costs = [_daily(f"d{i}", 10.0) for i in range(4)]
        assert _compute_current_spend(daily_costs, 3) == 40.0  # noqa: PLR2004


class TestMonthOverMonthDeltaHelpers:
    def test_delta_none_returns_zero(self) -> None:
        assert _month_over_month_delta(110.0, None) == 0.0

    def test_delta_zero_previous_returns_zero(self) -> None:
        assert _month_over_month_delta(110.0, 0.0) == 0.0

    def test_delta_rounds_to_two_decimals(self) -> None:
        assert _month_over_month_delta(110.123, 100.0) == 10.12  # noqa: PLR2004


class TestTopDriversHelpers:
    def test_top_drivers_empty_costs(self) -> None:
        assert _top_drivers([], 100.0, 3) == []

    def test_top_drivers_no_namespace_costs(self) -> None:
        daily_costs = [_daily("d1", 10.0)]
        assert _top_drivers(daily_costs, 100.0, 3) == []

    def test_top_drivers_no_aggregated_cost(self) -> None:
        daily_costs = [_daily("d1", 10.0, [{"name": "", "cost_usd": 0.0}])]
        result = _top_drivers(daily_costs, 100.0, 3)

        assert result == [
            ResourceCost(name="", kind="namespace", monthly_cost_usd=0.0, percentage=0.0)
        ]

    def test_top_drivers_name_defaults_to_empty(self) -> None:
        daily_costs = [_daily("d1", 10.0, [{"cost_usd": 5.0}, {"name": "x", "cost_usd": 3.0}])]
        result = _top_drivers(daily_costs, 100.0, 2)

        assert result == [
            ResourceCost(name="", kind="namespace", monthly_cost_usd=150.0, percentage=62.5),
            ResourceCost(name="x", kind="namespace", monthly_cost_usd=90.0, percentage=37.5),
        ]

    def test_top_drivers_projected_total_zero_falls_back_to_daily(self) -> None:
        daily_costs = [
            _daily(
                "d1",
                10.0,
                [{"name": "pay", "cost_usd": 1.0}, {"name": "web", "cost_usd": 2.0}],
            )
        ]
        result = _top_drivers(daily_costs, 0.0, 3)

        assert result == [
            ResourceCost(name="web", kind="namespace", monthly_cost_usd=60.0, percentage=66.7),
            ResourceCost(name="pay", kind="namespace", monthly_cost_usd=30.0, percentage=33.3),
        ]

    def test_top_drivers_fractional_projected_total(self) -> None:
        daily_costs = [
            _daily("d1", 10.0, [{"name": "pay", "cost_usd": 0.6}, {"name": "web", "cost_usd": 0.4}])
        ]
        result = _top_drivers(daily_costs, 152.33, 3)

        assert result[0].monthly_cost_usd == 18.0  # noqa: PLR2004
        assert result[1].monthly_cost_usd == 12.0  # noqa: PLR2004

    def test_top_drivers_projected_between_zero_and_one(self) -> None:
        daily_costs = [
            _daily("d1", 10.0, [{"name": "pay", "cost_usd": 0.6}, {"name": "web", "cost_usd": 0.4}])
        ]
        result = _top_drivers(daily_costs, 0.5, 3)

        assert result[0].percentage == 60.0  # noqa: PLR2004
        assert result[1].percentage == 40.0  # noqa: PLR2004  # noqa: PLR2004


class TestForecastMutationBoundaries:
    def test_current_spend_rounds_to_two_decimals(self) -> None:
        daily_costs = [_daily(f"2026-06-{d:02d}", 100.123) for d in range(1, 6)]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=5,
            days_in_month=30,
        )

        assert result.current_spend_usd == 500.62  # noqa: PLR2004

    def test_zero_elapsed_with_empty_costs_projects_zero(self) -> None:
        result = _engine().forecast(
            daily_costs=[],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=0,
            days_in_month=30,
        )

        assert result.projected_total_usd == 0.0

    def test_default_top_n_is_three(self) -> None:
        ns_costs = [{"name": f"n{i}", "cost_usd": float(i + 1)} for i in range(5)]
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-01", 10.0, ns_costs)],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )

        assert len(result.top_cost_drivers) == 3  # noqa: PLR2004

    def test_top_drivers_monthly_rounds_to_two_decimals(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-01", 10.0, [{"name": "a", "cost_usd": 0.1234}])],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )

        assert result.top_cost_drivers[0].monthly_cost_usd == 3.7  # noqa: PLR2004

    def test_non_dict_namespace_skipped_not_breaking_rest(self) -> None:
        result = _engine().forecast(
            daily_costs=[_daily("2026-06-01", 10.0, ["junk", {"name": "ok", "cost_usd": 5.0}])],
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )

        assert len(result.top_cost_drivers) == 1
        assert result.top_cost_drivers[0].name == "ok"


class TestCoverageBranches:
    def test_namespace_costs_non_list_skipped(self) -> None:
        daily_costs = [_daily("2026-06-01", 10.0, "not-a-list")]  # type: ignore[arg-type]
        result = _engine().forecast(
            daily_costs=daily_costs,
            cluster_name="prod",
            month="2026-06",
            days_elapsed=1,
            days_in_month=30,
        )

        assert result.top_cost_drivers == []

    def test_daily_total_none_treated_as_zero(self) -> None:
        daily_costs = [
            {"date": "2026-06-01", "total_usd": None, "namespace_costs": []},
            {"date": "2026-06-02", "total_usd": "5.5", "namespace_costs": []},
        ]
        result = _engine().forecast(
            daily_costs=daily_costs,  # type: ignore[arg-type]
            cluster_name="prod",
            month="2026-06",
            days_elapsed=2,
            days_in_month=30,
        )

        assert result.current_spend_usd == 5.5  # noqa: PLR2004

    def test_daily_total_unparseable_treated_as_zero(self) -> None:
        daily_costs = [
            {"date": "2026-06-01", "total_usd": "abc", "namespace_costs": []},
            {"date": "2026-06-02", "total_usd": 4.5, "namespace_costs": []},
        ]
        result = _engine().forecast(
            daily_costs=daily_costs,  # type: ignore[arg-type]
            cluster_name="prod",
            month="2026-06",
            days_elapsed=2,
            days_in_month=30,
        )

        assert result.current_spend_usd == 4.5  # noqa: PLR2004
