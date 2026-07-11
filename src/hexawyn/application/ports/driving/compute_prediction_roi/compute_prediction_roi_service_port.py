from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_response import (  # noqa: E501
    ComputePredictionRoiResponse,
)


class ComputePredictionRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse: ...
