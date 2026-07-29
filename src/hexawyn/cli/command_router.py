# mypy: ignore-errors
from collections.abc import Callable

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import ChatCliResponse


def route_command(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    service = ChatCliService(k8s_port=adapter, runtime=get_runtime())  # noqa: F821  # type: ignore
    return service._execute(  # type: ignore
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )
