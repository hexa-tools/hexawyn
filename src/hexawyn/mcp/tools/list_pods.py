"""MCP tool: list_pods — List all pods in a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.list_pods.list_pods_command import ListPodsCommand
from hexawyn.application.use_case.list_pods.list_pods_use_case import ListPodsUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_pods(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview.

    Args:
        namespace: The Kubernetes namespace to list pods from.
    """
    from hexawyn.application.service.list_pods_service import ListPodsService
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        service = ListPodsService(k8s_port=adapter)
        use_case = ListPodsUseCase(service=service)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    """Register list_pods as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_pods)
