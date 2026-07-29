from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.detect_pod_anomalies_use_case import (  # noqa: E501
    DetectPodAnomaliesUseCase,
    _to_anomaly_dict,
    _to_excluded_dict,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.response import (  # noqa: E501
    DetectPodAnomaliesResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.event import EventSeverity
from hexawyn.domain.models.pod_anomaly import ExcludedPod, PodAnomaly


class TestDetectPodAnomaliesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pod_metrics_baseline.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = DetectPodAnomaliesUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(DetectPodAnomaliesCommand(namespace="default"))

        assert isinstance(result, DetectPodAnomaliesResponse)

    def test_execute_with_no_pods_returns_empty_anomalies(self) -> None:
        port = MagicMock()
        port.get_pod_metrics_baseline.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = DetectPodAnomaliesUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(DetectPodAnomaliesCommand(namespace="default"))

        assert len(result.anomalies) == 0  # noqa: PLR2004

    def test_execute_raises_when_namespace_not_found(self) -> None:
        port = MagicMock()
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "other-ns", "status": "Active", "age": "30d"},
        ]

        use_case = DetectPodAnomaliesUseCase(port=port, k8s_port=k8s)

        with pytest.raises(ResourceNotFoundError, match="not found"):
            use_case.execute(DetectPodAnomaliesCommand(namespace="missing-ns"))


class TestMapperFunctions:
    def test_to_anomaly_dict_converts_pod_anomaly(self) -> None:
        anomaly = PodAnomaly(
            pod_name="api-pod",
            namespace="default",
            metric="cpu",
            severity=EventSeverity.HIGH,
            deviation_pct=250.0,
            z_score=3.2,
            isolation_forest_score=-1.5,
            detection_method="both",
            current_value=800.0,
            baseline_mean=230.0,
            note="Spiking CPU usage",
        )

        result = _to_anomaly_dict(anomaly)

        assert result["pod_name"] == "api-pod"
        assert result["namespace"] == "default"
        assert result["severity"] == "high"
        assert result["deviation_pct"] == 250.0  # noqa: PLR2004
        assert result["z_score"] == 3.2  # noqa: PLR2004
        assert result["note"] == "Spiking CPU usage"

    def test_to_excluded_dict_converts_excluded_pod(self) -> None:
        excluded = ExcludedPod(
            pod_name="short-lived-pod",
            namespace="default",
            reason="Insufficient baseline data",
        )

        result = _to_excluded_dict(excluded)

        assert result["pod_name"] == "short-lived-pod"
        assert result["namespace"] == "default"
        assert result["reason"] == "Insufficient baseline data"
