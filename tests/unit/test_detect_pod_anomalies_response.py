from __future__ import annotations

from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_response import (
    DetectPodAnomaliesResponse,
)


class TestDetectPodAnomaliesResponse:
    def test_defaults(self) -> None:
        response = DetectPodAnomaliesResponse()
        assert response.total_pods == 0
        assert response.anomalies == []
        assert response.excluded_pods == []
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = DetectPodAnomaliesResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
