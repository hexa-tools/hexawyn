from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_issuers_list.command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.certs_issuers_list.response import (
    CertsIssuersListResponse,
)
from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_service_port import (
    CertsIssuersListServicePort,
)


class CertsIssuersListService(CertsIssuersListServicePort):
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def list_issuers(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])
