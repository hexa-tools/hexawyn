"""Unit tests for detect_capacity_jump / compute_growth_rate — pure slope
computation and capacity-jump/spike detection over a daily value series."""

from __future__ import annotations

import pytest
from hexawyn.domain.services.cluster_capacity_forecast.growth_rate import (
    _has_recent_spike,
    _is_outlier,
    _least_squares_slope,
    compute_growth_rate,
    detect_capacity_jump,
)


class TestIsOutlierDirect:
    def test_delta_above_threshold_with_positive_baseline(self) -> None:
        assert _is_outlier(7.0, 6.0, 1.0) is True

    def test_delta_below_threshold_with_positive_baseline(self) -> None:
        assert _is_outlier(5.0, 6.0, 1.0) is False

    def test_delta_equal_threshold_not_outlier(self) -> None:
        assert _is_outlier(6.0, 6.0, 1.0) is False

    def test_zero_baseline_uses_delta_positive(self) -> None:
        assert _is_outlier(0.5, 0.0, 0.0) is True
        assert _is_outlier(-0.5, 0.0, 0.0) is False

    def test_fractional_baseline_still_uses_threshold(self) -> None:
        assert _is_outlier(2.0, 6.0, 0.5) is False


class TestLeastSquaresSlopeDirect:
    def test_single_point_zero_slope(self) -> None:
        assert _least_squares_slope([3.0]) == 0.0

    def test_two_point_slope(self) -> None:
        assert _least_squares_slope([0.0, 2.0]) == 2.0  # noqa: PLR2004

    def test_linear_series_exact_slope(self) -> None:
        assert _least_squares_slope([10.0, 12.0, 14.0, 16.0, 18.0]) == 2.0  # noqa: PLR2004

    def test_declining_series_negative_slope(self) -> None:
        assert _least_squares_slope([5.0, 4.0, 3.0, 2.0]) == -1.0

    def test_flat_series_zero_slope(self) -> None:
        assert _least_squares_slope([7.0, 7.0, 7.0, 7.0]) == 0.0

    def test_step_series_slope_exact(self) -> None:
        assert _least_squares_slope([0.0, 1.0, 2.0, 100.0, 101.0]) == 30.1  # noqa: PLR2004


class TestHasRecentSpikeDirect:
    def test_short_series_false(self) -> None:
        assert _has_recent_spike([1.0, 2.0, 3.0], 1.0) is False

    def test_flat_series_false(self) -> None:
        assert _has_recent_spike([5.0] * 15, 0.0) is False

    def test_recent_acceleration_true(self) -> None:
        series = [10.0]
        for _ in range(11):
            series.append(series[-1] + 0.1)
        series.append(series[-1] + 3.0)
        series.append(series[-1] + 3.0)
        series.append(series[-1] + 3.0)
        assert _has_recent_spike(series, _least_squares_slope(series)) is True

    def test_linear_series_no_recent_spike(self) -> None:
        series = [float(value) for value in range(1, 16)]
        assert _has_recent_spike(series, _least_squares_slope(series)) is False

    def test_recent_slowdown_false(self) -> None:
        series = [8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        assert _has_recent_spike(series, _least_squares_slope(series)) is False

    def test_flat_baseline_with_tiny_slope_flags_recent_uptick(self) -> None:
        series = [5.0] * 100_000 + [5.0, 5.5, 6.0]
        slope = _least_squares_slope(series)
        assert slope < 1e-9  # noqa: PLR2004
        assert _has_recent_spike(series, slope) is True


class TestDetectCapacityJump:
    def test_clean_linear_series_has_no_jump(self) -> None:
        values = [10.0 + 2.0 * i for i in range(14)]

        assert detect_capacity_jump(values) is None

    def test_single_step_change_is_detected(self) -> None:
        values = [
            10.0,
            12.0,
            14.0,
            16.0,
            18.0,
            50.0,
            52.0,
            54.0,
            56.0,
            58.0,
            60.0,
            62.0,
            64.0,
            66.0,
        ]

        assert detect_capacity_jump(values) == 5  # noqa: PLR2004

    def test_sustained_acceleration_is_not_a_single_jump(self) -> None:
        """A multi-day acceleration (recent spike) is a different edge case
        from a discrete one-time capacity jump — must not be conflated."""
        values = [10.0 + 0.1 * i for i in range(11)] + [13.0, 15.0, 17.0]

        assert detect_capacity_jump(values) is None

    def test_flat_series_with_one_jump_and_zero_baseline(self) -> None:
        values = [5.0] * 12 + [15.0]

        assert detect_capacity_jump(values) == 12  # noqa: PLR2004

    def test_too_few_points_returns_none(self) -> None:
        assert detect_capacity_jump([1.0, 2.0, 3.0]) is None


class TestComputeGrowthRate:
    def test_clean_linear_series_computes_exact_slope(self) -> None:
        """Matches the ticket's own CPU test data: 1.92 cores/day."""
        values = [67.2 - 1.92 * (13 - i) for i in range(14)]

        result = compute_growth_rate(values)

        assert result.slope_per_day == pytest.approx(1.92, abs=0.01)
        assert result.capacity_jump_detected is False
        assert result.spike_caveat is False
        assert result.window_days_used == 14  # noqa: PLR2004

    def test_flat_series_has_near_zero_slope(self) -> None:
        """TC5: usage flat for 14 days → no saturation predicted."""
        values = [50.0] * 14

        result = compute_growth_rate(values)

        assert result.slope_per_day == pytest.approx(0.0, abs=1e-9)

    def test_declining_series_has_negative_slope(self) -> None:
        """TC4 / edge case: growth rate negative (decommissioned workloads)."""
        values = [80.0 - 1.5 * i for i in range(14)]

        result = compute_growth_rate(values)

        assert result.slope_per_day < 0

    def test_capacity_jump_restricts_slope_to_post_jump_segment(self) -> None:
        values = [
            10.0,
            12.0,
            14.0,
            16.0,
            18.0,
            50.0,
            52.0,
            54.0,
            56.0,
            58.0,
            60.0,
            62.0,
            64.0,
            66.0,
        ]

        result = compute_growth_rate(values)

        assert result.capacity_jump_detected is True
        assert result.slope_per_day == pytest.approx(2.0, abs=0.01)

    def test_recent_spike_flagged_as_caveat_without_being_a_jump(self) -> None:
        values = [10.0 + 0.1 * i for i in range(11)] + [13.0, 15.0, 17.0]

        result = compute_growth_rate(values)

        assert result.capacity_jump_detected is False
        assert result.spike_caveat is True
        assert 0 < result.slope_per_day < 2.0  # noqa: PLR2004

    def test_insufficient_points_returns_zero_slope(self) -> None:
        result = compute_growth_rate([5.0])

        assert result.slope_per_day == 0.0
        assert result.window_days_used == 1
        assert result.capacity_jump_detected is False
        assert result.spike_caveat is False

    def test_empty_series_returns_zero_slope(self) -> None:
        result = compute_growth_rate([])

        assert result.slope_per_day == 0.0
        assert result.window_days_used == 0

    def test_jump_near_end_leaves_single_point_segment(self) -> None:
        values = [10.0] * 13 + [1000.0]

        result = compute_growth_rate(values)

        assert result.capacity_jump_detected is True
        assert result.slope_per_day == 0.0

    def test_short_series_skips_spike_check(self) -> None:
        result = compute_growth_rate([10.0, 11.0, 12.0])

        assert result.capacity_jump_detected is False
        assert result.spike_caveat is False

    def test_two_point_series_slope(self) -> None:
        result = compute_growth_rate([1.0, 2.0])

        assert result.slope_per_day == 1.0
        assert result.window_days_used == 2  # noqa: PLR2004

    def test_jump_never_flags_spike_caveat(self) -> None:
        values = [10.0, 12.0, 14.0, 16.0, 18.0, 50.0, 52.0, 54.0]
        result = compute_growth_rate(values)

        assert result.capacity_jump_detected is True
        assert result.spike_caveat is False
        assert result.slope_per_day == 2.0  # noqa: PLR2004

    def test_four_point_jump_detected(self) -> None:
        values = [10.0, 12.0, 14.0, 50.0]

        assert detect_capacity_jump(values) == 3  # noqa: PLR2004
        result = compute_growth_rate(values)
        assert result.capacity_jump_detected is True
        assert result.window_days_used == 4  # noqa: PLR2004

    def test_four_point_no_jump(self) -> None:
        assert detect_capacity_jump([10.0, 12.0, 14.0, 16.0]) is None
