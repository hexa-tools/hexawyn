from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw


def _month(label: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=label,
        total_usd=total,
        compute_usd=total * 0.6,
        storage_usd=total * 0.25,
        network_usd=total * 0.15,
    )


class TestGrowthRate:
    def test_steady_twelve_percent_monthly(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [
            _month("2026-01", 8000.0),
            _month("2026-02", 8960.0),
            _month("2026-03", 10035.0),
        ]

        result = estimate_growth(history)

        assert 11.5 <= result.monthly_rate_pct <= 12.5
        assert result.model in ("linear", "exponential")

    def test_flat_costs_zero_growth(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [_month("2026-01", 8000.0), _month("2026-02", 8000.0), _month("2026-03", 8000.0)]

        result = estimate_growth(history)

        assert result.monthly_rate_pct == 0.0
        assert result.model == "flat"


class TestGrowthModel:
    def test_decreasing_costs_detected(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [
            _month("2026-01", 10000.0),
            _month("2026-02", 9000.0),
            _month("2026-03", 8100.0),
        ]

        result = estimate_growth(history)

        assert result.model == "decreasing"
        assert result.monthly_rate_pct < 0

    def test_exponential_acceleration_detected(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [
            _month("2026-01", 8000.0),
            _month("2026-02", 9600.0),
            _month("2026-03", 12480.0),
            _month("2026-04", 17472.0),
        ]

        result = estimate_growth(history)

        assert result.model == "exponential"
        assert result.monthly_rate_pct > 0

    def test_linear_steady_growth(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [
            _month("2026-01", 8000.0),
            _month("2026-02", 8500.0),
            _month("2026-03", 9000.0),
            _month("2026-04", 9500.0),
        ]

        result = estimate_growth(history)

        assert result.model == "linear"


class TestEdgeCases:
    def test_single_month_is_flat_zero(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        result = estimate_growth([_month("2026-01", 8000.0)])

        assert result.monthly_rate_pct == 0.0
        assert result.model == "flat"

    def test_empty_history_is_flat_zero(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        result = estimate_growth([])

        assert result.monthly_rate_pct == 0.0
        assert result.model == "flat"
        assert result.current_monthly_usd == 0.0

    def test_current_monthly_is_last_month(self) -> None:
        from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth

        history = [_month("2026-01", 8000.0), _month("2026-02", 9000.0)]

        result = estimate_growth(history)

        assert result.current_monthly_usd == 9000.0
