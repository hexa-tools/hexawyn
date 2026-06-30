from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_response import (
    EstimateCostSavingResponse,
)


class EstimateCostSavingServicePort(ABC):
    @abstractmethod
    def estimate_cost_saving(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse: ...
