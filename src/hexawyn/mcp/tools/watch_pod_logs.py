"""MCP tool: watch_pod_logs — real-time pod log watch with instant critical alerting."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.use_case.watch_pod_logs.watch_pod_logs_use_case import (
    WatchPodLogsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def watch_pod_logs(
    pod_name: str,
    namespace: str,
    timeout_seconds: int = 300,
    max_reconnect_attempts: int = 3,
    sample_rate: int = 100,
) -> dict[str, object]:
    from hexawyn.application.service.watch_pod_logs_service import WatchPodLogsService
    from hexawyn.mcp.server import build_alert_notification_adapter, build_pod_log_watch_adapter

    try:
        watch_adapter = build_pod_log_watch_adapter()
        alert_adapter = build_alert_notification_adapter()
        service = WatchPodLogsService(watch_port=watch_adapter, alert_port=alert_adapter)
        r = WatchPodLogsUseCase(service=service).execute(
            WatchPodLogsCommand(
                pod_name=pod_name,
                namespace=namespace,
                timeout_seconds=timeout_seconds,
                max_reconnect_attempts=max_reconnect_attempts,
                sample_rate=sample_rate,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "stop_reason": r.stop_reason,
            "lines_observed": r.lines_observed,
            "lines_sampled": r.lines_sampled,
            "reconnect_count": r.reconnect_count,
            "confidence": r.confidence,
            "summary": r.summary,
            "alerts": r.alerts,
            "patterns": r.patterns,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(watch_pod_logs)
