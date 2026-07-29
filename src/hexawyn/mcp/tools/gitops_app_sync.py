# mypy: ignore-errors
"""MCP tool: gitops_app_sync."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_app_sync.command import GitopsAppSyncCommand
from hexawyn.application.use_case.gitops.gitops_app_sync.gitops_app_sync_use_case import (
    GitopsAppSyncUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_sync(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(gitops_app_sync)
