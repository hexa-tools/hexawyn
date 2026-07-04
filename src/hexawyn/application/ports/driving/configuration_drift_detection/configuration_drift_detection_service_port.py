from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_response import (
    ConfigurationDriftDetectionResponse,
)


class ConfigurationDriftDetectionServicePort(ABC):
    @abstractmethod
    def detect_drift(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse: ...
