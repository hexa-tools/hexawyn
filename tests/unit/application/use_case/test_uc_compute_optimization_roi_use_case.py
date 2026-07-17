"""Unit tests for ComputeOptimizationRoiUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (
    ComputeOptimizationRoiServicePort,
)
from hexawyn.application.use_case.compute_optimization_roi.compute_optimization_roi_use_case import (
    ComputeOptimizationRoiUseCase,
)


class TestComputeOptimizationRoiUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeOptimizationRoiServicePort)
        use_case = ComputeOptimizationRoiUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeOptimizationRoiServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeOptimizationRoiUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
