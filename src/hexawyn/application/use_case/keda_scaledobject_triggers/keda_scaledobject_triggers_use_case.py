from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_command import (
    KedaScaledObjectTriggersCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_response import (
    KedaScaledObjectTriggersResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_service_port import (
    KedaScaledObjectTriggersServicePort,
)


class KedaScaledObjectTriggersUseCase:
    def __init__(self, service: KedaScaledObjectTriggersServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledObjectTriggersCommand) -> KedaScaledObjectTriggersResponse:
        return self._svc.get_triggers(cmd)
