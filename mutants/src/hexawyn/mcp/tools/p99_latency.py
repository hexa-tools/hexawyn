"""MCP tool: p99_latency — Compute p99 latency for an HTTP endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.observability.p99_latency.p99_latency_use_case import (
    P99LatencyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_p99_latency__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_p99_latency__mutmut)
def p99_latency(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_orig(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_1(
    endpoint: str, time_window_minutes: int = 121, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_2(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 501.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_3(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = None
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_4(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = None
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_5(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            None
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_6(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=None).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_7(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=None,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_8(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=None,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_9(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=None,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_10(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_11(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_12(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_13(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "XXendpointXX": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_14(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "ENDPOINT": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_15(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "XXp50_msXX": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_16(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "P50_MS": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_17(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "XXp95_msXX": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_18(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "P95_MS": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_19(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "XXp99_msXX": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_20(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "P99_MS": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_21(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "XXslo_threshold_msXX": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_22(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "SLO_THRESHOLD_MS": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_23(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "XXslo_statusXX": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_24(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "SLO_STATUS": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_25(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "XXslo_delta_msXX": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_26(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "SLO_DELTA_MS": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_27(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "XXsample_countXX": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_28(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "SAMPLE_COUNT": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_29(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_30(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_31(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXendpointXX": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_32(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"ENDPOINT": endpoint, "error": str(exc)}


def x_p99_latency__mutmut_33(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "XXerrorXX": str(exc)}


def x_p99_latency__mutmut_34(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "ERROR": str(exc)}


def x_p99_latency__mutmut_35(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,  # type: ignore
                slo_threshold_ms=slo_threshold_ms,  # type: ignore
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(None)}

mutants_x_p99_latency__mutmut['_mutmut_orig'] = x_p99_latency__mutmut_orig # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_1'] = x_p99_latency__mutmut_1 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_2'] = x_p99_latency__mutmut_2 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_3'] = x_p99_latency__mutmut_3 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_4'] = x_p99_latency__mutmut_4 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_5'] = x_p99_latency__mutmut_5 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_6'] = x_p99_latency__mutmut_6 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_7'] = x_p99_latency__mutmut_7 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_8'] = x_p99_latency__mutmut_8 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_9'] = x_p99_latency__mutmut_9 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_10'] = x_p99_latency__mutmut_10 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_11'] = x_p99_latency__mutmut_11 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_12'] = x_p99_latency__mutmut_12 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_13'] = x_p99_latency__mutmut_13 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_14'] = x_p99_latency__mutmut_14 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_15'] = x_p99_latency__mutmut_15 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_16'] = x_p99_latency__mutmut_16 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_17'] = x_p99_latency__mutmut_17 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_18'] = x_p99_latency__mutmut_18 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_19'] = x_p99_latency__mutmut_19 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_20'] = x_p99_latency__mutmut_20 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_21'] = x_p99_latency__mutmut_21 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_22'] = x_p99_latency__mutmut_22 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_23'] = x_p99_latency__mutmut_23 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_24'] = x_p99_latency__mutmut_24 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_25'] = x_p99_latency__mutmut_25 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_26'] = x_p99_latency__mutmut_26 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_27'] = x_p99_latency__mutmut_27 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_28'] = x_p99_latency__mutmut_28 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_29'] = x_p99_latency__mutmut_29 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_30'] = x_p99_latency__mutmut_30 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_31'] = x_p99_latency__mutmut_31 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_32'] = x_p99_latency__mutmut_32 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_33'] = x_p99_latency__mutmut_33 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_34'] = x_p99_latency__mutmut_34 # type: ignore # mutmut generated
mutants_x_p99_latency__mutmut['x_p99_latency__mutmut_35'] = x_p99_latency__mutmut_35 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(p99_latency)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(p99_latency)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
