from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_list.command import CertsListCommand
from hexawyn.application.use_case.cert_manager.certs_list.response import CertsListResponse


class CertsListUseCase:
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def execute(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=[asdict(c) for c in certs])
