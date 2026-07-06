from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_response import (
    ComputeMTTRTrendResponse,
)


class ComputeMTTRTrendServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse: ...
