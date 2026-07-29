from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.compute_mttr_trend.command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.response import (
    ComputeMTTRTrendResponse,
)


class ComputeMTTRTrendServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse: ...
