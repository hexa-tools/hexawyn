from __future__ import annotations

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_response import (
    ConfigurationDriftDetectionResponse,
)


class TestConfigurationDriftDetectionResponse:
    def test_defaults(self) -> None:
        response = ConfigurationDriftDetectionResponse()

        assert response.drifted_resources == []
        assert response.drifted_by_namespace == {}
        assert response.in_sync_count == 0
        assert response.excluded_resources == []
        assert response.total_checked == 0
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = ConfigurationDriftDetectionResponse(error="helm not found")

        assert response.error == "helm not found"
