# mypy: ignore-errors
"""MCP tool: diff_cluster_resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.diff_cluster_resources.command import (
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.diff_cluster_resources_use_case import (  # noqa: E501
    DiffClusterResourcesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def diff_cluster_resources(
    source_context: str = "test", target_context: str = "test"
) -> dict[str, object]:  # type: ignore[no-untyped-def]  # noqa: E501
    from hexawyn.mcp.server import build_cluster_diff_adapter

    try:
        service = DiffClusterResourcesUseCase(cluster_diff_port=build_cluster_diff_adapter())
        use_case = DiffClusterResourcesUseCase(service=service)  # type: ignore
        _ = use_case.execute(DiffClusterResourcesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(diff_cluster_resources)
