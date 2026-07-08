from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_command import (
    KedaTriggerAuthGetCommand,
)
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_response import (
    KedaTriggerAuthGetResponse,
)
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_service_port import (
    KedaTriggerAuthGetServicePort,
)


class KedaTriggerAuthGetService(KedaTriggerAuthGetServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_auth(self, command: KedaTriggerAuthGetCommand) -> KedaTriggerAuthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerAuthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,
            ready=a.ready,
            message=a.message,
        )
