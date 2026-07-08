"""MCP tool: gitops_detect — Auto-detect which GitOps engine is installed in the cluster."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.gitops_detect.gitops_detect_command import (
    GitOpsDetectCommand,
)
from hexawyn.application.use_case.gitops_detect.gitops_detect_use_case import (
    GitOpsDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_detect() -> dict[str, object]:
    """Detect which GitOps engine (Flux CD or Argo CD) is installed in the cluster.

    Returns engine type, version, namespace, and app counts.
    """
    from hexawyn.application.service.gitops_detect_service import (
        GitOpsDetectService,
    )
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        adapter = build_gitops_adapter()
        service = GitOpsDetectService(gitops_port=adapter)
        use_case = GitOpsDetectUseCase(service=service)
        response = use_case.execute(GitOpsDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "apps_count": response.apps_count,
            "out_of_sync_count": response.out_of_sync_count,
            "failed_count": response.failed_count,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "engine": "unknown",
            "version": None,
            "namespace": None,
            "apps_count": 0,
            "out_of_sync_count": 0,
            "failed_count": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register gitops_detect as an MCP tool."""
    mcp.tool()(gitops_detect)
