from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.response import (
    DetectUnintendedExternalExposureResponse,
)


class DetectUnintendedExternalExposureServicePort(ABC):
    @abstractmethod
    def detect_unintended_exposure(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse: ...
