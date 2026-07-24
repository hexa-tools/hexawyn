"""MCP tool: gitops_app_sync."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_app_sync.command import GitopsAppSyncCommand
from hexawyn.application.use_case.gitops_app_sync.gitops_app_sync_use_case import (
    GitopsAppSyncUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_sync(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_sync)
