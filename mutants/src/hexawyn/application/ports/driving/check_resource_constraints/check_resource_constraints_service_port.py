from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CheckResourceConstraintsServicePort(ABC):
    @abstractmethod
    def check_resource_constraints(
        self, command: CheckResourceConstraintsCommand
    ) -> CheckResourceConstraintsResponse: ...
