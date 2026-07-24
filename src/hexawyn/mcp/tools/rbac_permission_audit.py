"""MCP tool: audit_rbac_permissions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.audit_rbac_permissions.audit_rbac_permissions_use_case import (
    AuditRbacPermissionsUseCase,
)
from hexawyn.application.use_case.audit_rbac_permissions.command import AuditRbacPermissionsCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_rbac_permissions() -> dict[str, object]:
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())
        _ = use_case.execute(AuditRbacPermissionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_rbac_permissions)
