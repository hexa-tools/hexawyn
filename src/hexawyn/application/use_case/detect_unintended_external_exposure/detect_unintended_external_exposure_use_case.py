from __future__ import annotations

from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_response import (
    DetectUnintendedExternalExposureResponse,
)
from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_service_port import (
    DetectUnintendedExternalExposureServicePort,
)


class DetectUnintendedExternalExposureUseCase:
    def __init__(self, service: DetectUnintendedExternalExposureServicePort) -> None:
        self._svc = service

    def execute(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        return self._svc.detect_unintended_exposure(command)
