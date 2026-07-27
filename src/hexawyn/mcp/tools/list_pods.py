"""MCP tool: list_pods — List all pods in a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.list_pods_use_case import ListPodsUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_pods(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_pods)
