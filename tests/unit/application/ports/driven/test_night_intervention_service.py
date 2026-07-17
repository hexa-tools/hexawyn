from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData


def _month(month: str, interventions: int, nights: int) -> MonthNightData:
    return MonthNightData(month=month, night_intervention_count=interventions, total_nights=nights)


class TestFormula:
    def test_zero_point_eight_per_night(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 24, 30)], previous_months=[], period="Ce mois"
        )

        assert report.avg_interventions_per_night == 0.8

    def test_delta_minus_43_percent(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        # Current: 0.8, previous: 1.4 → delta = (0.8-1.4)/1.4*100 = -42.9%
        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 24, 30)],
            previous_months=[_month("2026-Q1", 126, 90)],
            period="Ce mois",
        )

        assert -43.5 <= report.delta_pct <= -42.0
        assert report.trend == "improving"

    def test_stable_when_no_previous(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 24, 30)], previous_months=[], period="Ce mois"
        )

        assert report.trend == "stable"
        assert report.previous_avg_per_night is None

    def test_summary_includes_percentage(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 24, 30)],
            previous_months=[_month("2026-Q1", 126, 90)],
            period="Ce mois",
        )

        assert "40%" in report.summary or "43%" in report.summary or "42" in report.summary
        assert "intervention" in report.summary.lower()


class TestEdgeCases:
    def test_zero_nights_returns_zero(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 0, 0)], previous_months=[], period="Ce mois"
        )

        assert report.avg_interventions_per_night == 0.0

    def test_degrading_trend(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 60, 30)],
            previous_months=[_month("2026-Q1", 30, 30)],
            period="Ce mois",
        )

        assert report.trend == "degrading"
        assert report.delta_pct > 0

    def test_stable_trend_with_previous(self) -> None:
        from hexawyn.domain.services.engineer_workload.night_intervention_service import (
            compute_night_intervention_report,
        )

        report = compute_night_intervention_report(
            current_months=[_month("2026-06", 31, 30)],
            previous_months=[_month("2026-Q1", 30, 30)],
            period="Ce mois",
        )

        assert report.trend == "stable"
        assert report.previous_avg_per_night is not None
