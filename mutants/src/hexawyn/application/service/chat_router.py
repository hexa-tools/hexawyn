"""Chat routing — bridge between the CLI chat input and the chat use case."""

from __future__ import annotations

from collections.abc import Callable

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_command import (
    ChatCliCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
    ChatCliResponse,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_use_case import (
    ChatCliUseCase,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_route_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_route_command__mutmut)
def route_command(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_orig(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_1(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = None
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_2(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=None, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_3(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=None)
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_4(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_5(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, )
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_6(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        None,
        on_progress=on_progress,
    )


def x_route_command__mutmut_7(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        on_progress=None,
    )


def x_route_command__mutmut_8(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        on_progress=on_progress,
    )


def x_route_command__mutmut_9(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history or []),
        )


def x_route_command__mutmut_10(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=None, conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_11(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=None),
        on_progress=on_progress,
    )


def x_route_command__mutmut_12(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(conversation_history=conversation_history or []),
        on_progress=on_progress,
    )


def x_route_command__mutmut_13(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, ),
        on_progress=on_progress,
    )


def x_route_command__mutmut_14(
    text: str,
    adapter: K8sPort,
    conversation_history: list[dict[str, str]] | None = None,
    on_progress: Callable[[str, str], None] | None = None,
) -> ChatCliResponse:
    use_case = ChatCliUseCase(k8s_port=adapter, runtime=get_runtime())
    return use_case.execute(
        ChatCliCommand(query=text, conversation_history=conversation_history and []),
        on_progress=on_progress,
    )

mutants_x_route_command__mutmut['_mutmut_orig'] = x_route_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_1'] = x_route_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_2'] = x_route_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_3'] = x_route_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_4'] = x_route_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_5'] = x_route_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_6'] = x_route_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_7'] = x_route_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_8'] = x_route_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_9'] = x_route_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_10'] = x_route_command__mutmut_10 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_11'] = x_route_command__mutmut_11 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_12'] = x_route_command__mutmut_12 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_13'] = x_route_command__mutmut_13 # type: ignore # mutmut generated
mutants_x_route_command__mutmut['x_route_command__mutmut_14'] = x_route_command__mutmut_14 # type: ignore # mutmut generated
