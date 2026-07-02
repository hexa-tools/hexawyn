from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_response import (
    SensitiveDataAuditResponse,
)


class SensitiveDataAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse: ...
