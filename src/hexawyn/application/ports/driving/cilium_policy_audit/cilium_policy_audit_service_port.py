from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.response import (
    CiliumPolicyAuditResponse,
)


class CiliumPolicyAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse: ...
