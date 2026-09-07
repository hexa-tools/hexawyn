from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.response import (
    CiliumPolicyAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumPolicyAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse: ...
