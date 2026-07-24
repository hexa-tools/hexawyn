from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.sensitive_data_audit.command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.use_case.sensitive_data_audit.response import (
    SensitiveDataAuditResponse,
)


class SensitiveDataAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse: ...
