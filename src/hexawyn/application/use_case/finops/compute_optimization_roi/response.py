from dataclasses import dataclass

from hexawyn.domain.models.optimization_roi import OptimizationRoiReport


@dataclass
class ComputeOptimizationRoiResponse:
    result: OptimizationRoiReport
