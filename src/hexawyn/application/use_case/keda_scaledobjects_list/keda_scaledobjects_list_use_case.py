from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_command import (
    KedaScaledObjectsListCommand,
)
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_response import (
    KedaScaledObjectsListResponse,
)
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_service_port import (
    KedaScaledObjectsListServicePort,
)


class KedaScaledObjectsListUseCase:
    def __init__(self, service: KedaScaledObjectsListServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledObjectsListCommand) -> KedaScaledObjectsListResponse:
        return self._svc.list_objects(cmd)
