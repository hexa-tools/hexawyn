"""MCP tool: cilium_detect — Detect if Cilium is the active CNI."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_detect.cilium_detect_use_case import (
    CiliumDetectUseCase,
)
from hexawyn.application.use_case.cilium.cilium_detect.command import (
    CiliumDetectCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumDetectUseCase(port=adapter)
        result = use_case.execute(CiliumDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "version": result.version,
            "mode": result.mode,
            "namespace": result.namespace,
            "total_agents": result.total_agents,
            "ready_agents": result.ready_agents,
            "degraded_summary": result.degraded_summary,
            "agents": result.agents,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "version": None,
            "mode": "UNKNOWN",
            "namespace": None,
            "total_agents": 0,
            "ready_agents": 0,
            "degraded_summary": None,
            "agents": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_detect)
