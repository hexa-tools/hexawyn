from __future__ import annotations

from hexawyn.application.ports.driving.global_health_check.global_health_check_command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_response import (
    GlobalHealthCheckResponse,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_service_port import (
    GlobalHealthCheckServicePort,
)


class GlobalHealthCheckUseCase:
    def __init__(self, service: GlobalHealthCheckServicePort) -> None:
        self._service = service

    def execute(self, command: GlobalHealthCheckCommand) -> GlobalHealthCheckResponse:
        return self._service.global_health_check(command)
