from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.cost_profiling.cost_profiling_command import (
    CostProfilingCommand,
)
from hexawyn.application.ports.driving.cost_profiling.cost_profiling_response import (
    CostProfilingResponse,
)


class CostProfilingServicePort(ABC):
    @abstractmethod
    def profile(self, command: CostProfilingCommand) -> CostProfilingResponse: ...
