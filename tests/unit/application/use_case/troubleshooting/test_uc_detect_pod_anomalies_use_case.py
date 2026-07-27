from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.detect_pod_anomalies_use_case import (  # noqa: E501
    DetectPodAnomaliesUseCase,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.response import (  # noqa: E501
    DetectPodAnomaliesResponse,
)


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

        assert len(result.anomalies) == 0
