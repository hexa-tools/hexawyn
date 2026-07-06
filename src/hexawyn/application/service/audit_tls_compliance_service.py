from __future__ import annotations

from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_command import (
    AuditTLSComplianceCommand,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_response import (
    AuditTLSComplianceResponse,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_service_port import (
    AuditTLSComplianceServicePort,
)
from hexawyn.domain.services.tls_compliance.tls_compliance_engine import (
    TLSComplianceEngine,
)


class AuditTLSComplianceService(AuditTLSComplianceServicePort):
    def __init__(self, tls_port: TLSCompliancePort) -> None:
        self._port = tls_port
        self._engine = TLSComplianceEngine()

    def audit(self, command: AuditTLSComplianceCommand) -> AuditTLSComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTLSComplianceResponse(result=result)
