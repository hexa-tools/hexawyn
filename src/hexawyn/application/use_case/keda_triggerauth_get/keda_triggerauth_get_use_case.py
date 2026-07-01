from __future__ import annotations

from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_command import (
    KedaTriggerAuthGetCommand,
)
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_response import (
    KedaTriggerAuthGetResponse,
)
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_service_port import (
    KedaTriggerAuthGetServicePort,
)


class KedaTriggerAuthGetUseCase:
    def __init__(self, service: KedaTriggerAuthGetServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaTriggerAuthGetCommand) -> KedaTriggerAuthGetResponse:
        return self._svc.get_auth(cmd)
