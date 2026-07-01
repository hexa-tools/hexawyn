from __future__ import annotations

from hexawyn.application.ports.driving.certs_get.certs_get_command import CertsGetCommand
from hexawyn.application.ports.driving.certs_get.certs_get_response import CertsGetResponse
from hexawyn.application.ports.driving.certs_get.certs_get_service_port import CertsGetServicePort


class CertsGetUseCase:
    def __init__(self, service: CertsGetServicePort) -> None:
        self._service = service

    def execute(self, command: CertsGetCommand) -> CertsGetResponse:
        return self._service.get_cert(command)
