"""Unit tests for calculate_age_days / is_stale — deterministic date
arithmetic. Checker case 1: (today - last_modified).days must be exact, off
by more than one day is a FAIL."""

from __future__ import annotations

from datetime import date


class TestCalculateAgeDays:
    def test_checker_case_1_exact_day_count(self) -> None:
        """last_modified=2025-12-17, today=2026-06-16 -> 181 days, not 180."""
        from hexawyn.domain.services.secret_rotation.age_calculator import calculate_age_days

        age = calculate_age_days(last_modified=date(2025, 12, 17), today=date(2026, 6, 16))

        assert age == 181

    def test_zero_days_when_modified_today(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import calculate_age_days

        age = calculate_age_days(last_modified=date(2026, 1, 1), today=date(2026, 1, 1))

        assert age == 0

    def test_tc3_thirty_days(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import calculate_age_days

        age = calculate_age_days(last_modified=date(2026, 6, 1), today=date(2026, 7, 1))

        assert age == 30


class TestIsStale:
    def test_tc1_180_days_exceeds_90_day_threshold(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import is_stale

        assert is_stale(age_days=180, threshold_days=90) is True

    def test_tc2_95_days_exceeds_90_day_threshold(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import is_stale

        assert is_stale(age_days=95, threshold_days=90) is True

    def test_tc3_30_days_is_within_threshold(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import is_stale

        assert is_stale(age_days=30, threshold_days=90) is False

    def test_exactly_at_threshold_is_not_stale(self) -> None:
        from hexawyn.domain.services.secret_rotation.age_calculator import is_stale

        assert is_stale(age_days=90, threshold_days=90) is False
