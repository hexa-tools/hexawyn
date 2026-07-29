from __future__ import annotations

from hexawyn.domain.models.budget_intelligence import BudgetAlertRecommendation
from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
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
