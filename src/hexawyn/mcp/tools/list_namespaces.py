"""MCP tool: list_namespaces — List all namespaces with age overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.list_namespaces.command import ListNamespacesCommand
from hexawyn.application.use_case.cluster.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_namespaces() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_namespaces)
