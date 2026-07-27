from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.configuration_drift_detection.command import (  # noqa: E501
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
    ConfigurationDriftDetectionResponse,
)


class ConfigurationDriftDetectionServicePort(ABC):
    @abstractmethod
    def detect_drift(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse: ...
