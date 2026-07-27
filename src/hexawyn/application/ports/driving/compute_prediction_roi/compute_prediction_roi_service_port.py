from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_prediction_roi.command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.response import (  # noqa: E501
    ComputePredictionRoiResponse,
)


class ComputePredictionRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse: ...
