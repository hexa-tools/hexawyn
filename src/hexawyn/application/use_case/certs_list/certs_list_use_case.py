from __future__ import annotations

from hexawyn.application.ports.driving.certs_list.certs_list_command import CertsListCommand
from hexawyn.application.ports.driving.certs_list.certs_list_response import CertsListResponse
from hexawyn.application.ports.driving.certs_list.certs_list_service_port import (
    CertsListServicePort,
)


class CertsListUseCase:
    def __init__(self, service: CertsListServicePort) -> None:
        self._service = service

    def execute(self, command: CertsListCommand) -> CertsListResponse:
        return self._service.list_certs(command)
