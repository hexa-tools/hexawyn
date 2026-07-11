from dataclasses import fields


class TestProjectedMonth:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.budget_projection import ProjectedMonth

        field_names = {f.name for f in fields(ProjectedMonth)}

        assert field_names == {
            "month_offset",
            "month_label",
            "realistic_usd",
            "optimistic_usd",
            "pessimistic_usd",
            "by_category",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.budget_projection import ProjectedMonth

        month = ProjectedMonth(
            month_offset=6,
            month_label="2026-12",
            realistic_usd=15869.0,
            optimistic_usd=12000.0,
            pessimistic_usd=20000.0,
            by_category={"compute": 10000.0, "storage": 3869.0, "network": 2000.0},
        )

        assert month.month_offset == 6
        assert month.realistic_usd == 15869.0
        assert month.by_category["compute"] == 10000.0


class TestBudgetProjectionReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.budget_projection import BudgetProjectionReport

        report = BudgetProjectionReport(
            current_monthly_usd=8000.0,
            growth_rate_pct=12.0,
            growth_model="linear",
        )

        assert report.current_monthly_usd == 8000.0
        assert report.growth_rate_pct == 12.0
        assert report.growth_model == "linear"
        assert report.projected_months == []
        assert report.six_month_total_realistic == 0.0
        assert report.confidence == "low"
        assert report.budget_threshold_usd is None
        assert report.budget_exceeded is False
        assert report.budget_breach_month is None
        assert report.warning == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.budget_projection import BudgetProjectionReport

        report = BudgetProjectionReport(
            current_monthly_usd=8000.0,
            growth_rate_pct=12.0,
            growth_model="exponential",
            confidence="high",
            budget_threshold_usd=12000.0,
            budget_exceeded=True,
            budget_breach_month="2026-10",
            warning="Exponential growth detected.",
        )

        assert report.growth_model == "exponential"
        assert report.budget_exceeded is True
        assert report.budget_breach_month == "2026-10"
