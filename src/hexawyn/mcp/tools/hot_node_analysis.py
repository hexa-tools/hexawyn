"""MCP tool: hot_node_analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.hot_node_analysis.command import HotNodeAnalysisCommand
from hexawyn.application.use_case.cluster.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def hot_node_analysis() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(hot_node_analysis)
