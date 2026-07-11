from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRaw


def _opt(name: str, saving: float, category: str = "right_sizing") -> OptimizationRaw:
    return OptimizationRaw(name=name, category=category, monthly_saving_eur=saving, description="")


class TestSavings:
    def test_monthly_and_annual_savings(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import compute_savings

        result = compute_savings(baseline=500.0, current=150.0, traffic_growth_pct=0.0)

        assert result.monthly_saving_eur == 350.0
        assert result.annual_saving_eur == 4200.0
        assert result.savings_pct == 70.0

    def test_zero_savings_when_no_change(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import compute_savings

        result = compute_savings(baseline=500.0, current=500.0, traffic_growth_pct=0.0)

        assert result.monthly_saving_eur == 0.0
        assert result.savings_pct == 0.0

    def test_zero_baseline_yields_zero_pct(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import compute_savings

        result = compute_savings(baseline=0.0, current=0.0, traffic_growth_pct=0.0)

        assert result.savings_pct == 0.0
        assert result.monthly_saving_eur == 0.0


class TestTrafficNormalization:
    def test_normalizes_current_cost_against_traffic_growth(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import compute_savings

        # Traffic grew 20%; without it current would have been 150/1.2 = 125.
        result = compute_savings(baseline=500.0, current=150.0, traffic_growth_pct=20.0)

        assert result.traffic_normalized is True
        assert result.normalized_current_eur == 125.0
        assert result.monthly_saving_eur == 375.0

    def test_no_normalization_when_zero_growth(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import compute_savings

        result = compute_savings(baseline=500.0, current=150.0, traffic_growth_pct=0.0)

        assert result.traffic_normalized is False
        assert result.normalized_current_eur == 150.0


class TestRanking:
    def test_optimizations_sorted_by_saving_desc(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import rank_optimizations

        ranked = rank_optimizations([_opt("a", 100.0), _opt("b", 350.0), _opt("c", 50.0)])

        assert [item.name for item in ranked] == ["b", "a", "c"]
        assert ranked[0].monthly_saving_eur == 350.0

    def test_empty_list_returns_empty(self) -> None:
        from hexawyn.domain.services.optimization_roi.roi_calculator import rank_optimizations

        assert rank_optimizations([]) == []
