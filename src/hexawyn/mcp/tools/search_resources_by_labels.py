"""MCP tool: search_resources_by_labels."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.search_resources_by_labels.search_resources_by_labels_use_case import (
    SearchResourcesByLabelsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def search_resources_by_labels(label_selector="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(search_resources_by_labels)
