"""Unit tests for compute_hot_status — pure per-resource hot-detection over a
timestamped utilization series."""

from __future__ import annotations

import pytest
from hexawyn.domain.services.hot_node_analysis.hot_node_detection import compute_hot_status


def _series(hourly_values: list[float], start_hour: int = 0) -> list[tuple[str, float]]:
    return [
        (f"2026-06-17T{(start_hour + i) % 24:02d}:00:00Z", value)
        for i, value in enumerate(hourly_values)
    ]


class TestComputeHotStatus:
    def test_tc1_cpu_ninety_two_percent_for_twenty_of_twentyfour_hours_is_hot(self) -> None:
        """TC1: worker-1 CPU 92% for 20/24h → hot."""
        series = _series([92.0] * 20 + [50.0] * 4)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is True
        assert status.hot_hours == 20  # noqa: PLR2004
        assert status.avg_percent == pytest.approx(85.0)

    def test_tc4_no_hot_hours_is_not_hot(self) -> None:
        """TC4: no hot nodes → healthy."""
        series = _series([50.0] * 24)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is False
        assert status.hot_hours == 0

    def test_tc5_eighty_five_percent_cpu_is_hot(self) -> None:
        """TC5: 85% CPU consistently → hot (memory independence is exercised
        by calling this same function separately for the memory series)."""
        series = _series([85.0] * 24)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is True

    def test_thirty_percent_memory_is_not_hot(self) -> None:
        """TC5: 30% memory → not hot, independent of the CPU result."""
        series = _series([30.0] * 24)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is False

    def test_just_under_duration_threshold_is_not_hot(self) -> None:
        series = _series([92.0] * 11 + [50.0] * 13)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is False

    def test_empty_series_is_not_hot(self) -> None:
        status = compute_hot_status([], threshold_pct=80.0, duration_pct=50.0)

        assert status.is_hot is False
        assert status.avg_percent == 0.0
        assert status.hot_hours == 0
        assert status.business_hours_pattern is False


class TestBusinessHoursPattern:
    def test_hot_hours_clustered_in_business_hours_is_flagged(self) -> None:
        """Edge case: utilization spikes only during business hours (9-18)."""
        hourly = [30.0] * 9 + [92.0] * 9 + [30.0] * 6
        series = _series(hourly, start_hour=0)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=30.0)

        assert status.business_hours_pattern is True

    def test_hot_hours_scattered_across_day_and_night_is_not_flagged(self) -> None:
        hourly = [92.0 if h in (0, 1, 2, 22, 23) else 30.0 for h in range(24)]
        series = _series(hourly, start_hour=0)

        status = compute_hot_status(series, threshold_pct=80.0, duration_pct=10.0)

        assert status.business_hours_pattern is False
