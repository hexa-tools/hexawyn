from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledobjects_list.command import (
    KedaScaledobjectsListCommand,
)
from hexawyn.application.use_case.keda_scaledobjects_list.response import (
    KedaScaledobjectsListResponse,
)


class KedaScaledObjectsListUseCase:
    def __init__(self, keda_port: KedaPort) -> None:
        self._port = keda_port

    def execute(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(o) for o in objs])
