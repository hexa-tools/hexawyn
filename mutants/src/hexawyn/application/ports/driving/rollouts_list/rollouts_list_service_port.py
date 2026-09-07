from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollouts_list.command import (
    RolloutsListCommand,
)
from hexawyn.application.use_case.workloads.rollouts_list.response import (
    RolloutsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RolloutsListServicePort(ABC):
    @abstractmethod
    def list_rollouts(self, command: RolloutsListCommand) -> RolloutsListResponse: ...
