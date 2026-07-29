from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.finops.cost_profiling.response import (
    CostProfilingResponse,
)


class CostProfilingServicePort(ABC):
    @abstractmethod
    def profile(self, command: CostProfilingCommand) -> CostProfilingResponse: ...
