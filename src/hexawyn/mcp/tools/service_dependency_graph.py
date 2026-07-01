"""MCP tool: service_dependency_graph — Build dependency graph from OTel traces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.service_dependency_graph.service_dependency_graph_use_case import (
    ServiceDependencyGraphUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def service_dependency_graph(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.application.service.service_dependency_graph_service import (
        ServiceDependencyGraphService,
    )
    from hexawyn.mcp.server import build_service_dependency_graph_adapter

    try:
        a = build_service_dependency_graph_adapter()
        r = ServiceDependencyGraphUseCase(service=ServiceDependencyGraphService(port=a)).execute(
            ServiceDependencyGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "nodes": r.nodes,
            "edges": r.edges,
            "error": r.error,
        }
    except Exception as exc:
        return {"nodes": [], "edges": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(service_dependency_graph)
