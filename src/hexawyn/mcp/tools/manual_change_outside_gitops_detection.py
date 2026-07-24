"""MCP tool: manual_change_outside_gitops_detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.manual_change_outside_gitops.command import (
    ManualChangeOutsideGitopsCommand,
)
from hexawyn.application.use_case.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (
    ManualChangeOutsideGitopsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_manual_changes_outside_gitops(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_kustomize_drift_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(port=build_kustomize_drift_adapter())
        use_case.execute(ManualChangeOutsideGitopsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_manual_changes_outside_gitops)
