"""MCP tool: policy_audit — Global compliance audit report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.policy_audit.command import PolicyAuditCommand
from hexawyn.application.use_case.policy_audit.policy_audit_use_case import PolicyAuditUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_audit(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_audit)
