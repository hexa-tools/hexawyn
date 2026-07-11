from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligenceData


def _data(
    current: float = 4000.0,
    projected: float = 16000.0,
    budget: float | None = 12000.0,
) -> BudgetIntelligenceData:
    return BudgetIntelligenceData(
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
    )


class TestBudgetExceeded:
    def test_projected_over_budget_flagged(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=16000.0, budget=12000.0), period="2026-06"
        )

        assert report.budget_exceeded is True
        assert report.overshoot_pct > 0

    def test_projected_under_budget_not_flagged(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=8000.0, budget=12000.0), period="2026-06"
        )

        assert report.budget_exceeded is False
        assert report.overshoot_pct < 0

    def test_exactly_at_budget_not_exceeded(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=12000.0, budget=12000.0), period="2026-06"
        )

        assert report.budget_exceeded is False


class TestRecommendations:
    def test_exceeded_generates_recommendations(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=16000.0, budget=12000.0), period="2026-06"
        )

        assert len(report.recommendations) == 3

    def test_within_budget_no_recommendations(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=8000.0, budget=12000.0), period="2026-06"
        )

        assert report.recommendations == []


class TestMissingConfig:
    def test_no_budget_yields_explanation(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(_data(budget=None), period="2026-06")

        assert report.config_available is False
        assert "cloud_budget_monthly" in report.explanation
        assert report.budget_exceeded is False

    def test_zero_budget_treated_as_unconfigured(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(_data(budget=0.0), period="2026-06")

        assert report.config_available is False


class TestOvershoot:
    def test_forty_percent_over(self) -> None:
        from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
            compute_budget_intelligence,
        )

        report = compute_budget_intelligence(
            _data(projected=14000.0, budget=10000.0), period="2026-06"
        )

        assert report.overshoot_pct == 40.0
