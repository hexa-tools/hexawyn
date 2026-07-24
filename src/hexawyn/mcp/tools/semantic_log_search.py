"""MCP tool: semantic_log_search."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.semantic_log_search.command import SemanticLogSearchCommand
from hexawyn.application.use_case.semantic_log_search.semantic_log_search_use_case import (
    SemanticLogSearchUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def semantic_log_search(pattern="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SemanticLogSearchUseCase(port=build_k8s_adapter())
        _ = use_case.execute(SemanticLogSearchCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(semantic_log_search)
