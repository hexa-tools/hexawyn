"""Unit tests for ComputePredictionRoiUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (
    ComputePredictionRoiServicePort,
)
from hexawyn.application.use_case.compute_prediction_roi.compute_prediction_roi_use_case import (
    ComputePredictionRoiUseCase,
)


class TestComputePredictionRoiUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputePredictionRoiServicePort)
        use_case = ComputePredictionRoiUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputePredictionRoiServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputePredictionRoiUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
