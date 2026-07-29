from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.global_health_check.command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.use_case.cluster.global_health_check.response import (
    GlobalHealthCheckResponse,
)


class GlobalHealthCheckServicePort(ABC):
    @abstractmethod
    def global_health_check(
        self, command: GlobalHealthCheckCommand
    ) -> GlobalHealthCheckResponse: ...
