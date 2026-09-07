from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.finops.cost_profiling.response import (
    CostProfilingResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CostProfilingServicePort(ABC):
    @abstractmethod
    def profile(self, command: CostProfilingCommand) -> CostProfilingResponse: ...
