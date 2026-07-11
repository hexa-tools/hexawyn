from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)


class ComputeOptimizationRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse: ...
