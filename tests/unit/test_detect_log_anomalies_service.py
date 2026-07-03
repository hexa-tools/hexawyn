"""Unit tests for DetectLogAnomaliesService (mocks PodLogsPort — no real cluster)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.service.detect_log_anomalies_service import DetectLogAnomaliesService
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


def _line(minute: str, message: str = "heartbeat ok") -> PodLogLine:
    return PodLogLine(
        timestamp=f"2024-01-01T09:{minute}:00Z",
        level="INFO",
        message=message,
        run_index=0,
        is_json=False,
    )


class TestDetectLogAnomaliesService:
    def test_detect_returns_response_from_domain_computation(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = [_line(f"{m:02d}") for m in range(20) for _ in range(5)]
        service = DetectLogAnomaliesService(port=port)
        command = DetectLogAnomaliesCommand(pod_name="inventory-service", namespace="prod")

        response = service.detect(command)

        assert response.pod_name == "inventory-service"
        assert response.namespace == "prod"
        assert response.total_lines == 100
        assert response.summary == "no anomalies detected"
        port.fetch_logs.assert_called_once()

    def test_detect_maps_anomalies_to_dicts(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = [_line("00")] * 42
        service = DetectLogAnomaliesService(port=port)
        command = DetectLogAnomaliesCommand(pod_name="p", namespace="n")

        response = service.detect(command)

        assert response.insufficient_data is True
        assert response.anomalies == []

    def test_response_anomaly_dict_shape_for_volume_spike(self) -> None:
        """TC1 through the service layer: spike minute maps to a volume anomaly dict."""
        port = MagicMock()
        lines = [_line(f"{minute:02d}") for minute in range(10, 30) for _ in range(5)]
        lines += [_line("32") for _ in range(50)]
        port.fetch_logs.return_value = lines
        service = DetectLogAnomaliesService(port=port)

        response = service.detect(DetectLogAnomaliesCommand(pod_name="p", namespace="n"))

        assert len(response.anomalies) == 1
        anomaly = response.anomalies[0]
        assert anomaly["type"] == "volume"
        assert anomaly["timestamp"] == "2024-01-01T09:32"
        assert anomaly["anomaly_score"] > 3.0
        assert anomaly["low_confidence"] is False
