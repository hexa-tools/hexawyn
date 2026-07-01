from __future__ import annotations

from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_command import (
    CertsStatusExplainCommand,
)
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_response import (
    CertsStatusExplainResponse,
)
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_service_port import (
    CertsStatusExplainServicePort,
)


class CertsStatusExplainUseCase:
    def __init__(self, service: CertsStatusExplainServicePort) -> None:
        self._service = service

    def execute(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        return self._service.explain(command)
