from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_triggerauth_get.command import KedaTriggerauthGetCommand
from hexawyn.application.use_case.keda_triggerauth_get.response import KedaTriggerauthGetResponse


class KedaTriggerAuthGetUseCase:
    def __init__(self, keda_port: KedaPort) -> None:
        self._port = keda_port

    def execute(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(name=a.name, namespace=a.namespace, kind=a.kind)
