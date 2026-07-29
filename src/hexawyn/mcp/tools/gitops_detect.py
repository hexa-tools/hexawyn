"""MCP tool: gitops_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_detect.command import GitopsDetectCommand
from hexawyn.application.use_case.gitops.gitops_detect.gitops_detect_use_case import (
    GitopsDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsDetectUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "apps_count": response.apps_count,
            "out_of_sync_count": response.out_of_sync_count,
            "failed_count": response.failed_count,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": "",
            "namespace": "",
            "apps_count": 0,
            "out_of_sync_count": 0,
            "failed_count": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_detect)
