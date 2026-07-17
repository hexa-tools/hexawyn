from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRaw,
    PerformanceMetricRaw,
    SprintRoiData,
)


def _opt(name: str, saving: float, category: str = "right_sizing") -> OptimizationRaw:
    return OptimizationRaw(name=name, category=category, monthly_saving_eur=saving, description="")


def _metric(name: str, before: float, after: float) -> PerformanceMetricRaw:
    return PerformanceMetricRaw(metric=name, before=before, after=after)


def _data(
    has_baseline: bool = True,
    baseline: float = 500.0,
    current: float = 150.0,
    optimizations: list[OptimizationRaw] | None = None,
    metrics: list[PerformanceMetricRaw] | None = None,
) -> SprintRoiData:
    return SprintRoiData(
        has_baseline=has_baseline,
        baseline_monthly_eur=baseline,
        current_monthly_eur=current,
        optimizations=optimizations if optimizations is not None else [_opt("rs", 350.0)],
        performance_metrics=metrics if metrics is not None else [],
    )


class TestHappyPath:
    def test_three_optimizations_combined_roi(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        data = _data(
            optimizations=[
                _opt("right-size", 200.0),
                _opt("idle-removal", 100.0, "idle_pod_removal"),
                _opt("hpa-tune", 50.0, "hpa_tuning"),
            ]
        )

        report = OptimizationRoiService().compute(data, traffic_growth_pct=0.0)

        assert report.monthly_saving_eur == 350.0
        assert report.annual_saving_eur == 4200.0
        assert len(report.optimizations) == 3
        assert report.top_optimization is not None
        assert report.top_optimization.name == "right-size"

    def test_ticket_scenario_500_to_150(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        report = OptimizationRoiService().compute(_data(), traffic_growth_pct=0.0)

        assert report.baseline_monthly_eur == 500.0
        assert report.current_monthly_eur == 150.0
        assert report.savings_pct == 70.0


class TestTradeOff:
    def test_cost_down_latency_up_flags_regression(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        data = _data(metrics=[_metric("p99_latency_ms", 95.0, 130.0)])

        report = OptimizationRoiService().compute(data, traffic_growth_pct=0.0)

        assert report.has_regression is True
        assert "trade-off" in report.warning.lower() or "regress" in report.warning.lower()


class TestNoBaseline:
    def test_missing_baseline_returns_error_report(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        report = OptimizationRoiService().compute(_data(has_baseline=False), traffic_growth_pct=0.0)

        assert report.has_baseline is False
        assert "baseline" in report.warning.lower()
        assert report.monthly_saving_eur == 0.0
        assert report.optimizations == []


class TestZeroRoi:
    def test_zero_savings_honest_report(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        data = _data(baseline=500.0, current=500.0, optimizations=[])

        report = OptimizationRoiService().compute(data, traffic_growth_pct=0.0)

        assert report.has_baseline is True
        assert report.monthly_saving_eur == 0.0
        assert report.savings_pct == 0.0
        assert report.top_optimization is None


class TestTrafficNormalization:
    def test_traffic_growth_normalizes_savings(self) -> None:
        from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
            OptimizationRoiService,
        )

        report = OptimizationRoiService().compute(_data(), traffic_growth_pct=20.0)

        assert report.traffic_normalized is True
        assert report.traffic_growth_pct == 20.0
        assert report.monthly_saving_eur == 375.0
