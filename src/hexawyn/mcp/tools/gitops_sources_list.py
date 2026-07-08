"""MCP tool: gitops_sources_list — List GitOps sources (GitRepository, HelmRepository, Bucket)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_command import (
    GitOpsSourcesListCommand,
)
from hexawyn.application.use_case.gitops_sources_list.gitops_sources_list_use_case import (
    GitOpsSourcesListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_sources_list(namespace: str | None = None) -> dict[str, object]:
    """List all GitOps sources (GitRepository, HelmRepository, Bucket).

    Args:
        namespace: Optional namespace filter.
    """
    from hexawyn.application.service.gitops_sources_list_service import (
        GitOpsSourcesListService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsSourcesListService(gitops_port=adapter)
        use_case = GitOpsSourcesListUseCase(service=service)
        response = use_case.execute(GitOpsSourcesListCommand(namespace=namespace))
        return {"sources": response.sources, "error": response.error}
    except Exception as exc:
        return {"sources": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_sources_list)
