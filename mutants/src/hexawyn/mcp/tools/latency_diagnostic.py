"""MCP tool: latency_diagnostic — Identify root cause of latency spikes via OTel traces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.latency_diagnostic.command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.use_case.observability.latency_diagnostic.latency_diagnostic_use_case import (  # noqa: E501
    LatencyDiagnosticUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_latency_diagnostic__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_latency_diagnostic__mutmut)
def latency_diagnostic(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_orig(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_1(
    service_name: str, time_window_minutes: int = 16, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_2(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 501.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_3(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = None
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_4(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = None
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_5(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            None
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_6(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=None).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_7(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=None,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_8(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=None,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_9(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=None,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_10(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_11(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_12(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_13(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "XXservice_nameXX": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_14(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "SERVICE_NAME": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_15(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "XXslow_trace_countXX": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_16(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "SLOW_TRACE_COUNT": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_17(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "XXtotal_tracesXX": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_18(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "TOTAL_TRACES": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_19(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "XXbottlenecksXX": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_20(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "BOTTLENECKS": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_21(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "XXslowest_spanXX": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_22(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "SLOWEST_SPAN": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_23(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_24(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_25(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXservice_nameXX": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_26(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"SERVICE_NAME": service_name, "error": str(exc)}


def x_latency_diagnostic__mutmut_27(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "XXerrorXX": str(exc)}


def x_latency_diagnostic__mutmut_28(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "ERROR": str(exc)}


def x_latency_diagnostic__mutmut_29(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(None)}

mutants_x_latency_diagnostic__mutmut['_mutmut_orig'] = x_latency_diagnostic__mutmut_orig # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_1'] = x_latency_diagnostic__mutmut_1 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_2'] = x_latency_diagnostic__mutmut_2 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_3'] = x_latency_diagnostic__mutmut_3 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_4'] = x_latency_diagnostic__mutmut_4 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_5'] = x_latency_diagnostic__mutmut_5 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_6'] = x_latency_diagnostic__mutmut_6 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_7'] = x_latency_diagnostic__mutmut_7 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_8'] = x_latency_diagnostic__mutmut_8 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_9'] = x_latency_diagnostic__mutmut_9 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_10'] = x_latency_diagnostic__mutmut_10 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_11'] = x_latency_diagnostic__mutmut_11 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_12'] = x_latency_diagnostic__mutmut_12 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_13'] = x_latency_diagnostic__mutmut_13 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_14'] = x_latency_diagnostic__mutmut_14 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_15'] = x_latency_diagnostic__mutmut_15 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_16'] = x_latency_diagnostic__mutmut_16 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_17'] = x_latency_diagnostic__mutmut_17 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_18'] = x_latency_diagnostic__mutmut_18 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_19'] = x_latency_diagnostic__mutmut_19 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_20'] = x_latency_diagnostic__mutmut_20 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_21'] = x_latency_diagnostic__mutmut_21 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_22'] = x_latency_diagnostic__mutmut_22 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_23'] = x_latency_diagnostic__mutmut_23 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_24'] = x_latency_diagnostic__mutmut_24 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_25'] = x_latency_diagnostic__mutmut_25 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_26'] = x_latency_diagnostic__mutmut_26 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_27'] = x_latency_diagnostic__mutmut_27 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_28'] = x_latency_diagnostic__mutmut_28 # type: ignore # mutmut generated
mutants_x_latency_diagnostic__mutmut['x_latency_diagnostic__mutmut_29'] = x_latency_diagnostic__mutmut_29 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(latency_diagnostic)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(latency_diagnostic)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
