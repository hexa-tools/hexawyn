from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_command import (
    AuditTLSComplianceCommand,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_response import (
    AuditTLSComplianceResponse,
)


class AuditTLSComplianceServicePort(ABC):
    @abstractmethod
    def audit(self, command: AuditTLSComplianceCommand) -> AuditTLSComplianceResponse: ...
