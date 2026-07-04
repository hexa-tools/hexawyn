from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_response import (
    ConfigurationDriftDetectionResponse,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_service_port import (
    ConfigurationDriftDetectionServicePort,
)
from hexawyn.application.use_case.configuration_drift_detection.configuration_drift_detection_use_case import (
    ConfigurationDriftDetectionUseCase,
)


class TestConfigurationDriftDetectionUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ConfigurationDriftDetectionServicePort)
        expected = ConfigurationDriftDetectionResponse(summary="All in sync.")
        service.detect_drift.return_value = expected
        use_case = ConfigurationDriftDetectionUseCase(service=service)
        command = ConfigurationDriftDetectionCommand(namespace="production")

        result = use_case.execute(command)

        service.detect_drift.assert_called_once_with(command)
        assert result is expected
