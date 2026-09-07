from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollout_status.command import (
    RolloutStatusCommand,
)
from hexawyn.application.use_case.workloads.rollout_status.response import (
    RolloutStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RolloutStatusServicePort(ABC):
    @abstractmethod
    def get_status(self, command: RolloutStatusCommand) -> RolloutStatusResponse: ...
