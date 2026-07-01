from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_audit.policy_audit_command import (
    PolicyAuditCommand,
)
from hexawyn.application.ports.driving.policy_audit.policy_audit_response import (
    PolicyAuditResponse,
)


class PolicyAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        """Run a compliance audit."""
