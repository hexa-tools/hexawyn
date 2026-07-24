from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.audit_tls_compliance.command import (
    AuditTlsComplianceCommand,
)
from hexawyn.application.use_case.audit_tls_compliance.response import (
    AuditTlsComplianceResponse,
)


class AuditTLSComplianceServicePort(ABC):
    @abstractmethod
    def audit(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        ...
