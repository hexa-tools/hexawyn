"""Unit tests for detect_capacity_jump / compute_growth_rate — pure slope
computation and capacity-jump/spike detection over a daily value series."""

from __future__ import annotations

import pytest
from hexawyn.domain.services.cluster_capacity_forecast.growth_rate import (
    compute_growth_rate,
    detect_capacity_jump,
)


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

        assert detect_capacity_jump(values) == 5

    def test_sustained_acceleration_is_not_a_single_jump(self) -> None:
        """A multi-day acceleration (recent spike) is a different edge case
        from a discrete one-time capacity jump — must not be conflated."""
        values = [10.0 + 0.1 * i for i in range(11)] + [13.0, 15.0, 17.0]

        assert detect_capacity_jump(values) is None

    def test_flat_series_with_one_jump_and_zero_baseline(self) -> None:
        values = [5.0] * 12 + [15.0]

        assert detect_capacity_jump(values) == 12

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
        assert result.window_days_used == 14

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
        assert 0 < result.slope_per_day < 2.0

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
