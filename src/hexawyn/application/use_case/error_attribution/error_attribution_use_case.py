from __future__ import annotations

from hexawyn.application.ports.driving.error_attribution.error_attribution_command import (
    ErrorAttributionCommand,
)
from hexawyn.application.ports.driving.error_attribution.error_attribution_response import (
    ErrorAttributionResponse,
)
from hexawyn.application.ports.driving.error_attribution.error_attribution_service_port import (
    ErrorAttributionServicePort,
)


class ErrorAttributionUseCase:
    def __init__(self, service: ErrorAttributionServicePort) -> None:
        self._svc = service

    def execute(self, cmd: ErrorAttributionCommand) -> ErrorAttributionResponse:
        return self._svc.attribute(cmd)
