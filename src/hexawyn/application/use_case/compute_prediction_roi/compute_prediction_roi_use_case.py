from __future__ import annotations

from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_response import (  # noqa: E501
    ComputePredictionRoiResponse,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
    ComputePredictionRoiServicePort,
)


class ComputePredictionRoiUseCase:
    def __init__(self, service: ComputePredictionRoiServicePort) -> None:
        self._service = service

    def execute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        return self._service.compute(command)
