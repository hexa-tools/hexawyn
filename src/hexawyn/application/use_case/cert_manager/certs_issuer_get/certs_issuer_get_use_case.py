from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_issuer_get.command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuer_get.response import (
    CertsIssuerGetResponse,
)


class CertsIssuerGetUseCase:
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def execute(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )
