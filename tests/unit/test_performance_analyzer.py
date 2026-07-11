from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import PerformanceMetricRaw


def _metric(name: str, before: float, after: float) -> PerformanceMetricRaw:
    return PerformanceMetricRaw(metric=name, before=before, after=after)


class TestLatencyMetrics:
    def test_latency_decrease_is_improvement(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("p99_latency_ms", 120.0, 95.0)])

        assert impacts[0].improved is True
        assert impacts[0].regressed is False

    def test_latency_increase_is_regression(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("p99_latency_ms", 95.0, 130.0)])

        assert impacts[0].improved is False
        assert impacts[0].regressed is True


class TestReliabilityMetrics:
    def test_uptime_increase_is_improvement(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("uptime_pct", 99.0, 99.9)])

        assert impacts[0].improved is True
        assert impacts[0].regressed is False

    def test_uptime_decrease_is_regression(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("uptime_pct", 99.9, 99.0)])

        assert impacts[0].regressed is True

    def test_error_rate_increase_is_regression(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("error_rate", 0.01, 0.05)])

        assert impacts[0].regressed is True


class TestNoChange:
    def test_equal_values_neither_improved_nor_regressed(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
        )

        impacts = analyze_performance([_metric("p99_latency_ms", 100.0, 100.0)])

        assert impacts[0].improved is False
        assert impacts[0].regressed is False


class TestHasRegression:
    def test_true_when_any_metric_regressed(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
            has_regression,
        )

        impacts = analyze_performance(
            [_metric("p99_latency_ms", 95.0, 130.0), _metric("uptime_pct", 99.0, 99.9)]
        )

        assert has_regression(impacts) is True

    def test_false_when_all_improved(self) -> None:
        from hexawyn.domain.services.optimization_roi.performance_analyzer import (
            analyze_performance,
            has_regression,
        )

        impacts = analyze_performance([_metric("p99_latency_ms", 120.0, 95.0)])

        assert has_regression(impacts) is False
