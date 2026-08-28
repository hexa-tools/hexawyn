"""MCP tool: cilium_policy_audit — Cilium policy coverage audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_policy_audit.cilium_policy_audit_use_case import (
    CiliumPolicyAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_policy_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumPolicyAuditUseCase(port=adapter)
        result = use_case.execute(CiliumPolicyAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "view": result.view,
            "total_workloads": result.total_workloads,
            "uncovered_count": result.uncovered_count,
            "findings": result.findings,
            "summary": result.summary,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "view": "vanilla",
            "total_workloads": 0,
            "uncovered_count": 0,
            "findings": [],
            "summary": "",
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_policy_audit)
