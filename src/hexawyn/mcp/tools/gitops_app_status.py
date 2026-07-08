"""MCP tool: gitops_app_status — Get sync + health status of a GitOps app."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_command import (
    GitOpsAppStatusCommand,
)
from hexawyn.application.use_case.gitops_app_status.gitops_app_status_use_case import (
    GitOpsAppStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_status(name: str, namespace: str) -> dict[str, object]:
    """Get sync and health status with last reconciliation timestamp.

    Args:
        name: Application name.
        namespace: Application namespace.
    """
    from hexawyn.application.service.gitops_app_status_service import (
        GitOpsAppStatusService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsAppStatusService(gitops_port=adapter)
        use_case = GitOpsAppStatusUseCase(service=service)
        response = use_case.execute(GitOpsAppStatusCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "last_synced_at": response.last_synced_at,
            "last_commit": response.last_commit,
            "revision": response.revision,
            "message": response.message,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_status)
