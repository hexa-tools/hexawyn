"""MCP tool: audit_tls_compliance — scan services for TLS/SSL certificate issues."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_command import (
    AuditTLSComplianceCommand,
)
from hexawyn.application.use_case.audit_tls_compliance.audit_tls_compliance_use_case import (
    AuditTLSComplianceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_tls_compliance() -> dict[str, object]:
    """Audit services for TLS compliance: expired certs, no TLS, self-signed.

    Returns all services with no TLS configured, expired certificates,
    or certificates expiring within 30 days, ranked by severity.

    """
    from hexawyn.application.service.audit_tls_compliance_service import (
        AuditTLSComplianceService,
    )
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        adapter = build_tls_compliance_adapter()
        service = AuditTLSComplianceService(tls_port=adapter)
        use_case = AuditTLSComplianceUseCase(service=service)
        response = use_case.execute(AuditTLSComplianceCommand())
        r = response.result
        return {
            "all_compliant": r.all_compliant,
            "total_issues": r.total_issues,
            "services": [
                {
                    "service_name": s.service_name,
                    "namespace": s.namespace,
                    "tls_configured": s.tls_configured,
                    "cert_expiry_days": s.cert_expiry_days,
                    "days_remaining": s.days_remaining,
                    "severity": s.severity,
                    "cert_issuer": s.cert_issuer,
                    "is_self_signed": s.is_self_signed,
                    "proxy_tls_termination": s.proxy_tls_termination,
                }
                for s in r.services
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "all_compliant": False,
            "total_issues": 0,
            "services": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_tls_compliance)
