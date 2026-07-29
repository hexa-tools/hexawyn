from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compute_optimization_roi.command import (
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.compute_optimization_roi_use_case import (  # noqa: E501
    ComputeOptimizationRoiUseCase,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)


class TestComputeOptimizationRoiUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_sprint_roi_data.return_value = {
            "has_baseline": True,
            "baseline_monthly_eur": 10000.0,
            "current_monthly_eur": 8000.0,
            "optimizations": [],
            "performance_metrics": [],
        }

        use_case = ComputeOptimizationRoiUseCase(roi_port=port)
        result = use_case.execute(ComputeOptimizationRoiCommand(sprint_id="SPRINT-42"))

        assert isinstance(result, ComputeOptimizationRoiResponse)
        assert result.result is not None
