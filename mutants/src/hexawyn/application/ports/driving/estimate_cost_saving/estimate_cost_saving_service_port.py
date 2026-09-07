from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EstimateCostSavingServicePort(ABC):
    @abstractmethod
    def estimate_cost_saving(
        self, command: EstimateCostSavingCommand
    ) -> EstimateCostSavingResponse: ...
