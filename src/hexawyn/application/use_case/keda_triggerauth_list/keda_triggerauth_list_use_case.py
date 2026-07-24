from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_triggerauth_list.command import KedaTriggerauthListCommand
from hexawyn.application.use_case.keda_triggerauth_list.response import KedaTriggerauthListResponse


class KedaTriggerAuthListUseCase:
    def __init__(self, keda_port: KedaPort) -> None:
        self._port = keda_port

    def execute(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerauthListResponse(trigger_auths=[asdict(a) for a in auths])
