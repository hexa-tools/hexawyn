from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_command import (
    KedaScaledJobGetCommand,
)
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_response import (
    KedaScaledJobGetResponse,
)
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_service_port import (
    KedaScaledJobGetServicePort,
)


class KedaScaledJobGetUseCase:
    def __init__(self, service: KedaScaledJobGetServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledJobGetCommand) -> KedaScaledJobGetResponse:
        return self._svc.get_job(cmd)
