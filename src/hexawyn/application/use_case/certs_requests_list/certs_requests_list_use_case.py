from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_requests_list.command import CertsRequestsListCommand
from hexawyn.application.use_case.certs_requests_list.response import CertsRequestsListResponse


class CertsRequestsListUseCase:
    def __init__(self, cert_manager_port: CertManagerPort) -> None:
        self._port = cert_manager_port

    def execute(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])
