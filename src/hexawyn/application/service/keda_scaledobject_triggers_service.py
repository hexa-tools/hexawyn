from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledobject_triggers.command import (
    KedaScaledObjectTriggersCommand,
)
from hexawyn.application.use_case.keda_scaledobject_triggers.response import (
    KedaScaledObjectTriggersResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_service_port import (
    KedaScaledObjectTriggersServicePort,
)


class KedaScaledObjectTriggersService(KedaScaledObjectTriggersServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_triggers(
        self, command: KedaScaledObjectTriggersCommand
    ) -> KedaScaledObjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledObjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])
