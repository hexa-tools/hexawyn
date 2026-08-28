"""MCP tool: cilium_service_graph — build a service graph from Cilium flows."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_service_graph.cilium_service_graph_use_case import (
    CiliumServiceGraphUseCase,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_service_graph(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_service_graph)
