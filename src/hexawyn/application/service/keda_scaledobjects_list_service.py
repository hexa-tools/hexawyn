from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_command import (
    KedaScaledObjectsListCommand,
)
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_response import (
    KedaScaledObjectsListResponse,
)
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_service_port import (
    KedaScaledObjectsListServicePort,
)


class KedaScaledObjectsListService(KedaScaledObjectsListServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def list_objects(self, command: KedaScaledObjectsListCommand) -> KedaScaledObjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledObjectsListResponse(scaled_objects=[asdict(o) for o in objs])
