# mypy: ignore-errors
"""MCP tool: etcd_logs — Retrieve etcd logs with anomaly detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.etcd_logs.command import (
    ETCDLogsCommand,
)
from hexawyn.application.use_case.observability.etcd_logs.etcd_logs_use_case import ETCDLogsUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def etcd_logs(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_etcd_logs_adapter

    try:
        a = build_etcd_logs_adapter()
        r = ETCDLogsUseCase(port=a).execute(
            ETCDLogsCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "etcd_accessible": r.etcd_accessible,
            "total_log_lines": r.total_log_lines,
            "error_count": r.error_count,
            "leader_election_count": r.leader_election_count,
            "compaction_errors": r.compaction_errors,
            "leader_instability": r.leader_instability,
            "summary": r.summary,
            "errors": r.errors,
            "error": r.error,
        }
    except Exception as exc:
        return {"etcd_accessible": False, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(etcd_logs)
