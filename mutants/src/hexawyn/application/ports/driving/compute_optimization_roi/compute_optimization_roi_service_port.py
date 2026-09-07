from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_optimization_roi.command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeOptimizationRoiServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse: ...
