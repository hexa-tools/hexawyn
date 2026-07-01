from __future__ import annotations

from hexawyn.application.ports.driving.canary_comparison.canary_comparison_command import (
    CanaryComparisonCommand,
)
from hexawyn.application.ports.driving.canary_comparison.canary_comparison_response import (
    CanaryComparisonResponse,
)
from hexawyn.application.ports.driving.canary_comparison.canary_comparison_service_port import (
    CanaryComparisonServicePort,
)


class CanaryComparisonUseCase:
    def __init__(self, service: CanaryComparisonServicePort) -> None:
        self._svc = service

    def execute(self, cmd: CanaryComparisonCommand) -> CanaryComparisonResponse:
        return self._svc.compare(cmd)
