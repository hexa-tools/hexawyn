"""MCP tool: audit_rbac_permissions — flags service accounts bound to
cluster-admin, wildcard verbs, or all resources, and suggests a minimal
Role/ClusterRole replacement for each."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.use_case.audit_rbac_permissions.audit_rbac_permissions_use_case import (
    AuditRBACPermissionsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_rbac_permissions(window_days: int = 30) -> dict[str, object]:
    from hexawyn.application.service.audit_rbac_permissions_service import (
        ServiceAccountRBACAuditService,
    )
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        service = ServiceAccountRBACAuditService(rbac_port=build_rbac_audit_adapter())
        r = AuditRBACPermissionsUseCase(service=service).execute(
            AuditRBACPermissionsCommand(window_days=window_days)
        )
        return {
            "findings": r.findings,
            "unused_service_accounts": r.unused_service_accounts,
            "excluded_system_service_accounts": r.excluded_system_service_accounts,
            "total_service_accounts_checked": r.total_service_accounts_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_rbac_permissions)
