"""MCP tool: detect_manual_changes_outside_gitops — flags ConfigMap/Secret
writes made by a human or CI service account rather than a GitOps controller
(ArgoCD/Flux), within a trailing window."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.use_case.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (
    ManualChangeOutsideGitOpsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_manual_changes_outside_gitops(namespace: str, window_days: int = 7) -> dict[str, object]:
    from hexawyn.application.service.manual_change_outside_gitops_service import (
        ManualChangeOutsideGitOpsService,
    )
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        service = ManualChangeOutsideGitOpsService(audit_port=build_audit_log_adapter())
        r = ManualChangeOutsideGitOpsUseCase(service=service).execute(
            ManualChangeOutsideGitOpsCommand(namespace=namespace, window_days=window_days)
        )
        return {
            "manual_changes": r.manual_changes,
            "total_manual_changes": r.total_manual_changes,
            "excluded_gitops_change_count": r.excluded_gitops_change_count,
            "used_managed_fields_fallback": r.used_managed_fields_fallback,
            "partial_window": r.partial_window,
            "notes": r.notes,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_manual_changes_outside_gitops)
