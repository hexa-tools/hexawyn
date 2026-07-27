"""MCP tool: audit_rbac_permissions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
    AuditRbacPermissionsUseCase,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.command import (
    AuditRbacPermissionsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_rbac_permissions(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_rbac_permissions)
