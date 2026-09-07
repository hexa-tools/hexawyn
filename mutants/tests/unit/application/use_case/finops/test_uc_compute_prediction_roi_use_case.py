from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compute_prediction_roi.command import (
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.compute_prediction_roi_use_case import (  # noqa: E501
    ComputePredictionRoiUseCase,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.response import (  # noqa: E501
    ComputePredictionRoiResponse,
)


class TestComputePredictionRoiUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_prediction_data.return_value = []

        use_case = ComputePredictionRoiUseCase(
            prediction_roi_port=port,
        )
        result = use_case.execute(ComputePredictionRoiCommand(period="2025-Q1"))

        assert isinstance(result, ComputePredictionRoiResponse)
