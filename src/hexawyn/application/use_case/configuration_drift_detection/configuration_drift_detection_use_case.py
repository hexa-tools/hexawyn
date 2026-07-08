from __future__ import annotations

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_response import (
    ConfigurationDriftDetectionResponse,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_service_port import (
    ConfigurationDriftDetectionServicePort,
)


class ConfigurationDriftDetectionUseCase:
    def __init__(self, service: ConfigurationDriftDetectionServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        return self._svc.detect_drift(command)
