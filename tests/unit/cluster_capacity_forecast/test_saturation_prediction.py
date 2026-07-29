"""Unit tests for predict_saturation — pure ceiling-extrapolation math."""

from __future__ import annotations

from datetime import date

from hexawyn.domain.services.cluster_capacity_forecast.saturation_prediction import (
    predict_saturation,
)

_MAX_HORIZON = 365


class TestPredictSaturation:
    def test_cpu_saturates_in_fifteen_days(self) -> None:
        """TC1: CPU at 70% (67.2/96), growing 1.92 cores/day → 15 days."""
        result = predict_saturation(
            current=67.2,
            ceiling=96.0,
            growth_rate_per_day=1.92,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation == 15  # noqa: PLR2004
        assert result.saturation_date == "2026-07-02"
        assert result.capped_horizon is False

    def test_memory_saturates_in_forty_days(self) -> None:
        """TC2: Memory at 80% (307.2/384), growing 1.92 GB/day → 40 days."""
        result = predict_saturation(
            current=307.2,
            ceiling=384.0,
            growth_rate_per_day=1.92,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation == 40  # noqa: PLR2004

    def test_negative_growth_means_no_risk(self) -> None:
        """TC4 / edge case: negative growth (decommissioned workloads) → capacity freeing."""
        result = predict_saturation(
            current=60.0,
            ceiling=96.0,
            growth_rate_per_day=-1.0,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation is None
        assert result.saturation_date is None
        assert result.capped_horizon is False

    def test_zero_growth_means_stable(self) -> None:
        """TC5: usage flat → no saturation predicted."""
        result = predict_saturation(
            current=60.0,
            ceiling=96.0,
            growth_rate_per_day=0.0,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation is None

    def test_horizon_beyond_max_is_capped(self) -> None:
        """Checker edge case: growth=0.01%/day implying ~3000 days must be
        capped, not reported as a literal absurd date."""
        result = predict_saturation(
            current=50.0,
            ceiling=100.0,
            growth_rate_per_day=0.01,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation is None
        assert result.saturation_date is None
        assert result.capped_horizon is True

    def test_horizon_exactly_at_cap_is_not_capped(self) -> None:
        result = predict_saturation(
            current=0.0,
            ceiling=365.0,
            growth_rate_per_day=1.0,
            observed_at=date(2026, 6, 17),
            max_horizon_days=_MAX_HORIZON,
        )

        assert result.days_to_saturation == 365  # noqa: PLR2004
        assert result.capped_horizon is False
