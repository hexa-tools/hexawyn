"""MCP tool: hot_node_analysis — identifies nodes consistently above 80% CPU
or memory, their top resource-consuming pods, and whether redistribution,
vertical scaling, or adding a node is the right fix."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def hot_node_analysis(window_hours: int = 24) -> dict[str, object]:
    from hexawyn.application.service.hot_node_analysis_service import HotNodeAnalysisService
    from hexawyn.mcp.server import build_metrics_query_adapter, build_node_analysis_adapter

    try:
        service = HotNodeAnalysisService(
            metrics_port=build_metrics_query_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        r = HotNodeAnalysisUseCase(service=service).execute(
            HotNodeAnalysisCommand(window_hours=window_hours)
        )
        return {
            "hot_nodes": r.hot_nodes,
            "healthy_node_count": r.healthy_node_count,
            "excluded_cordoned_nodes": r.excluded_cordoned_nodes,
            "warnings": r.warnings,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(hot_node_analysis)
