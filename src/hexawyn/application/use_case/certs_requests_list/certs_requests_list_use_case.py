from __future__ import annotations

from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_command import (
    CertsRequestsListCommand,
)
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_response import (
    CertsRequestsListResponse,
)
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_service_port import (
    CertsRequestsListServicePort,
)


class CertsRequestsListUseCase:
    def __init__(self, service: CertsRequestsListServicePort) -> None:
        self._service = service

    def execute(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        return self._service.list_requests(command)
