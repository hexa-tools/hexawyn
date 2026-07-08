"""Unit tests for DetectPodAnomaliesService (mocks PodMetricsBaselinePort + K8sPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.service.detect_pod_anomalies_service import DetectPodAnomaliesService
from hexawyn.domain.errors import ResourceNotFoundError


def _pod(name: str, current: float = 200.0, pod_age_hours: float = 720.0) -> dict:
    baseline = [200.0 + ((i % 3) - 1) * 2.0 for i in range(167)]
    return {
        "pod_name": name,
        "namespace": "production",
        "pod_age_hours": pod_age_hours,
        "hours_since_last_restart": None,
        "baseline_window_hours": 168.0,
        "cpu_baseline_millicores": baseline,
        "cpu_current_millicores": current,
        "memory_baseline_bytes": [500.0] * 167,
        "memory_current_bytes": 500.0,
        "error_rate_baseline_pct": [0.1] * 167,
        "error_rate_current_pct": 0.1,
        "is_scheduled_batch_job": False,
    }


def _make_service(
    port: MagicMock | None = None, k8s_port: MagicMock | None = None
) -> DetectPodAnomaliesService:
    if port is None:
        port = MagicMock()
        port.get_all_pod_metrics_data.return_value = []
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "100d"}
        ]
    return DetectPodAnomaliesService(port=port, k8s_port=k8s_port)


class TestNamespaceValidation:
    def test_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        service = _make_service(k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.detect(DetectPodAnomaliesCommand(namespace="ghost"))


class TestBulkFetch:
    def test_calls_port_once_in_bulk(self) -> None:
        port = MagicMock()
        port.get_all_pod_metrics_data.return_value = [_pod("payment-api", current=850.0)]
        service = _make_service(port=port)

        response = service.detect(
            DetectPodAnomaliesCommand(namespace="production", baseline_window_days=7)
        )

        port.get_all_pod_metrics_data.assert_called_once_with(namespace="production", window_days=7)
        assert response.error is None
        assert response.total_pods == 1
        assert len(response.anomalies) == 1
        assert response.anomalies[0]["pod_name"] == "payment-api"
        assert response.anomalies[0]["severity"] == "critical"

    def test_clean_report_maps_to_empty_anomalies(self) -> None:
        port = MagicMock()
        port.get_all_pod_metrics_data.return_value = [_pod("healthy-pod")]
        service = _make_service(port=port)

        response = service.detect(DetectPodAnomaliesCommand(namespace="production"))

        assert response.anomalies == []
        assert "no anomal" in response.summary.lower()

    def test_excluded_pod_maps_to_excluded_pods_dict(self) -> None:
        port = MagicMock()
        port.get_all_pod_metrics_data.return_value = [_pod("fresh-deploy", pod_age_hours=3.0)]
        service = _make_service(port=port)

        response = service.detect(DetectPodAnomaliesCommand(namespace="production"))

        assert len(response.excluded_pods) == 1
        assert response.excluded_pods[0]["pod_name"] == "fresh-deploy"
        assert "no baseline" in response.excluded_pods[0]["reason"]
