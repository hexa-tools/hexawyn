"""MCP tool: sensitive_data_audit — Audit access to sensitive endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.sensitive_data_audit.command import SensitiveDataAuditCommand
from hexawyn.application.use_case.sensitive_data_audit.sensitive_data_audit_use_case import (
    SensitiveDataAuditUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def sensitive_data_audit(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(sensitive_data_audit)
