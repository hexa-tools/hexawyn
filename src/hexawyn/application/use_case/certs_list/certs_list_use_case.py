from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_list.command import CertsListCommand
from hexawyn.application.use_case.certs_list.response import CertsListResponse


class CertsListUseCase:
    def __init__(self, cert_manager_port: CertManagerPort) -> None:
        self._port = cert_manager_port

    def execute(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=[asdict(c) for c in certs])
