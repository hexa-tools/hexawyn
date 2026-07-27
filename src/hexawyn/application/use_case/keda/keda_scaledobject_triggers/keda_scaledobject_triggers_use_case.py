from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.command import (
    KedaScaledobjectTriggersCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.response import (
    KedaScaledobjectTriggersResponse,
)


class KedaScaledobjectTriggersUseCase:
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_triggers(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])
