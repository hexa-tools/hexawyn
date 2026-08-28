"""MCP tool: get_cilium_status — Cilium datapath health & connectivity."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.get_cilium_status.command import (
    GetCiliumStatusCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_status.get_cilium_status_use_case import (
    GetCiliumStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_cilium_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumStatusUseCase(port=adapter)
        result = use_case.execute(GetCiliumStatusCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "degraded_summary": result.degraded_summary,
            "controller_errors": result.controller_errors,
            "connectivity": result.connectivity,
            "nodes": result.nodes,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "degraded_summary": None,
            "controller_errors": 0,
            "connectivity": None,
            "nodes": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_status)
