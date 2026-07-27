from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRaw
from hexawyn.domain.services.optimization_roi.roi_calculator import (
    SavingsResult,
    _normalize,
    _pct,
    compute_savings,
    rank_optimizations,
)


class TestNormalize:
    def test_no_traffic_growth(self) -> None:
        assert _normalize(1000.0, 0.0) == 1000.0  # noqa: PLR2004

    def test_negative_growth_returns_current(self) -> None:
        assert _normalize(1000.0, -5.0) == 1000.0  # noqa: PLR2004

    def test_positive_growth_normalizes(self) -> None:
        result = _normalize(1100.0, 10.0)
        assert result == pytest.approx(1000.0)

    def test_fifty_percent_growth(self) -> None:
        result = _normalize(1500.0, 50.0)
        assert result == 1000.0  # noqa: PLR2004

    def test_hundred_percent_growth(self) -> None:
        result = _normalize(2000.0, 100.0)
        assert result == 1000.0  # noqa: PLR2004


class TestPct:
    def test_simple_pct(self) -> None:
        assert _pct(500.0, 1000.0) == 50.0  # noqa: PLR2004

    def test_zero_saving(self) -> None:
        assert _pct(0.0, 1000.0) == 0.0

    def test_zero_baseline(self) -> None:
        assert _pct(100.0, 0.0) == 0.0

    def test_negative_baseline(self) -> None:
        assert _pct(100.0, -10.0) == 0.0

    def test_full_savings(self) -> None:
        assert _pct(1000.0, 1000.0) == 100.0  # noqa: PLR2004

    def test_fractional_pct(self) -> None:
        result = _pct(1.0, 3.0)
        assert result == 33.3  # noqa: PLR2004


class TestComputeSavings:
    def test_simple_savings_no_traffic(self) -> None:
        result = compute_savings(1000.0, 700.0, 0.0)
        assert result.monthly_saving_eur == 300.0  # noqa: PLR2004
        assert result.annual_saving_eur == 3600.0  # noqa: PLR2004
        assert result.savings_pct == 30.0  # noqa: PLR2004
        assert result.traffic_normalized is False

    def test_savings_with_traffic_growth(self) -> None:
        result = compute_savings(1000.0, 1100.0, 10.0)
        assert result.traffic_normalized is True
        assert result.normalized_current_eur == 1000.0  # noqa: PLR2004

    def test_no_savings(self) -> None:
        result = compute_savings(1000.0, 1000.0, 0.0)
        assert result.monthly_saving_eur == 0.0
        assert result.annual_saving_eur == 0.0

    def test_negative_savings_means_cost_increased(self) -> None:
        result = compute_savings(1000.0, 1500.0, 0.0)
        assert result.monthly_saving_eur == -500.0  # noqa: PLR2004

    def test_savingsresult_is_frozen(self) -> None:
        result = compute_savings(1000.0, 500.0, 0.0)
        assert isinstance(result, SavingsResult)

    def test_normalized_current_rounded(self) -> None:
        result = compute_savings(1000.0, 1066.0, 10.0)
        assert result.normalized_current_eur == round(1066.0 / (1 + 10.0 / 100), 2)

    def test_zero_baseline(self) -> None:
        result = compute_savings(0.0, 100.0, 0.0)
        assert result.savings_pct == 0.0


class TestRankOptimizations:
    def test_sorts_by_monthly_saving_desc(self) -> None:
        raw: list[OptimizationRaw] = [
            {
                "name": "Small fix",
                "category": "right_sizing",
                "monthly_saving_eur": 50.0,
                "description": "desc",
            },
            {
                "name": "Big win",
                "category": "idle_pod_removal",
                "monthly_saving_eur": 500.0,
                "description": "desc",
            },
            {
                "name": "Medium fix",
                "category": "hpa_tuning",
                "monthly_saving_eur": 200.0,
                "description": "desc",
            },
        ]
        result = rank_optimizations(raw)
        assert result[0].name == "Big win"
        assert result[1].name == "Medium fix"
        assert result[2].name == "Small fix"

    def test_empty_list(self) -> None:
        result = rank_optimizations([])
        assert result == []

    def test_single_item(self) -> None:
        raw: list[OptimizationRaw] = [
            {
                "name": "Only one",
                "category": "other",
                "monthly_saving_eur": 100.0,
                "description": "desc",
            },
        ]
        result = rank_optimizations(raw)
        assert len(result) == 1
        assert result[0].name == "Only one"

    def test_equal_savings_preserves_order(self) -> None:
        raw: list[OptimizationRaw] = [
            {
                "name": "First",
                "category": "right_sizing",
                "monthly_saving_eur": 100.0,
                "description": "",
            },
            {
                "name": "Second",
                "category": "right_sizing",
                "monthly_saving_eur": 100.0,
                "description": "",
            },
        ]
        result = rank_optimizations(raw)
        assert result[0].name == "First"
        assert result[1].name == "Second"

    def test_fields_preserved(self) -> None:
        raw: list[OptimizationRaw] = [
            {
                "name": "Fix",
                "category": "storage_cleanup",
                "monthly_saving_eur": 300.0,
                "description": "Cleaned up PVs",
            },
        ]
        result = rank_optimizations(raw)
        assert result[0].category == "storage_cleanup"
        assert result[0].monthly_saving_eur == 300.0  # noqa: PLR2004
        assert result[0].description == "Cleaned up PVs"

    def test_missing_description_defaults_to_empty(self) -> None:
        raw: list[OptimizationRaw] = [
            {"name": "Fix", "category": "other", "monthly_saving_eur": 100.0},
        ]
        result = rank_optimizations(raw)
        assert result[0].description == ""
