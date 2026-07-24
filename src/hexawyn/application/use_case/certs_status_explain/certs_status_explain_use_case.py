from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_status_explain.command import CertsStatusExplainCommand
from hexawyn.application.use_case.certs_status_explain.response import CertsStatusExplainResponse


class CertsStatusExplainUseCase:
    def __init__(self, cert_manager_port: CertManagerPort) -> None:
        self._port = cert_manager_port

    def execute(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )
