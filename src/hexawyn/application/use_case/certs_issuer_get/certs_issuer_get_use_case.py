from __future__ import annotations

from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_response import (
    CertsIssuerGetResponse,
)
from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_service_port import (
    CertsIssuerGetServicePort,
)


class CertsIssuerGetUseCase:
    def __init__(self, service: CertsIssuerGetServicePort) -> None:
        self._service = service

    def execute(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        return self._service.get_issuer(command)
