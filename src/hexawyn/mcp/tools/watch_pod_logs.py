# mypy: ignore-errors
"""MCP tool: watch_pod_logs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.watch_pod_logs.command import WatchPodLogsCommand
from hexawyn.application.use_case.troubleshooting.watch_pod_logs.watch_pod_logs_use_case import (
    WatchPodLogsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def watch_pod_logs(
    pod_name: str = "test-pod_name", namespace: str = "test-ns"
) -> dict[str, object]:  # type: ignore[no-untyped-def]  # noqa: E501
    from hexawyn.mcp.server import build_alert_notification_adapter

    try:
        use_case = WatchPodLogsUseCase(pod_log_watch_port=build_alert_notification_adapter())  # type: ignore
        _ = use_case.execute(WatchPodLogsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(watch_pod_logs)
