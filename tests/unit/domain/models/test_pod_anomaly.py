"""Unit tests for pod anomaly detection domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.event import EventSeverity
from hexawyn.domain.models.pod_anomaly import (
    ExcludedPod,
    PodAnomaly,
    PodAnomalyDetectionReport,
    PodAnomalyDetectionRequest,
)


class TestPodAnomaly:
    def test_fields(self) -> None:
        anomaly = PodAnomaly(
            pod_name="payment-api-abc",
            namespace="production",
            metric="cpu",
            severity=EventSeverity.CRITICAL,
            deviation_pct=325.0,
            z_score=6.2,
            isolation_forest_score=None,
            detection_method="zscore",
            current_value=850.0,
            baseline_mean=200.0,
        )
        assert anomaly.severity == EventSeverity.CRITICAL
        assert anomaly.deviation_pct == 325.0  # noqa: PLR2004
        assert anomaly.note == ""


class TestExcludedPod:
    def test_fields(self) -> None:
        excluded = ExcludedPod(
            pod_name="new-pod-xyz", namespace="production", reason="no baseline: too young"
        )
        assert excluded.pod_name == "new-pod-xyz"
        assert "too young" in excluded.reason


class TestPodAnomalyDetectionRequest:
    def test_defaults(self) -> None:
        request = PodAnomalyDetectionRequest(namespace="production")
        assert request.baseline_window_days == 7  # noqa: PLR2004

    def test_custom_window(self) -> None:
        request = PodAnomalyDetectionRequest(namespace="production", baseline_window_days=14)
        assert request.baseline_window_days == 14  # noqa: PLR2004


class TestPodAnomalyDetectionReport:
    def test_defaults(self) -> None:
        report = PodAnomalyDetectionReport(namespace="production", total_pods=20)
        assert report.anomalies == []
        assert report.excluded_pods == []
        assert report.summary == ""

    def test_with_anomalies(self) -> None:
        anomaly = PodAnomaly(
            pod_name="payment-api-abc",
            namespace="production",
            metric="cpu",
            severity=EventSeverity.CRITICAL,
            deviation_pct=325.0,
            z_score=6.2,
            isolation_forest_score=None,
            detection_method="zscore",
            current_value=850.0,
            baseline_mean=200.0,
        )
        report = PodAnomalyDetectionReport(
            namespace="production", total_pods=20, anomalies=[anomaly]
        )
        assert len(report.anomalies) == 1
        assert report.anomalies[0].pod_name == "payment-api-abc"
