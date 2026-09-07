"""Unit tests for detect_pod_anomalies — pod metrics anomaly detection vs 7-day baseline.

Test data mirrors the ticket's own fixture: 20 pods in production, pod payment-api
normal CPU 200m, current 850m (325% above baseline).
"""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsRawData
from hexawyn.domain.models.event import EventSeverity
from hexawyn.domain.services.pod_anomaly_detection.detector import detect_pod_anomalies

_NAMESPACE = "production"
_WINDOW_HOURS = 168.0  # 7 days, 1 point/hour


def _flat_series(value: float, count: int, jitter: float = 2.0) -> list[float]:
    return [value + jitter * ((i % 3) - 1) for i in range(count)]


def _pod(  # noqa: PLR0913
    pod_name: str,
    *,
    pod_age_hours: float = 720.0,
    hours_since_last_restart: float | None = None,
    baseline_window_hours: float = _WINDOW_HOURS,
    cpu_baseline: list[float] | None = None,
    cpu_current: float = 200.0,
    memory_baseline: list[float] | None = None,
    memory_current: float = 500.0,
    error_rate_baseline: list[float] | None = None,
    error_rate_current: float = 0.1,
    is_scheduled_batch_job: bool = False,
) -> PodMetricsRawData:
    return PodMetricsRawData(
        pod_name=pod_name,
        namespace=_NAMESPACE,
        pod_age_hours=pod_age_hours,
        hours_since_last_restart=hours_since_last_restart,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline or _flat_series(200.0, 167),
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline or _flat_series(500.0, 167),
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline or _flat_series(0.1, 167, jitter=0.02),
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=is_scheduled_batch_job,
    )


class TestClearCpuSpike:
    """TC1: Pod using 3x its normal CPU → CRITICAL, Z-score > 5."""

    def test_payment_api_cpu_spike_is_critical(self) -> None:
        pod = _pod("payment-api", cpu_baseline=_flat_series(200.0, 167), cpu_current=850.0)

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        cpu_anomalies = [a for a in report.anomalies if a.metric == "cpu"]
        assert len(cpu_anomalies) == 1
        anomaly = cpu_anomalies[0]
        assert anomaly.severity == EventSeverity.CRITICAL
        assert anomaly.z_score is not None
        assert anomaly.z_score > 5.0  # noqa: PLR2004
        assert anomaly.deviation_pct == pytest.approx(325.0, rel=0.02)
        assert anomaly.detection_method in ("zscore", "both")


class TestGradualMemoryDrift:
    """TC2: gradual memory increase over 6h → Isolation Forest trend anomaly."""

    def test_gradual_drift_flagged_as_trend_anomaly(self) -> None:
        stable = _flat_series(500.0, 162)
        drift = [700.0, 750.0, 800.0, 850.0, 900.0]
        pod = _pod("worker-1", memory_baseline=stable + drift, memory_current=950.0)

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        memory_anomalies = [a for a in report.anomalies if a.metric == "memory"]
        assert len(memory_anomalies) == 1
        anomaly = memory_anomalies[0]
        assert anomaly.detection_method in ("isolation_forest", "both")
        assert anomaly.isolation_forest_score is not None


class TestCleanBaseline:
    """TC3: all pods within baseline range → clean 'no anomalies detected' report."""

    def test_all_pods_healthy_returns_clean_report(self) -> None:
        pods = [_pod(f"pod-{i}") for i in range(5)]

        report = detect_pod_anomalies(pods, baseline_window_days=7)

        assert report.anomalies == []
        assert "no anomal" in report.summary.lower()


class TestNewPodExcluded:
    """TC4: new pod with no baseline (deployed today) → excluded with a note."""

    def test_young_pod_excluded_from_comparison(self) -> None:
        young_pod = _pod("fresh-deploy", pod_age_hours=3.0)
        healthy_pod = _pod("stable-pod")

        report = detect_pod_anomalies([young_pod, healthy_pod], baseline_window_days=7)

        excluded_names = {excluded.pod_name for excluded in report.excluded_pods}
        assert "fresh-deploy" in excluded_names
        reason = next(e.reason for e in report.excluded_pods if e.pod_name == "fresh-deploy")
        assert "3.0h" in reason or "3h" in reason
        assert all(a.pod_name != "fresh-deploy" for a in report.anomalies)


class TestScheduledBatchJobEdgeCase:
    def test_batch_job_spike_capped_at_low_severity(self) -> None:
        pod = _pod(
            "nightly-report-job",
            cpu_baseline=_flat_series(200.0, 167),
            cpu_current=850.0,
            is_scheduled_batch_job=True,
        )

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        cpu_anomalies = [a for a in report.anomalies if a.metric == "cpu"]
        assert len(cpu_anomalies) == 1
        anomaly = cpu_anomalies[0]
        assert anomaly.severity == EventSeverity.LOW
        assert "batch" in anomaly.note.lower() or "cron" in anomaly.note.lower()


class TestRestartedPodEdgeCase:
    def test_baseline_limited_to_time_since_restart(self) -> None:
        stable_recent = _flat_series(200.0, 10)
        long_stale_history = _flat_series(200.0, 157)
        pod = _pod(
            "recently-restarted",
            hours_since_last_restart=10.0,
            cpu_baseline=long_stale_history + stable_recent,
            cpu_current=850.0,
        )

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        cpu_anomalies = [a for a in report.anomalies if a.metric == "cpu"]
        assert len(cpu_anomalies) == 1
        assert "restart" in cpu_anomalies[0].note.lower()


class TestEmptyInput:
    def test_no_pods_returns_empty_report(self) -> None:
        report = detect_pod_anomalies([], baseline_window_days=7)

        assert report.total_pods == 0
        assert report.anomalies == []
        assert report.excluded_pods == []


class TestSeverityTiers:
    """A 100-point alternating baseline makes the resulting Z-score (computed
    over baseline+current together, per ZScoreAnomalyDetector) numerically
    solvable for a target value — `current` is picked so the actual z lands
    precisely inside each severity band."""

    def test_zscore_between_4_and_5_is_high(self) -> None:
        baseline = [99.0, 101.0] * 50
        pod = _pod("mid-spike-pod", cpu_baseline=baseline, cpu_current=105.0959)

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        cpu_anomalies = [a for a in report.anomalies if a.metric == "cpu"]
        assert len(cpu_anomalies) == 1
        assert cpu_anomalies[0].severity == EventSeverity.HIGH

    def test_zscore_between_3_and_4_is_medium(self) -> None:
        baseline = [99.0, 101.0] * 50
        pod = _pod("small-spike-pod", cpu_baseline=baseline, cpu_current=103.7763)

        report = detect_pod_anomalies([pod], baseline_window_days=7)

        cpu_anomalies = [a for a in report.anomalies if a.metric == "cpu"]
        assert len(cpu_anomalies) == 1
        assert cpu_anomalies[0].severity == EventSeverity.MEDIUM
