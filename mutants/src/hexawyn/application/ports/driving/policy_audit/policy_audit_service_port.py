from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_audit.command import (
    PolicyAuditCommand,
)
from hexawyn.application.use_case.governance.policy_audit.response import (
    PolicyAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PolicyAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: PolicyAuditCommand) -> PolicyAuditResponse: ...
