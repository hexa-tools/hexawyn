from __future__ import annotations

from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_command import (
    KedaTriggerAuthListCommand,
)
from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_response import (
    KedaTriggerAuthListResponse,
)
from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_service_port import (
    KedaTriggerAuthListServicePort,
)


class KedaTriggerAuthListUseCase:
    def __init__(self, service: KedaTriggerAuthListServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaTriggerAuthListCommand) -> KedaTriggerAuthListResponse:
        return self._svc.list_auths(cmd)
