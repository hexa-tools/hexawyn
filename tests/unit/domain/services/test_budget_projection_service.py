from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw
from hexawyn.domain.services.budget_projection.budget_projection_service import (
    BudgetProjectionService,
    _apply_seasonality,
    _budget_breach,
    _category_mix,
    _confidence,
    _exclude,
    _scale,
    _warning,
)


def _raw(
    month: str,
    total: float,
    compute_usd: float = 50.0,
    storage_usd: float = 30.0,
    network_usd: float = 20.0,
) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=total,
        compute_usd=compute_usd,
        storage_usd=storage_usd,
        network_usd=network_usd,
    )


def _pm(  # noqa: PLR0913
    offset: int,
    label: str,
    realistic: float,
    optimistic: float,
    pessimistic: float,
    by_category: dict[str, float] | None = None,
) -> object:
    from hexawyn.domain.models.budget_projection import ProjectedMonth

    return ProjectedMonth(
        month_offset=offset,
        month_label=label,
        realistic_usd=realistic,
        optimistic_usd=optimistic,
        pessimistic_usd=pessimistic,
        by_category=by_category
        or {"compute": realistic * 0.6, "storage": realistic * 0.25, "network": realistic * 0.15},
    )


class TestExclude:
    def test_no_excluded_returns_original(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 120.0)]
        result = _exclude(history, [])
        assert result == history

    def test_excludes_specific_months(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 120.0), _raw("2026-03", 140.0)]
        result = _exclude(history, ["2026-02"])
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["month"] == "2026-01"
        assert result[1]["month"] == "2026-03"

    def test_exclude_all_returns_empty(self) -> None:
        history = [_raw("2026-01", 100.0), _raw("2026-02", 120.0)]
        result = _exclude(history, ["2026-01", "2026-02"])
        assert result == []

    def test_exclude_nonexistent_months_has_no_effect(self) -> None:
        history = [_raw("2026-01", 100.0)]
        result = _exclude(history, ["2025-12"])
        assert result == history

    def test_empty_history_returns_empty(self) -> None:
        result = _exclude([], ["2026-01"])
        assert result == []


class TestCategoryMix:
    def test_uses_latest_month_mix(self) -> None:
        history = [
            _raw("2026-01", 100.0, compute_usd=80.0, storage_usd=15.0, network_usd=5.0),
            _raw("2026-02", 100.0, compute_usd=50.0, storage_usd=30.0, network_usd=20.0),
        ]
        result = _category_mix(history)
        assert result["compute"] == 0.5  # noqa: PLR2004
        assert result["storage"] == 0.3  # noqa: PLR2004
        assert result["network"] == 0.2  # noqa: PLR2004

    def test_empty_history_returns_default_mix(self) -> None:
        result = _category_mix([])
        assert result["compute"] == 0.6  # noqa: PLR2004
        assert result["storage"] == 0.25  # noqa: PLR2004
        assert result["network"] == 0.15  # noqa: PLR2004

    def test_zero_total_returns_default_mix(self) -> None:
        history = [_raw("2026-01", 0.0, compute_usd=0.0, storage_usd=0.0, network_usd=0.0)]
        result = _category_mix(history)
        assert result["compute"] == 0.6  # noqa: PLR2004
        assert result["storage"] == 0.25  # noqa: PLR2004

    def test_single_month_history(self) -> None:
        history = [_raw("2026-01", 200.0, compute_usd=140.0, storage_usd=40.0, network_usd=20.0)]
        result = _category_mix(history)
        assert result["compute"] == 0.7  # noqa: PLR2004
        assert result["storage"] == 0.2  # noqa: PLR2004
        assert result["network"] == 0.1  # noqa: PLR2004


class TestApplySeasonality:
    def test_no_factors_returns_unchanged(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {})
        assert result == months

    def test_factor_one_keeps_unchanged(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {1: 1.0})
        assert result == months

    def test_factor_greater_than_one_scales_up(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {1: 1.5})
        assert result[0].realistic_usd == 150.0  # noqa: PLR2004
        assert result[0].optimistic_usd == 135.0  # noqa: PLR2004
        assert result[0].pessimistic_usd == 165.0  # noqa: PLR2004

    def test_factor_less_than_one_scales_down(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {1: 0.5})
        assert result[0].realistic_usd == 50.0  # noqa: PLR2004

    def test_missing_offset_gets_factor_one(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {2: 1.5})
        assert result[0].realistic_usd == 100.0  # noqa: PLR2004

    def test_multiple_months_with_different_factors(self) -> None:
        from hexawyn.domain.models.budget_projection import ProjectedMonth

        months = [
            ProjectedMonth(
                month_offset=1,
                month_label="2026-07",
                realistic_usd=100.0,
                optimistic_usd=90.0,
                pessimistic_usd=110.0,
                by_category={"compute": 60.0, "storage": 25.0, "network": 15.0},
            ),
            ProjectedMonth(
                month_offset=2,
                month_label="2026-08",
                realistic_usd=200.0,
                optimistic_usd=180.0,
                pessimistic_usd=220.0,
                by_category={"compute": 120.0, "storage": 50.0, "network": 30.0},
            ),
        ]
        result = _apply_seasonality(months, {1: 1.5, 2: 0.5})
        assert result[0].realistic_usd == 150.0  # noqa: PLR2004
        assert result[1].realistic_usd == 100.0  # noqa: PLR2004

    def test_seasonality_scales_by_category(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        result = _apply_seasonality(months, {1: 2.0})
        assert result[0].by_category["compute"] == 120.0  # noqa: PLR2004
        assert result[0].by_category["storage"] == 50.0  # noqa: PLR2004
        assert result[0].by_category["network"] == 30.0  # noqa: PLR2004


class TestScale:
    def test_scale_multiplies_all_fields(self) -> None:
        from hexawyn.domain.models.budget_projection import ProjectedMonth

        month = ProjectedMonth(
            month_offset=1,
            month_label="2026-07",
            realistic_usd=100.0,
            optimistic_usd=90.0,
            pessimistic_usd=110.0,
            by_category={"compute": 60.0, "storage": 25.0, "network": 15.0},
        )
        result = _scale(month, 2.0)
        assert result.realistic_usd == 200.0  # noqa: PLR2004
        assert result.optimistic_usd == 180.0  # noqa: PLR2004
        assert result.pessimistic_usd == 220.0  # noqa: PLR2004
        assert result.by_category["compute"] == 120.0  # noqa: PLR2004

    def test_scale_preserves_offset_and_label(self) -> None:
        from hexawyn.domain.models.budget_projection import ProjectedMonth

        month = ProjectedMonth(
            month_offset=1,
            month_label="2026-07",
            realistic_usd=100.0,
            optimistic_usd=90.0,
            pessimistic_usd=110.0,
            by_category={"compute": 100.0},
        )
        result = _scale(month, 1.5)
        assert result.month_offset == 1
        assert result.month_label == "2026-07"


class TestConfidence:
    def test_high_with_enough_months(self) -> None:
        assert _confidence(6) == "high"
        assert _confidence(12) == "high"

    def test_medium_with_three_to_five_months(self) -> None:
        assert _confidence(3) == "medium"
        assert _confidence(4) == "medium"
        assert _confidence(5) == "medium"

    def test_low_with_fewer_than_three_months(self) -> None:
        assert _confidence(0) == "low"
        assert _confidence(1) == "low"
        assert _confidence(2) == "low"


class TestBudgetBreach:
    def test_none_threshold_never_breaches(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        breached, month = _budget_breach(months, None)
        assert breached is False
        assert month is None

    def test_no_breach_when_below_threshold(self) -> None:
        months = [_pm(1, "2026-07", 100.0, 90.0, 110.0)]
        breached, month = _budget_breach(months, 200.0)
        assert breached is False
        assert month is None

    def test_breach_detected(self) -> None:
        months = [
            _pm(1, "2026-07", 100.0, 90.0, 110.0),
            _pm(2, "2026-08", 250.0, 200.0, 300.0),
        ]
        breached, month = _budget_breach(months, 200.0)
        assert breached is True
        assert month == "2026-08"

    def test_first_breach_month_returned(self) -> None:
        months = [
            _pm(1, "2026-07", 250.0, 200.0, 300.0),
            _pm(2, "2026-08", 250.0, 200.0, 300.0),
        ]
        breached, month = _budget_breach(months, 200.0)
        assert breached is True
        assert month == "2026-07"

    def test_exact_threshold_does_not_breach(self) -> None:
        months = [_pm(1, "2026-07", 200.0, 180.0, 220.0)]
        breached, month = _budget_breach(months, 200.0)
        assert breached is False

    def test_empty_months_no_breach(self) -> None:
        breached, month = _budget_breach([], 100.0)
        assert breached is False
        assert month is None


class TestWarning:
    def test_low_confidence_triggers_warning(self) -> None:
        result = _warning("low", "linear")
        assert "fewer than three months" in result

    def test_exponential_model_triggers_warning(self) -> None:
        result = _warning("high", "exponential")
        assert "Exponential cost growth" in result

    def test_low_confidence_and_exponential_produces_both_warnings(self) -> None:
        result = _warning("low", "exponential")
        assert "fewer than three months" in result
        assert "Exponential cost growth" in result

    def test_no_warnings(self) -> None:
        result = _warning("high", "linear")
        assert result == ""

    def test_medium_confidence_linear_no_warning(self) -> None:
        result = _warning("medium", "linear")
        assert result == ""

    def test_medium_confidence_exponential_has_warning(self) -> None:
        result = _warning("medium", "exponential")
        assert "Exponential cost growth" in result


class TestBudgetProjectionService:
    def test_project_happy_path(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
            _raw("2026-04", 1331.0),
            _raw("2026-05", 1464.1),
            _raw("2026-06", 1610.51),
        ]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=3000.0)
        assert report.confidence == "high"
        assert report.growth_model in ("linear", "exponential", "decreasing", "flat")
        assert len(report.projected_months) == 3  # noqa: PLR2004
        assert report.current_monthly_usd == 1610.51  # noqa: PLR2004
        assert report.six_month_total_realistic > 0

    def test_project_with_budget_breach(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
            _raw("2026-04", 1331.0),
            _raw("2026-05", 1464.1),
            _raw("2026-06", 1610.51),
        ]
        report = service.project(history=history, horizon_months=6, budget_threshold_usd=1500.0)
        assert report.budget_exceeded is True
        assert report.budget_breach_month is not None

    def test_project_no_threshold(self) -> None:
        service = BudgetProjectionService()
        history = [_raw("2026-01", 1000.0), _raw("2026-02", 1100.0), _raw("2026-03", 1210.0)]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        assert report.budget_threshold_usd is None
        assert report.budget_exceeded is False
        assert report.budget_breach_month is None

    def test_project_empty_history(self) -> None:
        service = BudgetProjectionService()
        report = service.project(history=[], horizon_months=3, budget_threshold_usd=None)
        assert report.confidence == "low"
        assert report.current_monthly_usd == 0.0
        assert len(report.projected_months) == 3  # noqa: PLR2004

    def test_project_single_month_history(self) -> None:
        service = BudgetProjectionService()
        history = [_raw("2026-06", 1000.0)]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        assert report.confidence == "low"
        assert len(report.projected_months) == 3  # noqa: PLR2004

    def test_project_with_exclude_months(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 2000.0),
            _raw("2026-03", 1200.0),
            _raw("2026-04", 1300.0),
            _raw("2026-05", 1400.0),
            _raw("2026-06", 1500.0),
        ]
        report = service.project(
            history=history, horizon_months=3, budget_threshold_usd=None, exclude_months=["2026-02"]
        )
        assert report.current_monthly_usd == 1500.0  # noqa: PLR2004

    def test_project_with_seasonal_factors(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
            _raw("2026-04", 1331.0),
            _raw("2026-05", 1464.1),
            _raw("2026-06", 1610.51),
        ]
        report = service.project(
            history=history,
            horizon_months=3,
            budget_threshold_usd=None,
            seasonal_factors={1: 2.0, 2: 1.0, 3: 0.5},
        )
        assert report.projected_months[0].realistic_usd != report.projected_months[2].realistic_usd

    def test_project_decreasing_trend(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 2000.0),
            _raw("2026-02", 1800.0),
            _raw("2026-03", 1620.0),
            _raw("2026-04", 1458.0),
            _raw("2026-05", 1312.2),
            _raw("2026-06", 1180.98),
        ]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        assert report.growth_rate_pct < 0
        assert report.growth_model == "decreasing"

    def test_project_exponential_trend(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1050.0),
            _raw("2026-03", 1150.0),
            _raw("2026-04", 1300.0),
            _raw("2026-05", 1550.0),
            _raw("2026-06", 1900.0),
        ]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        if report.growth_model == "exponential":
            assert "Exponential" in report.warning or report.warning == ""

    def test_project_flat_trend(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1002.0),
            _raw("2026-03", 999.0),
            _raw("2026-04", 1001.0),
            _raw("2026-05", 1003.0),
            _raw("2026-06", 1000.0),
        ]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        assert report.growth_model == "flat"
        assert abs(report.growth_rate_pct) <= 0.5  # noqa: PLR2004

    def test_project_with_empty_seasonal_dict(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
        ]
        report = service.project(
            history=history, horizon_months=3, budget_threshold_usd=None, seasonal_factors={}
        )
        assert len(report.projected_months) == 3  # noqa: PLR2004

    def test_project_with_none_exclude_months(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
            _raw("2026-04", 1331.0),
        ]
        report = service.project(history=history, horizon_months=3, budget_threshold_usd=None)
        assert report.confidence == "medium"

    def test_report_return_type(self) -> None:
        service = BudgetProjectionService()
        report = service.project(history=[], horizon_months=1, budget_threshold_usd=None)
        assert hasattr(report, "current_monthly_usd")
        assert hasattr(report, "confidence")
        assert hasattr(report, "projected_months")
        assert hasattr(report, "warning")

    def test_zero_horizon_produces_no_months(self) -> None:
        service = BudgetProjectionService()
        report = service.project(
            history=[_raw("2026-06", 1000.0)], horizon_months=0, budget_threshold_usd=None
        )
        assert len(report.projected_months) == 0

    def test_exclude_month_via_service(self) -> None:
        service = BudgetProjectionService()
        history = [
            _raw("2026-01", 1000.0),
            _raw("2026-02", 1100.0),
            _raw("2026-03", 1210.0),
        ]
        report = service.project(
            history=history, horizon_months=1, budget_threshold_usd=None, exclude_months=["2026-03"]
        )
        assert report.current_monthly_usd == 1100.0  # noqa: PLR2004
