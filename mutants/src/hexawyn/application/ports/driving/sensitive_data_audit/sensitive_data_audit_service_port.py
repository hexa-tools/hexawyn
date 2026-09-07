from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.sensitive_data_audit.command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.use_case.security.sensitive_data_audit.response import (
    SensitiveDataAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SensitiveDataAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse: ...
