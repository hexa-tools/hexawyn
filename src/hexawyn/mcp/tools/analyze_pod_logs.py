"""MCP tool: analyze_pod_logs — Strategy-pattern log analysis for a pod over a time window."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.analyze_pod_logs.analyze_pod_logs_use_case import (
    AnalyzePodLogsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_pod_logs(
    pod_name: str, namespace: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.application.service.analyze_pod_logs_service import AnalyzePodLogsService
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        adapter = build_pod_logs_adapter()
        r = AnalyzePodLogsUseCase(service=AnalyzePodLogsService(port=adapter)).execute(
            AnalyzePodLogsCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
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


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_pod_logs)
