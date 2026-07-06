from __future__ import annotations

from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_command import (
    AuditTLSComplianceCommand,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_response import (
    AuditTLSComplianceResponse,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_service_port import (
    AuditTLSComplianceServicePort,
)


class AuditTLSComplianceUseCase:
    def __init__(self, service: AuditTLSComplianceServicePort) -> None:
        self._service = service

    def execute(self, command: AuditTLSComplianceCommand) -> AuditTLSComplianceResponse:
        return self._service.audit(command)
