# mypy: ignore-errors
"""MCP tool: semantic_log_search."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.semantic_log_search.command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.observability.semantic_log_search.semantic_log_search_use_case import (  # noqa: E501
    SemanticLogSearchUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def semantic_log_search(pattern: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SemanticLogSearchUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SemanticLogSearchCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(semantic_log_search)
