from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_triggerauth_get.command import (
    KedaTriggerauthGetCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_get.response import (
    KedaTriggerauthGetResponse,
)


class KedaTriggerauthGetUseCase:
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def execute(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )
