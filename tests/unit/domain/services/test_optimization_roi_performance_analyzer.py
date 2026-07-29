from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import PerformanceMetricRaw
from hexawyn.domain.models.optimization_roi import PerformanceImpact
from hexawyn.domain.services.optimization_roi.performance_analyzer import (
    _higher_is_better,
    _to_impact,
    analyze_performance,
    has_regression,
)


class TestHigherIsBetter:
    def test_uptime_is_higher_better(self) -> None:
        assert _higher_is_better("uptime") is True

    def test_availability_is_higher_better(self) -> None:
        assert _higher_is_better("availability_pct") is True

    def test_success_is_higher_better(self) -> None:
        assert _higher_is_better("success_rate") is True

    def test_latency_is_not_higher_better(self) -> None:
        assert _higher_is_better("p99_latency_ms") is False

    def test_error_rate_is_not_higher_better(self) -> None:
        assert _higher_is_better("error_rate") is False

    def test_case_insensitive(self) -> None:
        assert _higher_is_better("UPTIME_PCT") is True

    def test_unrelated_metric_is_not_higher_better(self) -> None:
        assert _higher_is_better("cpu_usage") is False


class TestToImpact:
    def test_improvement_when_lower_is_better(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "p99_latency_ms",
            "before": 120.0,
            "after": 95.0,
        }
        impact = _to_impact(metric)
        assert impact.improved is True
        assert impact.regressed is False

    def test_regression_when_lower_is_better(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "p99_latency_ms",
            "before": 95.0,
            "after": 120.0,
        }
        impact = _to_impact(metric)
        assert impact.improved is False
        assert impact.regressed is True

    def test_improvement_when_higher_is_better(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "uptime",
            "before": 99.5,
            "after": 99.9,
        }
        impact = _to_impact(metric)
        assert impact.improved is True
        assert impact.regressed is False

    def test_regression_when_higher_is_better(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "availability",
            "before": 99.9,
            "after": 99.5,
        }
        impact = _to_impact(metric)
        assert impact.improved is False
        assert impact.regressed is True

    def test_no_change(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "p99_latency_ms",
            "before": 100.0,
            "after": 100.0,
        }
        impact = _to_impact(metric)
        assert impact.improved is False
        assert impact.regressed is False

    def test_fields_preserved(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "error_rate",
            "before": 5.0,
            "after": 2.0,
        }
        impact = _to_impact(metric)
        assert impact.metric == "error_rate"
        assert impact.before == 5.0  # noqa: PLR2004
        assert impact.after == 2.0  # noqa: PLR2004

    def test_success_rate_higher_is_better_improved(self) -> None:
        metric: PerformanceMetricRaw = {
            "metric": "success_rate",
            "before": 95.0,
            "after": 99.0,
        }
        impact = _to_impact(metric)
        assert impact.improved is True


class TestAnalyzePerformance:
    def test_empty_metrics_returns_empty(self) -> None:
        result = analyze_performance([])
        assert result == []

    def test_single_metric(self) -> None:
        metrics: list[PerformanceMetricRaw] = [
            {"metric": "p99_latency_ms", "before": 200.0, "after": 150.0},
        ]
        result = analyze_performance(metrics)
        assert len(result) == 1
        assert isinstance(result[0], PerformanceImpact)

    def test_multiple_metrics(self) -> None:
        metrics: list[PerformanceMetricRaw] = [
            {"metric": "p99_latency_ms", "before": 200.0, "after": 150.0},
            {"metric": "uptime", "before": 99.0, "after": 99.5},
            {"metric": "error_rate", "before": 3.0, "after": 1.0},
        ]
        result = analyze_performance(metrics)
        assert len(result) == 3  # noqa: PLR2004


class TestHasRegression:
    def test_no_impacts_no_regression(self) -> None:
        assert has_regression([]) is False

    def test_all_improved_no_regression(self) -> None:
        impacts = [
            PerformanceImpact(
                metric="latency",
                before=100.0,
                after=80.0,
                improved=True,
                regressed=False,
            ),
            PerformanceImpact(
                metric="uptime", before=99.0, after=99.5, improved=True, regressed=False
            ),
        ]
        assert has_regression(impacts) is False

    def test_one_regression_detected(self) -> None:
        impacts = [
            PerformanceImpact(
                metric="latency",
                before=100.0,
                after=80.0,
                improved=True,
                regressed=False,
            ),
            PerformanceImpact(
                metric="error_rate",
                before=1.0,
                after=5.0,
                improved=False,
                regressed=True,
            ),
        ]
        assert has_regression(impacts) is True

    def test_all_regressed(self) -> None:
        impacts = [
            PerformanceImpact(
                metric="latency",
                before=80.0,
                after=100.0,
                improved=False,
                regressed=True,
            ),
            PerformanceImpact(
                metric="error_rate",
                before=1.0,
                after=3.0,
                improved=False,
                regressed=True,
            ),
        ]
        assert has_regression(impacts) is True
