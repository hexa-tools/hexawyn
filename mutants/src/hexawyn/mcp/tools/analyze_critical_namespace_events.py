"""MCP tool: analyze_critical_namespace_events — Analyze critical namespace events."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsUseCase,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_critical_namespace_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_critical_namespace_events__mutmut)
def analyze_critical_namespace_events(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = None
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=None,
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=None,
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = None
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(None)
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=None))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"XXcritical_eventsXX": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"CRITICAL_EVENTS": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "XXerrorXX": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "ERROR": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"XXcritical_eventsXX": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"CRITICAL_EVENTS": [], "error": str(exc)}


def x_analyze_critical_namespace_events__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "XXerrorXX": str(exc)}


def x_analyze_critical_namespace_events__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "ERROR": str(exc)}


def x_analyze_critical_namespace_events__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(None)}

mutants_x_analyze_critical_namespace_events__mutmut['_mutmut_orig'] = x_analyze_critical_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_1'] = x_analyze_critical_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_2'] = x_analyze_critical_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_3'] = x_analyze_critical_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_4'] = x_analyze_critical_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_5'] = x_analyze_critical_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_6'] = x_analyze_critical_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_7'] = x_analyze_critical_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_8'] = x_analyze_critical_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_9'] = x_analyze_critical_namespace_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_10'] = x_analyze_critical_namespace_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_11'] = x_analyze_critical_namespace_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_12'] = x_analyze_critical_namespace_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_13'] = x_analyze_critical_namespace_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_14'] = x_analyze_critical_namespace_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_15'] = x_analyze_critical_namespace_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_16'] = x_analyze_critical_namespace_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_critical_namespace_events__mutmut['x_analyze_critical_namespace_events__mutmut_17'] = x_analyze_critical_namespace_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_critical_namespace_events)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(analyze_critical_namespace_events)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
