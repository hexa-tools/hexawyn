# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_status_explain.command import (
    CertsStatusExplainCommand,
)


class CertsStatusExplainUseCase:
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def explain(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )
