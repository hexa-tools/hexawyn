from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_command import (
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_response import (
    KedaScaledObjectStatusResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_service_port import (
    KedaScaledObjectStatusServicePort,
)


class KedaScaledObjectStatusUseCase:
    def __init__(self, service: KedaScaledObjectStatusServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledObjectStatusCommand) -> KedaScaledObjectStatusResponse:
        return self._svc.get_status(cmd)
