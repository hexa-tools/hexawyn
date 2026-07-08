from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_response import (
    DetectUnintendedExternalExposureResponse,
)


class DetectUnintendedExternalExposureServicePort(ABC):
    @abstractmethod
    def detect_unintended_exposure(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse: ...
