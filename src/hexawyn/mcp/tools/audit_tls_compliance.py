"""MCP tool: audit_tls_compliance — scan services for TLS issues."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.audit_tls_compliance.audit_tls_compliance_use_case import (
    AuditTlsComplianceUseCase,
)
from hexawyn.application.use_case.audit_tls_compliance.command import AuditTlsComplianceCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_tls_compliance() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTlsComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_tls_compliance)
