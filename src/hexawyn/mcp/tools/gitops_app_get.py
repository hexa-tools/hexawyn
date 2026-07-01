"""MCP tool: gitops_app_get — Get detailed status of a specific GitOps application."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_command import (
    GitOpsAppGetCommand,
)
from hexawyn.application.use_case.gitops_app_get.gitops_app_get_use_case import (
    GitOpsAppGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_get(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific GitOps application.

    Args:
        name: Application name.
        namespace: Namespace where the application is defined.
    """
    from hexawyn.application.service.gitops_app_get_service import GitOpsAppGetService
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsAppGetService(gitops_port=adapter)
        use_case = GitOpsAppGetUseCase(service=service)
        response = use_case.execute(GitOpsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "last_synced_at": response.last_synced_at,
            "last_commit": response.last_commit,
            "source_url": response.source_url,
            "revision": response.revision,
            "message": response.message,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_get)
