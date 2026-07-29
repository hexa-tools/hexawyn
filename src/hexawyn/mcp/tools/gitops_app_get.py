"""MCP tool: gitops_app_get — Get ArgoCD/Flux application details."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_app_get.command import GitopsAppGetCommand
from hexawyn.application.use_case.gitops.gitops_app_get.gitops_app_get_use_case import (
    GitopsAppGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_get(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_get)
