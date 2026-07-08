from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_command import (
    CertsRequestsListCommand,
)
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_response import (
    CertsRequestsListResponse,
)
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_service_port import (
    CertsRequestsListServicePort,
)


class CertsRequestsListService(CertsRequestsListServicePort):
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def list_requests(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])
