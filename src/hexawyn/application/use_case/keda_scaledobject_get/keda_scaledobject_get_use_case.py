from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_command import (
    KedaScaledObjectGetCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_response import (
    KedaScaledObjectGetResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_service_port import (
    KedaScaledObjectGetServicePort,
)


class KedaScaledObjectGetUseCase:
    def __init__(self, service: KedaScaledObjectGetServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledObjectGetCommand) -> KedaScaledObjectGetResponse:
        return self._svc.get_object(cmd)
