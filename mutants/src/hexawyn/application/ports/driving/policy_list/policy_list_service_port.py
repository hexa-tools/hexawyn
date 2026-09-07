from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_list.command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.governance.policy_list.response import (
    PolicyListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PolicyListServicePort(ABC):
    @abstractmethod
    def list_policies(self, command: PolicyListCommand) -> PolicyListResponse: ...
