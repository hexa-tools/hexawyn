from __future__ import annotations

from hexawyn.application.ports.driving.certs_detect.certs_detect_command import CertsDetectCommand
from hexawyn.application.ports.driving.certs_detect.certs_detect_response import CertsDetectResponse
from hexawyn.application.ports.driving.certs_detect.certs_detect_service_port import (
    CertsDetectServicePort,
)


class CertsDetectUseCase:
    def __init__(self, service: CertsDetectServicePort) -> None:
        self._service = service

    def execute(self, command: CertsDetectCommand) -> CertsDetectResponse:
        return self._service.detect(command)
