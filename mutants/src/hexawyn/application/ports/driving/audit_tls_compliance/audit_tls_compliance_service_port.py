from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.audit_tls_compliance.command import (
    AuditTlsComplianceCommand,
)
from hexawyn.application.use_case.security.audit_tls_compliance.response import (
    AuditTlsComplianceResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AuditTLSComplianceServicePort(ABC):
    @abstractmethod
    def audit(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse: ...
