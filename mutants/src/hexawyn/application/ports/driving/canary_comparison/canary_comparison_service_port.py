from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.canary_comparison.command import (
    CanaryComparisonCommand,
)
from hexawyn.application.use_case.pipelines.canary_comparison.response import (
    CanaryComparisonResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CanaryComparisonServicePort(ABC):
    @abstractmethod
    def compare(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse: ...
