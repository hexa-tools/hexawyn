from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.governance.policy_violations_list.response import (
    PolicyViolationsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PolicyViolationsListServicePort(ABC):
    @abstractmethod
    def list_violations(
        self, command: PolicyViolationsListCommand
    ) -> PolicyViolationsListResponse: ...
