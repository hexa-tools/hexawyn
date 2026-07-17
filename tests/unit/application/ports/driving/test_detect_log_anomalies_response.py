from __future__ import annotations

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_response import (
    DetectLogAnomaliesResponse,
)


class TestDetectLogAnomaliesResponse:
    def test_defaults(self) -> None:
        response = DetectLogAnomaliesResponse()
        assert response.total_lines == 0
        assert response.anomalies == []
        assert response.insufficient_data is False
        assert response.error is None

    def test_error_field(self) -> None:
        response = DetectLogAnomaliesResponse(error="Pod not found")
        assert response.error == "Pod not found"
