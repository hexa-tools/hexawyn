"""MCP tool: list_namespaces — List all namespaces with age overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.use_case.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_namespaces() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview.

    Returns a dict with:
    - namespaces: list of {name, status, age}
    - error: error message if cluster is unreachable (None otherwise)
    """
    from hexawyn.application.service.list_namespaces_service import ListNamespacesService
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case: ListNamespacesUseCase = ListNamespacesService(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    """Register list_namespaces as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_namespaces)
