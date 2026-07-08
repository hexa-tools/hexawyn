"""MCP tool: gitops_apps_list — List all GitOps applications in the cluster."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_command import (
    GitOpsAppsListCommand,
)
from hexawyn.application.use_case.gitops_apps_list.gitops_apps_list_use_case import (
    GitOpsAppsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_apps_list(namespace: str | None = None) -> dict[str, object]:
    """List all GitOps applications (Flux HelmRelease/Kustomization or ArgoCD Application).

    Args:
        namespace: Optional namespace filter.
    """
    from hexawyn.application.service.gitops_apps_list_service import (
        GitOpsAppsListService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsAppsListService(gitops_port=adapter)
        use_case = GitOpsAppsListUseCase(service=service)
        response = use_case.execute(GitOpsAppsListCommand(namespace=namespace))
        return {"apps": response.apps, "error": response.error}
    except Exception as exc:
        return {"apps": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_apps_list)
