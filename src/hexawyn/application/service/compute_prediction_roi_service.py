from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_response import (  # noqa: E501
    ComputePredictionRoiResponse,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
    ComputePredictionRoiServicePort,
)
from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
    compute_prediction_roi,
)


class ComputePredictionRoiService(ComputePredictionRoiServicePort):
    def __init__(self, prediction_roi_port: PredictionRoiPort) -> None:
        self._port = prediction_roi_port

    def compute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)
