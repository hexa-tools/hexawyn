from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort
from hexawyn.application.use_case.finops.compute_prediction_roi.command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.response import (  # noqa: E501
    ComputePredictionRoiResponse,
)
from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
    compute_prediction_roi,
)


class ComputePredictionRoiUseCase:
    def __init__(self, prediction_roi_port: PredictionRoiPort) -> None:
        self._port = prediction_roi_port

    def execute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)
