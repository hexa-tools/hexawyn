from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.service.chat_cli_service import ChatCliService
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.application.use_case.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse


def route_command(text: str, adapter: K8sPort) -> ChatCliResponse:
    service = ChatCliService(k8s_port=adapter, runtime=get_runtime())
    return service.execute(ChatCliCommand(query=text))
