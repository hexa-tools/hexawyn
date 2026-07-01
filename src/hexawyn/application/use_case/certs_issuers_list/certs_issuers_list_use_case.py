from __future__ import annotations

from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_command import (
    CertsIssuersListCommand,
)
from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_response import (
    CertsIssuersListResponse,
)
from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_service_port import (
    CertsIssuersListServicePort,
)


class CertsIssuersListUseCase:
    def __init__(self, service: CertsIssuersListServicePort) -> None:
        self._service = service

    def execute(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        return self._service.list_issuers(command)
