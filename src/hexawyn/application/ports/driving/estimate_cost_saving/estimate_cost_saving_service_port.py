from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)


class EstimateCostSavingServicePort(ABC):
    @abstractmethod
    def estimate_cost_saving(
        self, command: EstimateCostSavingCommand
    ) -> EstimateCostSavingResponse: ...
