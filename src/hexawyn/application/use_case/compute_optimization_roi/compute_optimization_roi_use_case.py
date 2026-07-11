from __future__ import annotations

from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
    ComputeOptimizationRoiServicePort,
)


class ComputeOptimizationRoiUseCase:
    def __init__(self, service: ComputeOptimizationRoiServicePort) -> None:
        self._service = service

    def execute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        return self._service.compute(command)
