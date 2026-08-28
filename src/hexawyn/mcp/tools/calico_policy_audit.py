"""MCP tool: calico_policy_audit — audit Calico L3/L4 coverage gaps."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_policy_audit.calico_policy_audit_use_case import (
    CalicoPolicyAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _gap_dict(gap: object) -> dict[str, object]:
    """Project a CalicoCoverageGap into a plain, serialisable dict."""
    return {
        "namespace": getattr(gap, "namespace", None),
        "workload_count": getattr(gap, "workload_count", 0),
        "policy_count": getattr(gap, "policy_count", 0),
        "issue": getattr(gap, "issue", None),
        "network_status": getattr(gap, "network_status", None),
        "risk_level": getattr(gap, "risk_level", None),
        "selectors": list(getattr(gap, "selectors", ())),
        "note": getattr(gap, "note", None),
    }


def calico_policy_audit(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoPolicyAuditUseCase(port=build_calico_adapter())
        command = CalicoPolicyAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "degraded_to_vanilla": result.degraded_to_vanilla,
            "total_namespaces_checked": result.total_namespaces_checked,
            "gap_count": result.gap_count,
            "findings": [_gap_dict(finding) for finding in result.findings],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "degraded_to_vanilla": True,
            "total_namespaces_checked": 0,
            "gap_count": 0,
            "findings": [],
            "summary": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_policy_audit)
