from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.canary_comparison.canary_comparison_command import (
    CanaryComparisonCommand,
)
from hexawyn.application.ports.driving.canary_comparison.canary_comparison_response import (
    CanaryComparisonResponse,
)


class CanaryComparisonServicePort(ABC):
    @abstractmethod
    def compare(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse: ...
