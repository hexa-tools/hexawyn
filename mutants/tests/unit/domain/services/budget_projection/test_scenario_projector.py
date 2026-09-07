from __future__ import annotations

from hexawyn.domain.services.budget_projection.growth_estimator import GrowthEstimate
from hexawyn.domain.services.budget_projection.scenario_projector import (
    _add_months,
    _compound,
    _pessimistic_factor,
    _split_categories,
)


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


class TestCompoundRounding:
    def test_compound_rounds_to_two_decimals(self) -> None:
        assert _compound(100.0, 0.00123, 1) == 100.12  # noqa: PLR2004

    def test_compound_exponential_offset(self) -> None:
        assert _compound(100.0, 0.1, 2) == 121.0  # noqa: PLR2004


class TestSplitCategoriesRounding:
    def test_split_rounds_each_category_to_two_decimals(self) -> None:
        assert _split_categories(100.123, {"a": 0.5}) == {"a": 50.06}  # noqa: PLR2004

    def test_split_preserves_share_fraction(self) -> None:
        assert _split_categories(100.0, {"a": 0.123}) == {"a": 12.3}  # noqa: PLR2004


class TestPessimisticFactor:
    def test_exponential_model_uses_double_pessimistic_factor(self) -> None:
        assert _pessimistic_factor("exponential") == 2.0  # noqa: PLR2004

    def test_linear_model_uses_standard_pessimistic_factor(self) -> None:
        assert _pessimistic_factor("linear") == 1.5  # noqa: PLR2004

    def test_decreasing_model_uses_standard_pessimistic_factor(self) -> None:
        assert _pessimistic_factor("decreasing") == 1.5  # noqa: PLR2004

    def test_flat_model_uses_standard_pessimistic_factor(self) -> None:
        assert _pessimistic_factor("flat") == 1.5  # noqa: PLR2004


class TestAddMonths:
    def test_same_year_increment(self) -> None:
        assert _add_months("2026-03", 2) == "2026-05"

    def test_rolls_over_year(self) -> None:
        assert _add_months("2026-11", 3) == "2027-02"

    def test_december_wraps_to_january(self) -> None:
        assert _add_months("2026-12", 1) == "2027-01"
