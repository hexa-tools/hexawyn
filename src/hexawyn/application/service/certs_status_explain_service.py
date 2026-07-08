from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_command import (
    CertsStatusExplainCommand,
)
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_response import (
    CertsStatusExplainResponse,
)
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_service_port import (
    CertsStatusExplainServicePort,
)


class CertsStatusExplainService(CertsStatusExplainServicePort):
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def explain(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )
