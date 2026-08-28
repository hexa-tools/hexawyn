"""MCP tool: get_cilium_flows — query Cilium flow logs via Hubble."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.get_cilium_flows_use_case import (
    GetCiliumFlowsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_cilium_flows(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_flows)
