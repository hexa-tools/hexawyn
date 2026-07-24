"""MCP tool: query_kubearchive."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.query_kubearchive.command import QueryKubearchiveCommand
from hexawyn.application.use_case.query_kubearchive.query_kubearchive_use_case import (
    QueryKubeArchiveUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def query_kubearchive(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())
        _ = use_case.execute(QueryKubearchiveCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(query_kubearchive)
