from __future__ import annotations

from hexawyn.domain.models.budget_intelligence import (
    BudgetAlertRecommendation,
    BudgetIntelligenceReport,
)
from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
    _build_recommendations,
    compute_budget_intelligence,
)


class TestComputeBudgetIntelligence:
    def test_no_budget_configured(self) -> None:
        data = {
            "budget_monthly_eur": None,
            "projected_spend_eur": 1000.0,
            "current_spend_eur": 500.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        assert not report.config_available
        assert report.period_label == "2026-07"

    def test_zero_budget(self) -> None:
        data = {"budget_monthly_eur": 0, "projected_spend_eur": 1000.0, "current_spend_eur": 500.0}
        report = compute_budget_intelligence(data, "2026-07")
        assert not report.config_available

    def test_budget_not_exceeded(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 800.0,
            "current_spend_eur": 300.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        assert report.config_available
        assert not report.budget_exceeded
        assert report.recommendations == []

    def test_budget_exceeded(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 1500.0,
            "current_spend_eur": 800.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        assert report.budget_exceeded
        assert report.overshoot_pct > 0
        assert len(report.recommendations) == 3  # noqa: PLR2004

    def test_budget_exactly_matched(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 1000.0,
            "current_spend_eur": 500.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        assert not report.budget_exceeded
        assert report.overshoot_pct == 0.0

    def test_budget_negative(self) -> None:
        data = {
            "budget_monthly_eur": -100.0,
            "projected_spend_eur": 500.0,
            "current_spend_eur": 200.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        assert not report.config_available

    def test_recommendations_are_budget_alert_type(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 1500.0,
            "current_spend_eur": 800.0,
        }
        report = compute_budget_intelligence(data, "2026-07")
        for rec in report.recommendations:
            assert isinstance(rec, BudgetAlertRecommendation)


class TestExactBudgetIntelligencePayload:
    def test_exceeded_report_full_payload(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 1500.0,
            "current_spend_eur": 800.0,
        }
        report = compute_budget_intelligence(data, "2026-07")

        assert report == BudgetIntelligenceReport(
            period_label="2026-07",
            current_spend_eur=800.0,
            projected_spend_eur=1500.0,
            budget_monthly_eur=1000.0,
            overshoot_pct=50.0,
            budget_exceeded=True,
            recommendations=[
                BudgetAlertRecommendation(
                    action="Verifier les workloads les plus couteux",
                    description="Identifier les services consommant le plus de ressources.",
                ),
                BudgetAlertRecommendation(
                    action="Optimiser les limites CPU",
                    description="Reduire les requests/limits sur-contraintes sans impact.",
                ),
                BudgetAlertRecommendation(
                    action="Reporter les traitements non critiques",
                    description="Decaler les batch jobs hors pic (+50.0% projete).",
                ),
            ],
            config_available=True,
            explanation="",
        )

    def test_not_exceeded_report_full_payload(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 800.0,
            "current_spend_eur": 300.0,
        }
        report = compute_budget_intelligence(data, "2026-07")

        assert report == BudgetIntelligenceReport(
            period_label="2026-07",
            current_spend_eur=300.0,
            projected_spend_eur=800.0,
            budget_monthly_eur=1000.0,
            overshoot_pct=-20.0,
            budget_exceeded=False,
            recommendations=[],
            config_available=True,
            explanation="",
        )

    def test_no_config_report_full_payload(self) -> None:
        data = {
            "budget_monthly_eur": None,
            "projected_spend_eur": 1500.0,
            "current_spend_eur": 800.0,
        }
        report = compute_budget_intelligence(data, "2026-07")

        assert report == BudgetIntelligenceReport(
            period_label="2026-07",
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=0.0,
            overshoot_pct=0.0,
            budget_exceeded=False,
            recommendations=[],
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    def test_overshoot_rounds_to_one_decimal(self) -> None:
        data = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 1050.123,
            "current_spend_eur": 800.0,
        }
        report = compute_budget_intelligence(data, "2026-07")

        assert report.overshoot_pct == 5.0  # noqa: PLR2004
        assert report.recommendations[2].description == (
            "Decaler les batch jobs hors pic (+5.0% projete)."
        )


class TestBuildRecommendationsNotExceeded:
    def test_empty_when_not_exceeded(self) -> None:
        assert _build_recommendations(False, 50.0) == []


class TestSubUnitBudget:
    def test_budget_between_zero_and_one_is_valid(self) -> None:
        data = {
            "budget_monthly_eur": 0.5,
            "projected_spend_eur": 1.0,
            "current_spend_eur": 0.4,
        }
        report = compute_budget_intelligence(data, "2026-07")

        assert report.config_available is True
        assert report.budget_exceeded is True
        assert report.overshoot_pct == 100.0  # noqa: PLR2004
