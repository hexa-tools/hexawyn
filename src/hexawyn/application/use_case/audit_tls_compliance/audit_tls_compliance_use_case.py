from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort
from hexawyn.application.use_case.audit_tls_compliance.command import AuditTlsComplianceCommand
from hexawyn.application.use_case.audit_tls_compliance.response import AuditTlsComplianceResponse
from hexawyn.domain.services.tls_compliance.tls_compliance_engine import TLSComplianceEngine


class AuditTlsComplianceUseCase:
    def __init__(self, tls_port: TLSCompliancePort) -> None:
        self._port = tls_port
        self._engine = TLSComplianceEngine()

    def execute(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)
