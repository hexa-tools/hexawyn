from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_optimization_roi.command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)


class ComputeOptimizationRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse: ...
