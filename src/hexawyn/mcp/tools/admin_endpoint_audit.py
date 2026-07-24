"""MCP tool: admin_endpoint_audit — Audit admin endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.admin_endpoint_audit.admin_endpoint_audit_use_case import (
    AdminEndpointAuditUseCase,
)
from hexawyn.application.use_case.admin_endpoint_audit.command import AdminEndpointAuditCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def admin_endpoint_audit(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(AdminEndpointAuditCommand(namespace=namespace))
        return {"endpoints": r.endpoints, "error": r.error}
    except Exception as exc:
        return {"endpoints": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(admin_endpoint_audit)
