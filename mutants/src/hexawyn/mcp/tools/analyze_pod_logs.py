"""MCP tool: analyze_pod_logs — Strategy-pattern log analysis for a pod over a time window."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.analyze_pod_logs.analyze_pod_logs_use_case import (
    AnalyzePodLogsUseCase,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_pod_logs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_pod_logs__mutmut)
def analyze_pod_logs(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_orig(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_1(
    pod_name: str, namespace: str, time_window_minutes: int = 31
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_2(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = None
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_3(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = None
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_4(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            None
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_5(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=None).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_6(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=None, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_7(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=None, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_8(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=None
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_9(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_10(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_11(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_12(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "XXpod_nameXX": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_13(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "POD_NAME": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_14(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "XXnamespaceXX": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_15(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "NAMESPACE": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_16(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "XXtime_window_minutesXX": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_17(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "TIME_WINDOW_MINUTES": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_18(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "XXstrategy_usedXX": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_19(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "STRATEGY_USED": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_20(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "XXtotal_linesXX": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_21(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "TOTAL_LINES": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_22(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "XXerror_countXX": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_23(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "ERROR_COUNT": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_24(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "XXwarning_countXX": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_25(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "WARNING_COUNT": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_26(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "XXconfidenceXX": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_27(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "CONFIDENCE": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_28(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "XXsummaryXX": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_29(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "SUMMARY": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_30(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "XXrestarts_detectedXX": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_31(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "RESTARTS_DETECTED": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_32(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "XXsanitized_binaryXX": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_33(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "SANITIZED_BINARY": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_34(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "XXtoken_reduction_percentageXX": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_35(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "TOKEN_REDUCTION_PERCENTAGE": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_36(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "XXdegradedXX": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_37(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "DEGRADED": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_38(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "XXpatternsXX": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_39(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "PATTERNS": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_40(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "XXconnection_timeoutsXX": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_41(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "CONNECTION_TIMEOUTS": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_42(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "XXconnection_refusedXX": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_43(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "CONNECTION_REFUSED": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_44(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "XXrunsXX": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_45(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "RUNS": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_46(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "XXranked_eventsXX": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_47(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "RANKED_EVENTS": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_48(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_49(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_50(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXpod_nameXX": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_51(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"POD_NAME": pod_name, "namespace": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_52(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "XXnamespaceXX": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_53(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "NAMESPACE": namespace, "error": str(exc)}


def x_analyze_pod_logs__mutmut_54(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "XXerrorXX": str(exc)}


def x_analyze_pod_logs__mutmut_55(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "ERROR": str(exc)}


def x_analyze_pod_logs__mutmut_56(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(port=adapter).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name, namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "strategy_used": r.strategy_used,
            "total_lines": r.total_lines,
            "error_count": r.error_count,
            "warning_count": r.warning_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "restarts_detected": r.restarts_detected,
            "sanitized_binary": r.sanitized_binary,
            "token_reduction_percentage": r.token_reduction_percentage,
            "degraded": r.degraded,
            "patterns": r.patterns,
            "connection_timeouts": r.connection_timeouts,
            "connection_refused": r.connection_refused,
            "runs": r.runs,
            "ranked_events": r.ranked_events,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(None)}

mutants_x_analyze_pod_logs__mutmut['_mutmut_orig'] = x_analyze_pod_logs__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_1'] = x_analyze_pod_logs__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_2'] = x_analyze_pod_logs__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_3'] = x_analyze_pod_logs__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_4'] = x_analyze_pod_logs__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_5'] = x_analyze_pod_logs__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_6'] = x_analyze_pod_logs__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_7'] = x_analyze_pod_logs__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_8'] = x_analyze_pod_logs__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_9'] = x_analyze_pod_logs__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_10'] = x_analyze_pod_logs__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_11'] = x_analyze_pod_logs__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_12'] = x_analyze_pod_logs__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_13'] = x_analyze_pod_logs__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_14'] = x_analyze_pod_logs__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_15'] = x_analyze_pod_logs__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_16'] = x_analyze_pod_logs__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_17'] = x_analyze_pod_logs__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_18'] = x_analyze_pod_logs__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_19'] = x_analyze_pod_logs__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_20'] = x_analyze_pod_logs__mutmut_20 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_21'] = x_analyze_pod_logs__mutmut_21 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_22'] = x_analyze_pod_logs__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_23'] = x_analyze_pod_logs__mutmut_23 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_24'] = x_analyze_pod_logs__mutmut_24 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_25'] = x_analyze_pod_logs__mutmut_25 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_26'] = x_analyze_pod_logs__mutmut_26 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_27'] = x_analyze_pod_logs__mutmut_27 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_28'] = x_analyze_pod_logs__mutmut_28 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_29'] = x_analyze_pod_logs__mutmut_29 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_30'] = x_analyze_pod_logs__mutmut_30 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_31'] = x_analyze_pod_logs__mutmut_31 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_32'] = x_analyze_pod_logs__mutmut_32 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_33'] = x_analyze_pod_logs__mutmut_33 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_34'] = x_analyze_pod_logs__mutmut_34 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_35'] = x_analyze_pod_logs__mutmut_35 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_36'] = x_analyze_pod_logs__mutmut_36 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_37'] = x_analyze_pod_logs__mutmut_37 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_38'] = x_analyze_pod_logs__mutmut_38 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_39'] = x_analyze_pod_logs__mutmut_39 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_40'] = x_analyze_pod_logs__mutmut_40 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_41'] = x_analyze_pod_logs__mutmut_41 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_42'] = x_analyze_pod_logs__mutmut_42 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_43'] = x_analyze_pod_logs__mutmut_43 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_44'] = x_analyze_pod_logs__mutmut_44 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_45'] = x_analyze_pod_logs__mutmut_45 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_46'] = x_analyze_pod_logs__mutmut_46 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_47'] = x_analyze_pod_logs__mutmut_47 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_48'] = x_analyze_pod_logs__mutmut_48 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_49'] = x_analyze_pod_logs__mutmut_49 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_50'] = x_analyze_pod_logs__mutmut_50 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_51'] = x_analyze_pod_logs__mutmut_51 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_52'] = x_analyze_pod_logs__mutmut_52 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_53'] = x_analyze_pod_logs__mutmut_53 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_54'] = x_analyze_pod_logs__mutmut_54 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_55'] = x_analyze_pod_logs__mutmut_55 # type: ignore # mutmut generated
mutants_x_analyze_pod_logs__mutmut['x_analyze_pod_logs__mutmut_56'] = x_analyze_pod_logs__mutmut_56 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_pod_logs)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(analyze_pod_logs)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
