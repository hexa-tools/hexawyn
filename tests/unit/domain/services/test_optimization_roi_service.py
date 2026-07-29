from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRaw,
    PerformanceMetricRaw,
    SprintRoiData,
)
from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
    OptimizationRoiService,
)


def _roi_data(
    has_baseline: bool = True,
    baseline_eur: float = 1000.0,
    current_eur: float = 700.0,
    optimizations: list[OptimizationRaw] | None = None,
    performance_metrics: list[PerformanceMetricRaw] | None = None,
) -> SprintRoiData:
    return SprintRoiData(
        has_baseline=has_baseline,
        baseline_monthly_eur=baseline_eur,
        current_monthly_eur=current_eur,
        optimizations=optimizations or [],
        performance_metrics=performance_metrics or [],
    )


class TestOptimizationRoiService:
    def test_no_baseline_returns_warning(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(has_baseline=False)
        report = service.compute(data, 0.0)
        assert report.has_baseline is False
        assert "No pre-sprint cost baseline" in report.warning

    def test_computes_savings_with_baseline(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(has_baseline=True, baseline_eur=1000.0, current_eur=700.0)
        report = service.compute(data, 0.0)
        assert report.has_baseline is True
        assert report.monthly_saving_eur == 300.0  # noqa: PLR2004
        assert report.annual_saving_eur == 3600.0  # noqa: PLR2004
        assert report.savings_pct == 30.0  # noqa: PLR2004

    def test_with_traffic_growth(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(has_baseline=True, baseline_eur=1000.0, current_eur=1100.0)
        report = service.compute(data, 10.0)
        assert report.traffic_normalized is True
        assert report.traffic_growth_pct == 10.0  # noqa: PLR2004

    def test_top_optimization_set_when_present(self) -> None:
        service = OptimizationRoiService()
        optimizations: list[OptimizationRaw] = [
            {
                "name": "Big win",
                "category": "right_sizing",
                "monthly_saving_eur": 500.0,
                "description": "desc",
            },
            {
                "name": "Small fix",
                "category": "hpa_tuning",
                "monthly_saving_eur": 100.0,
                "description": "desc",
            },
        ]
        data = _roi_data(optimizations=optimizations)
        report = service.compute(data, 0.0)
        assert report.top_optimization is not None
        assert report.top_optimization.name == "Big win"

    def test_top_optimization_none_when_empty(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(optimizations=[])
        report = service.compute(data, 0.0)
        assert report.top_optimization is None

    def test_no_regression_no_warning(self) -> None:
        service = OptimizationRoiService()
        metrics: list[PerformanceMetricRaw] = [
            {"metric": "p99_latency_ms", "before": 120.0, "after": 95.0},
        ]
        data = _roi_data(performance_metrics=metrics)
        report = service.compute(data, 0.0)
        assert report.has_regression is False
        assert report.warning == ""

    def test_regression_adds_warning(self) -> None:
        service = OptimizationRoiService()
        metrics: list[PerformanceMetricRaw] = [
            {"metric": "p99_latency_ms", "before": 95.0, "after": 120.0},
        ]
        data = _roi_data(performance_metrics=metrics)
        report = service.compute(data, 0.0)
        assert report.has_regression is True
        assert "cost/performance trade-off" in report.warning

    def test_baseline_and_current_preserved(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(has_baseline=True, baseline_eur=1500.0, current_eur=900.0)
        report = service.compute(data, 0.0)
        assert report.baseline_monthly_eur == 1500.0  # noqa: PLR2004
        assert report.current_monthly_eur == 900.0  # noqa: PLR2004

    def test_performance_impacts_populated(self) -> None:
        service = OptimizationRoiService()
        metrics: list[PerformanceMetricRaw] = [
            {"metric": "p99_latency_ms", "before": 200.0, "after": 150.0},
            {"metric": "uptime", "before": 99.0, "after": 99.5},
        ]
        data = _roi_data(performance_metrics=metrics)
        report = service.compute(data, 0.0)
        assert len(report.performance_impacts) == 2  # noqa: PLR2004

    def test_savings_pct_when_no_savings(self) -> None:
        service = OptimizationRoiService()
        data = _roi_data(has_baseline=True, baseline_eur=1000.0, current_eur=1000.0)
        report = service.compute(data, 0.0)
        assert report.monthly_saving_eur == 0.0
        assert report.savings_pct == 0.0
