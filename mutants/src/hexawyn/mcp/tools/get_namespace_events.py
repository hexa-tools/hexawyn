"""MCP tool: get_namespace_events."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.get_namespace_events_use_case import (  # noqa: E501
    GetNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_namespace_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_namespace_events__mutmut)
def get_namespace_events(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=None)  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=None))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_get_namespace_events__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_get_namespace_events__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_get_namespace_events__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_get_namespace_events__mutmut['_mutmut_orig'] = x_get_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_1'] = x_get_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_2'] = x_get_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_3'] = x_get_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_4'] = x_get_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_5'] = x_get_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_6'] = x_get_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_7'] = x_get_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_8'] = x_get_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_9'] = x_get_namespace_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_10'] = x_get_namespace_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_events)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_events)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
