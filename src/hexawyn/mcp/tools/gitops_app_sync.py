"""MCP tool: gitops_app_sync — Read-only sync status of a GitOps app (never triggers sync)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_command import (
    GitOpsAppSyncCommand,
)
from hexawyn.application.use_case.gitops_app_sync.gitops_app_sync_use_case import (
    GitOpsAppSyncUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_sync(name: str, namespace: str) -> dict[str, object]:
    """Get the last sync status — read-only, never triggers a sync.

    Use `flux reconcile` or Argo CD UI to trigger a sync manually.

    Args:
        name: Application name.
        namespace: Application namespace.
    """
    from hexawyn.application.service.gitops_app_sync_service import (
        GitOpsAppSyncService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsAppSyncService(gitops_port=adapter)
        use_case = GitOpsAppSyncUseCase(service=service)
        response = use_case.execute(GitOpsAppSyncCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "sync_status": response.sync_status,
            "last_synced_at": response.last_synced_at,
            "revision": response.revision,
            "message": response.message,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_sync)
