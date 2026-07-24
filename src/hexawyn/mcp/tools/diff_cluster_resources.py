"""MCP tool: diff_cluster_resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.diff_cluster_resources.command import DiffClusterResourcesCommand
from hexawyn.application.use_case.diff_cluster_resources.diff_cluster_resources_use_case import (
    DiffClusterResourcesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def diff_cluster_resources(source_context="test", target_context="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_cluster_diff_adapter

    try:
        use_case = DiffClusterResourcesUseCase(cluster_diff_port=build_cluster_diff_adapter())
        _ = use_case.execute(DiffClusterResourcesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(diff_cluster_resources)
