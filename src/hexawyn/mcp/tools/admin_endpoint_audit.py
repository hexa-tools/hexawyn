"""MCP tool: admin_endpoint_audit — Audit failed /admin calls for security analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.use_case.admin_endpoint_audit.admin_endpoint_audit_use_case import (
    AdminEndpointAuditUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def admin_endpoint_audit(
    endpoint_pattern: str = "/admin*", time_window_minutes: int = 30, flag_threshold: int = 5
) -> dict[str, object]:
    from hexawyn.application.service.admin_endpoint_audit_service import AdminEndpointAuditService
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        a = build_security_audit_adapter()
        r = AdminEndpointAuditUseCase(service=AdminEndpointAuditService(port=a)).execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(admin_endpoint_audit)
