from __future__ import annotations

from hexawyn.domain.services.budget_projection.growth_estimator import GrowthEstimate


class TestProjectScenarios:
    def test_realistic_uses_compound_growth(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        estimate = GrowthEstimate(current_monthly_usd=8000.0, monthly_rate_pct=12.0, model="linear")

        months = project_months(
            estimate,
            horizon=6,
            category_mix={"compute": 0.6, "storage": 0.25, "network": 0.15},
            start_month="2026-06",
        )

        assert len(months) == 6  # noqa: PLR2004
        month6 = months[5]
        assert month6.month_offset == 6  # noqa: PLR2004
        assert 15700 <= month6.realistic_usd <= 15900  # noqa: PLR2004

    def test_optimistic_below_realistic_below_pessimistic(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        estimate = GrowthEstimate(current_monthly_usd=8000.0, monthly_rate_pct=12.0, model="linear")

        months = project_months(
            estimate, horizon=6, category_mix={"compute": 1.0}, start_month="2026-06"
        )

        for month in months:
            assert month.optimistic_usd < month.realistic_usd < month.pessimistic_usd

    def test_category_breakdown_sums_to_realistic(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        estimate = GrowthEstimate(current_monthly_usd=8000.0, monthly_rate_pct=12.0, model="linear")

        months = project_months(
            estimate,
            horizon=3,
            category_mix={"compute": 0.6, "storage": 0.25, "network": 0.15},
            start_month="2026-06",
        )

        month = months[0]
        assert abs(sum(month.by_category.values()) - month.realistic_usd) < 0.5  # noqa: PLR2004

    def test_month_labels_increment(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        estimate = GrowthEstimate(current_monthly_usd=8000.0, monthly_rate_pct=10.0, model="linear")

        months = project_months(
            estimate, horizon=8, category_mix={"compute": 1.0}, start_month="2026-11"
        )

        assert months[0].month_label == "2026-12"
        assert months[1].month_label == "2027-01"
        assert months[2].month_label == "2027-02"

    def test_decreasing_growth_projects_savings(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        estimate = GrowthEstimate(
            current_monthly_usd=10000.0, monthly_rate_pct=-10.0, model="decreasing"
        )

        months = project_months(
            estimate, horizon=6, category_mix={"compute": 1.0}, start_month="2026-06"
        )

        assert months[5].realistic_usd < 10000.0  # noqa: PLR2004

    def test_pessimistic_wider_for_exponential(self) -> None:
        from hexawyn.domain.services.budget_projection.scenario_projector import project_months

        exponential = GrowthEstimate(
            current_monthly_usd=8000.0, monthly_rate_pct=20.0, model="exponential"
        )
        linear = GrowthEstimate(current_monthly_usd=8000.0, monthly_rate_pct=20.0, model="linear")

        exp_months = project_months(
            exponential, horizon=6, category_mix={"compute": 1.0}, start_month="2026-06"
        )
        lin_months = project_months(
            linear, horizon=6, category_mix={"compute": 1.0}, start_month="2026-06"
        )

        assert exp_months[5].pessimistic_usd > lin_months[5].pessimistic_usd
