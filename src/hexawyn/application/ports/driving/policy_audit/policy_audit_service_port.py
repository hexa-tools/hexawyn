from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_audit.command import (
    PolicyAuditCommand,
)
from hexawyn.application.use_case.governance.policy_audit.response import (
    PolicyAuditResponse,
)


class PolicyAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: PolicyAuditCommand) -> PolicyAuditResponse: ...
