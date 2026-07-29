from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.response import (
    CertsIssuersListResponse,
)


class CertsIssuersListUseCase:
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def execute(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])
