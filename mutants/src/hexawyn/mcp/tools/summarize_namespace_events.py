"""MCP tool: summarize_namespace_events — Phase 1 progressive disclosure (high-level overview)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.summarize_namespace_events_use_case import (  # noqa: E501
    SummarizeNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_summarize_namespace_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_summarize_namespace_events__mutmut)
def summarize_namespace_events(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_orig(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_1(namespace: str, time_window_minutes: int = 16) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_2(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = None
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_3(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = None
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_4(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = None
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_5(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=None
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_6(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=None, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_7(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=None
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_8(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_9(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_10(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=None, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_11(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=None
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_12(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_13(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_14(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "XXnamespaceXX": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_15(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "NAMESPACE": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_16(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "XXtotal_eventsXX": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_17(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "TOTAL_EVENTS": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_18(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "XXseverity_breakdownXX": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_19(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "SEVERITY_BREAKDOWN": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_20(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "XXtop_affected_podsXX": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_21(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "TOP_AFFECTED_PODS": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_22(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_23(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_24(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXnamespaceXX": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_25(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"NAMESPACE": namespace, "error": str(exc)}


def x_summarize_namespace_events__mutmut_26(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "XXerrorXX": str(exc)}


def x_summarize_namespace_events__mutmut_27(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "ERROR": str(exc)}


def x_summarize_namespace_events__mutmut_28(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(  # type: ignore
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(None)}

mutants_x_summarize_namespace_events__mutmut['_mutmut_orig'] = x_summarize_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_1'] = x_summarize_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_2'] = x_summarize_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_3'] = x_summarize_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_4'] = x_summarize_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_5'] = x_summarize_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_6'] = x_summarize_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_7'] = x_summarize_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_8'] = x_summarize_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_9'] = x_summarize_namespace_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_10'] = x_summarize_namespace_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_11'] = x_summarize_namespace_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_12'] = x_summarize_namespace_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_13'] = x_summarize_namespace_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_14'] = x_summarize_namespace_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_15'] = x_summarize_namespace_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_16'] = x_summarize_namespace_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_17'] = x_summarize_namespace_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_18'] = x_summarize_namespace_events__mutmut_18 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_19'] = x_summarize_namespace_events__mutmut_19 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_20'] = x_summarize_namespace_events__mutmut_20 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_21'] = x_summarize_namespace_events__mutmut_21 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_22'] = x_summarize_namespace_events__mutmut_22 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_23'] = x_summarize_namespace_events__mutmut_23 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_24'] = x_summarize_namespace_events__mutmut_24 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_25'] = x_summarize_namespace_events__mutmut_25 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_26'] = x_summarize_namespace_events__mutmut_26 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_27'] = x_summarize_namespace_events__mutmut_27 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_28'] = x_summarize_namespace_events__mutmut_28 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(summarize_namespace_events)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(summarize_namespace_events)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
