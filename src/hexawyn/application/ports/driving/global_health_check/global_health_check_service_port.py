from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.global_health_check.global_health_check_command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_response import (
    GlobalHealthCheckResponse,
)


class GlobalHealthCheckServicePort(ABC):
    @abstractmethod
    def global_health_check(
        self, command: GlobalHealthCheckCommand
    ) -> GlobalHealthCheckResponse: ...
