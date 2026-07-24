from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_issuers_list.command import CertsIssuersListCommand
from hexawyn.application.use_case.certs_issuers_list.response import CertsIssuersListResponse


class CertsIssuersListUseCase:
    def __init__(self, cert_manager_port: CertManagerPort) -> None:
        self._port = cert_manager_port

    def execute(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])
