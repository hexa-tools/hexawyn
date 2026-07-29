from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData
from hexawyn.domain.services.engineer_workload.night_intervention_service import (
    compute_night_intervention_report,
)


def _make_month(month: str, intervention_count: int, total_nights: int) -> MonthNightData:
    return {
        "month": month,
        "night_intervention_count": intervention_count,
        "total_nights": total_nights,
    }


class TestComputeNightInterventionReport:
    def test_happy_path_single_month(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 5, 30)]
        previous: list[MonthNightData] = []

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.period_label == "July 2026"
        assert result.avg_interventions_per_night == 0.2  # noqa: PLR2004
        assert result.previous_avg_per_night is None
        assert result.delta_pct == 0.0
        assert result.trend == "stable"
        assert "0,2" in result.summary

    def test_happy_path_multiple_months(self) -> None:
        current: list[MonthNightData] = [
            _make_month("2026-07", 6, 31),
            _make_month("2026-08", 9, 31),
        ]
        previous: list[MonthNightData] = [
            _make_month("2026-04", 3, 30),
            _make_month("2026-05", 3, 31),
            _make_month("2026-06", 0, 30),
        ]

        result = compute_night_intervention_report(current, previous, "Q3 2026")

        assert result.period_label == "Q3 2026"
        expected_current = round((6 + 9) / (31 + 31), 1)
        assert result.avg_interventions_per_night == expected_current
        expected_previous = round((3 + 3 + 0) / (30 + 31 + 30), 1)
        assert result.previous_avg_per_night == expected_previous

    def test_degrading_trend(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 20, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 3, 30)]

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.trend == "degrading"
        assert result.delta_pct > 5.0  # noqa: PLR2004

    def test_improving_trend(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 3, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 20, 30)]

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.trend == "improving"
        assert result.delta_pct < -5.0  # noqa: PLR2004

    def test_stable_trend_within_threshold(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 10, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 10, 30)]

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.trend == "stable"
        assert abs(result.delta_pct) <= 5.0  # noqa: PLR2004

    def test_zero_interventions(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 0, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 0, 30)]

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.avg_interventions_per_night == 0.0
        assert result.trend == "stable"
        assert result.delta_pct == 0.0

    def test_zero_total_nights_returns_zero_average(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 5, 0)]
        previous: list[MonthNightData] = []

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.avg_interventions_per_night == 0.0

    def test_previous_average_zero_delta_stable(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 5, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 0, 0)]

        result = compute_night_intervention_report(current, previous, "July 2026")

        assert result.trend == "stable"
        assert result.delta_pct == 0.0

    def test_no_previous_months(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 5, 31)]
        previous: list[MonthNightData] = []

        result = compute_night_intervention_report(current, previous, "Q3")

        assert result.previous_avg_per_night is None
        assert result.summary.startswith("Moyenne")

    def test_summary_with_delta_positive(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 20, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 5, 30)]

        result = compute_night_intervention_report(current, previous, "Q3")

        assert "hausse" in result.summary

    def test_summary_with_delta_negative(self) -> None:
        current: list[MonthNightData] = [_make_month("2026-07", 5, 30)]
        previous: list[MonthNightData] = [_make_month("2026-06", 20, 30)]

        result = compute_night_intervention_report(current, previous, "Q3")

        assert "baisse" in result.summary

    def test_empty_current_months(self) -> None:
        current: list[MonthNightData] = []
        previous: list[MonthNightData] = []

        result = compute_night_intervention_report(current, previous, "empty")

        assert result.avg_interventions_per_night == 0.0
        assert result.previous_avg_per_night is None
