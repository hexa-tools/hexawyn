"""MCP tool: slowest_traces — Find the slowest OTel traces for a pod."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.slowest_traces.slowest_traces_use_case import SlowestTracesUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def slowest_traces(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name, time_window_minutes=time_window_minutes, top_n=top_n
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(slowest_traces)
