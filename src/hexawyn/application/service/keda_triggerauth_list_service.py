from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_triggerauth_list.command import (
    KedaTriggerAuthListCommand,
)
from hexawyn.application.use_case.keda_triggerauth_list.response import (
    KedaTriggerAuthListResponse,
)
from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_service_port import (
    KedaTriggerAuthListServicePort,
)


class KedaTriggerAuthListService(KedaTriggerAuthListServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def list_auths(self, command: KedaTriggerAuthListCommand) -> KedaTriggerAuthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerAuthListResponse(trigger_auths=[asdict(a) for a in auths])
