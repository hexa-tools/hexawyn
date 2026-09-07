"""Unit tests for estimate_growth — monthly growth rate + model classification."""

from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw
from hexawyn.domain.services.budget_projection.growth_estimator import (
    GrowthEstimate,
    _classify_model,
    _is_accelerating,
    _month_over_month_changes,
    estimate_growth,
)


def _raw(
    month: str, total: float, compute: float = 0.0, storage: float = 0.0, network: float = 0.0
) -> MonthlyCostRaw:
    return {
        "month": month,
        "total_usd": total,
        "compute_usd": compute,
        "storage_usd": storage,
        "network_usd": network,
    }


class TestEstimateGrowthShortHistory:
    def test_empty_history_flat_zero(self) -> None:
        result = estimate_growth([])
        assert result == GrowthEstimate(current_monthly_usd=0.0, monthly_rate_pct=0.0, model="flat")

    def test_single_month_flat(self) -> None:
        result = estimate_growth([_raw("2026-01", 100.0)])
        assert result == GrowthEstimate(
            current_monthly_usd=100.0, monthly_rate_pct=0.0, model="flat"
        )


class TestEstimateGrowthFlat:
    def test_constant_history_flat(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 100.0)]
        result = estimate_growth(history)
        assert result == GrowthEstimate(
            current_monthly_usd=100.0, monthly_rate_pct=0.0, model="flat"
        )

    def test_under_half_percent_change_is_flat(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 100.3)]
        result = estimate_growth(history)
        assert result.model == "flat"

    def test_all_zero_previous_months_flat(self) -> None:
        history = [_raw("2026-01", 0.0), _raw("2026-02", 0.0), _raw("2026-03", 50.0)]
        result = estimate_growth(history)
        assert result == GrowthEstimate(
            current_monthly_usd=50.0, monthly_rate_pct=0.0, model="flat"
        )


class TestEstimateGrowthDecreasing:
    def test_negative_rate_decreasing(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 90.0)]
        result = estimate_growth(history)
        assert result.model == "decreasing"
        assert result.monthly_rate_pct == -10.0  # noqa: PLR2004


class TestEstimateGrowthLinear:
    def test_constant_increase_is_linear(self) -> None:
        history = [
            _raw("2026-01", 100.0),
            _raw("2026-02", 110.0),
            _raw("2026-03", 121.0),
            _raw("2026-04", 133.1),
        ]
        result = estimate_growth(history)
        assert result.model == "linear"
        assert result.current_monthly_usd == 133.1  # noqa: PLR2004


class TestEstimateGrowthExponential:
    def test_accelerating_increase_is_exponential(self) -> None:
        history = [
            _raw("2026-01", 100.0),
            _raw("2026-02", 110.0),
            _raw("2026-03", 130.0),
            _raw("2026-04", 165.0),
        ]
        result = estimate_growth(history)
        assert result.model == "exponential"
        assert result.current_monthly_usd == 165.0  # noqa: PLR2004


class TestClassifyModel:
    def test_flat_at_negative_tolerance_boundary(self) -> None:
        assert _classify_model(-0.5, [-0.5]) == "flat"

    def test_flat_at_positive_tolerance_boundary(self) -> None:
        assert _classify_model(0.5, [0.5]) == "flat"

    def test_above_tolerance_is_linear_when_not_accelerating(self) -> None:
        assert _classify_model(10.0, [10.0, 10.0]) == "linear"

    def test_above_tolerance_accelerating_is_exponential(self) -> None:
        assert _classify_model(10.0, [5.0, 10.0, 20.0]) == "exponential"

    def test_negative_mean_rate_is_decreasing(self) -> None:
        assert _classify_model(-10.0, [-10.0]) == "decreasing"


class TestIsAccelerating:
    def test_single_change_not_accelerating(self) -> None:
        assert _is_accelerating([5.0]) is False

    def test_all_gaps_over_two_percent_is_accelerating(self) -> None:
        assert _is_accelerating([5.0, 10.0, 20.0]) is True

    def test_stagnant_gap_not_accelerating(self) -> None:
        assert _is_accelerating([5.0, 5.0]) is False

    def test_small_gap_not_accelerating(self) -> None:
        assert _is_accelerating([5.0, 6.5]) is False

    def test_two_point_gap_exactly_two_not_accelerating(self) -> None:
        assert _is_accelerating([5.0, 7.0]) is False


class TestMonthOverMonthChanges:
    def test_changes_are_percentages(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 110.0), _raw("2026-03", 121.0)]
        assert _month_over_month_changes(history) == [10.0, 10.0]

    def test_zero_previous_month_skipped(self) -> None:
        history = [_raw("2026-01", 0.0), _raw("2026-02", 50.0), _raw("2026-03", 60.0)]
        assert _month_over_month_changes(history) == [20.0]

    def test_changes_round_mean_two_decimals(self) -> None:
        history = [
            _raw("2026-01", 100.0),
            _raw("2026-02", 110.0),
            _raw("2026-03", 122.1),
        ]
        result = estimate_growth(history)
        assert result.monthly_rate_pct == 10.5  # noqa: PLR2004


class TestRoundingBoundaries:
    def test_mean_rate_rounds_to_two_decimals(self) -> None:
        history = [
            _raw("2026-01", 100.0),
            _raw("2026-02", 110.0),
            _raw("2026-03", 121.0055),
        ]
        result = estimate_growth(history)
        assert result.monthly_rate_pct == 10.0  # noqa: PLR2004

    def test_two_changes_accelerating_is_true(self) -> None:
        assert _is_accelerating([5.0, 9.0]) is True

    def test_rate_between_half_and_one_is_not_decreasing(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 100.7)]
        result = estimate_growth(history)
        assert result.monthly_rate_pct == 0.7  # noqa: PLR2004
        assert result.model == "linear"
