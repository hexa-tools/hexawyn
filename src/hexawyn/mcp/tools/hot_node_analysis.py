"""MCP tool: hot_node_analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.hot_node_analysis.command import HotNodeAnalysisCommand
from hexawyn.application.use_case.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def hot_node_analysis() -> dict[str, object]:
    from hexawyn.mcp.server import build_node_analysis_adapter

    try:
        use_case = HotNodeAnalysisUseCase(port=build_node_analysis_adapter())
        _ = use_case.execute(HotNodeAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(hot_node_analysis)
