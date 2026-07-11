from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw


def _month(
    label: str, total: float, mix: tuple[float, float, float] = (0.6, 0.25, 0.15)
) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=label,
        total_usd=total,
        compute_usd=total * mix[0],
        storage_usd=total * mix[1],
        network_usd=total * mix[2],
    )


def _steady_12pct(count: int, start: float = 8000.0) -> list[MonthlyCostRaw]:
    history: list[MonthlyCostRaw] = []
    value = start
    for index in range(count):
        history.append(_month(f"2026-{index + 1:02d}", round(value, 2)))
        value *= 1.12
    return history


class TestProjection:
    def test_six_months_projected(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=_steady_12pct(6), horizon_months=6, budget_threshold_usd=None
        )

        assert len(report.projected_months) == 6
        assert report.growth_rate_pct > 0
        assert report.six_month_total_realistic > 0

    def test_steady_growth_upward_trend(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=_steady_12pct(6), horizon_months=6, budget_threshold_usd=None
        )

        realistic = [m.realistic_usd for m in report.projected_months]
        assert realistic == sorted(realistic)

    def test_decreasing_costs_show_savings(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        history = [
            _month("2026-01", 10000.0),
            _month("2026-02", 9000.0),
            _month("2026-03", 8100.0),
        ]

        report = BudgetProjectionService().project(
            history=history, horizon_months=6, budget_threshold_usd=None
        )

        assert report.growth_model == "decreasing"
        assert report.projected_months[5].realistic_usd < report.current_monthly_usd


class TestConfidence:
    def test_low_confidence_with_scarce_data(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=[_month("2026-01", 8000.0)], horizon_months=6, budget_threshold_usd=None
        )

        assert report.confidence == "low"
        assert report.warning != ""

    def test_high_confidence_with_ample_data(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=_steady_12pct(6), horizon_months=6, budget_threshold_usd=None
        )

        assert report.confidence == "high"


class TestExponentialWarning:
    def test_exponential_growth_flags_warning(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        history = [
            _month("2026-01", 8000.0),
            _month("2026-02", 9600.0),
            _month("2026-03", 12480.0),
            _month("2026-04", 17472.0),
        ]

        report = BudgetProjectionService().project(
            history=history, horizon_months=6, budget_threshold_usd=None
        )

        assert report.growth_model == "exponential"
        assert "exponential" in report.warning.lower()


class TestBudgetThreshold:
    def test_budget_exceeded_flags_breach_month(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=_steady_12pct(6), horizon_months=6, budget_threshold_usd=12000.0
        )

        assert report.budget_exceeded is True
        assert report.budget_breach_month is not None

    def test_budget_not_exceeded(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=_steady_12pct(6), horizon_months=6, budget_threshold_usd=1_000_000.0
        )

        assert report.budget_exceeded is False
        assert report.budget_breach_month is None


class TestExcludeAnomalousPeriod:
    def test_excluded_months_ignored(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        history = _steady_12pct(5)
        history.append(_month("2026-06", 40000.0))  # anomalous new-cluster spike

        report = BudgetProjectionService().project(
            history=history,
            horizon_months=6,
            budget_threshold_usd=None,
            exclude_months=["2026-06"],
        )

        assert report.growth_rate_pct < 20


class TestSeasonality:
    def test_seasonal_factor_applied(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        history = _steady_12pct(6)

        base = BudgetProjectionService().project(
            history=history, horizon_months=6, budget_threshold_usd=None
        )
        seasonal = BudgetProjectionService().project(
            history=history,
            horizon_months=6,
            budget_threshold_usd=None,
            seasonal_factors={5: 1.5},
        )

        assert seasonal.projected_months[4].realistic_usd > base.projected_months[4].realistic_usd


class TestDegenerateHistory:
    def test_all_history_excluded_uses_defaults(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        report = BudgetProjectionService().project(
            history=[_month("2026-06", 8000.0)],
            horizon_months=6,
            budget_threshold_usd=None,
            exclude_months=["2026-06"],
        )

        assert report.current_monthly_usd == 0.0
        assert report.growth_model == "flat"

    def test_zero_total_months_stay_flat(self) -> None:
        from hexawyn.domain.services.budget_projection.budget_projection_service import (
            BudgetProjectionService,
        )

        history = [_month("2026-01", 0.0), _month("2026-02", 0.0)]

        report = BudgetProjectionService().project(
            history=history, horizon_months=3, budget_threshold_usd=None
        )

        assert report.growth_model == "flat"
        assert report.growth_rate_pct == 0.0
