"""MCP tool: gitops_source_get — Get detailed status of a specific GitOps source."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_command import (
    GitOpsSourceGetCommand,
)
from hexawyn.application.use_case.gitops_source_get.gitops_source_get_use_case import (
    GitOpsSourceGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_source_get(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific GitOps source (GitRepository, HelmRepository, etc.).

    Args:
        name: Source name.
        namespace: Source namespace.
    """
    from hexawyn.application.service.gitops_source_get_service import (
        GitOpsSourceGetService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsSourceGetService(gitops_port=adapter)
        use_case = GitOpsSourceGetUseCase(service=service)
        response = use_case.execute(GitOpsSourceGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "kind": response.kind,
            "url": response.url,
            "ready": response.ready,
            "last_updated_at": response.last_updated_at,
            "message": response.message,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_source_get)
