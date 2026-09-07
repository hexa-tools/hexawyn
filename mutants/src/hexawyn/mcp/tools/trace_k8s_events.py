"""MCP tool: trace_k8s_events — Show k8s events during a slow trace window."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.trace_k8s_events_use_case import (  # noqa: E501
    TraceK8sEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_trace_k8s_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_trace_k8s_events__mutmut)
def trace_k8s_events(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_orig(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_1(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = None
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_2(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = None
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_3(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(None)
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_4(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=None).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_5(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=None))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_6(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "XXtrace_idXX": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_7(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "TRACE_ID": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_8(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "XXmatching_eventsXX": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_9(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "MATCHING_EVENTS": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_10(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "XXslowest_spanXX": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_11(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "SLOWEST_SPAN": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_12(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "XXconclusionXX": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_13(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "CONCLUSION": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_14(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_15(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_16(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXtrace_idXX": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_17(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"TRACE_ID": trace_id, "error": str(exc)}


def x_trace_k8s_events__mutmut_18(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "XXerrorXX": str(exc)}


def x_trace_k8s_events__mutmut_19(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "ERROR": str(exc)}


def x_trace_k8s_events__mutmut_20(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(None)}

mutants_x_trace_k8s_events__mutmut['_mutmut_orig'] = x_trace_k8s_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_1'] = x_trace_k8s_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_2'] = x_trace_k8s_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_3'] = x_trace_k8s_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_4'] = x_trace_k8s_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_5'] = x_trace_k8s_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_6'] = x_trace_k8s_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_7'] = x_trace_k8s_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_8'] = x_trace_k8s_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_9'] = x_trace_k8s_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_10'] = x_trace_k8s_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_11'] = x_trace_k8s_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_12'] = x_trace_k8s_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_13'] = x_trace_k8s_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_14'] = x_trace_k8s_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_15'] = x_trace_k8s_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_16'] = x_trace_k8s_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_17'] = x_trace_k8s_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_18'] = x_trace_k8s_events__mutmut_18 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_19'] = x_trace_k8s_events__mutmut_19 # type: ignore # mutmut generated
mutants_x_trace_k8s_events__mutmut['x_trace_k8s_events__mutmut_20'] = x_trace_k8s_events__mutmut_20 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(trace_k8s_events)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(trace_k8s_events)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
