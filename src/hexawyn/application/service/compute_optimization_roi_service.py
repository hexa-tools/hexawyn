from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
    ComputeOptimizationRoiServicePort,
)
from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
    OptimizationRoiService,
)


class ComputeOptimizationRoiService(ComputeOptimizationRoiServicePort):
    def __init__(self, roi_port: OptimizationRoiPort) -> None:
        self._port = roi_port
        self._engine = OptimizationRoiService()

    def compute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)
