"""MCP tool: manual_change_outside_gitops_detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
    ManualChangeOutsideGitopsCommand,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
    ManualChangeOutsideGitopsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_manual_changes_outside_gitops(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_manual_changes_outside_gitops)
