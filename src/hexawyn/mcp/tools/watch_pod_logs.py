"""MCP tool: watch_pod_logs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.watch_pod_logs.command import WatchPodLogsCommand
from hexawyn.application.use_case.watch_pod_logs.watch_pod_logs_use_case import WatchPodLogsUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def watch_pod_logs(pod_name="test-pod_name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_alert_notification_adapter

    try:
        use_case = WatchPodLogsUseCase(pod_log_watch_port=build_alert_notification_adapter())
        _ = use_case.execute(WatchPodLogsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(watch_pod_logs)
