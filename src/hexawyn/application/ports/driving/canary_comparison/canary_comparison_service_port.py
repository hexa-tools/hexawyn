from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.canary_comparison.command import (
    CanaryComparisonCommand,
)
from hexawyn.application.use_case.pipelines.canary_comparison.response import (
    CanaryComparisonResponse,
)


class CanaryComparisonServicePort(ABC):
    @abstractmethod
    def compare(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse: ...
