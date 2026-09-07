from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_prediction_roi.command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.response import (  # noqa: E501
    ComputePredictionRoiResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputePredictionRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse: ...
