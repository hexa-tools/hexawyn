from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort
from hexawyn.application.use_case.finops.compute_optimization_roi.command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)
from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
    OptimizationRoiService,
)


class ComputeOptimizationRoiUseCase:
    def __init__(self, roi_port: OptimizationRoiPort) -> None:
        self._port = roi_port
        self._engine = OptimizationRoiService()

    def execute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)
