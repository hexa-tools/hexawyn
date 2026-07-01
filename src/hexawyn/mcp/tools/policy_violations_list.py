"""MCP tool: policy_violations_list — List current policy violations."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.policy_violations_list.policy_violations_list_use_case import (
    PolicyViolationsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_violations_list(namespace: str | None = None) -> dict[str, object]:
    """List current policy violations with severity and message."""
    from hexawyn.application.service.policy_violations_list_service import (
        PolicyViolationsListService,
    )
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        service = PolicyViolationsListService(policy_port=adapter)
        use_case = PolicyViolationsListUseCase(service=service)
        r = use_case.execute(PolicyViolationsListCommand(namespace=namespace))
        return {"violations": r.violations, "error": r.error}
    except Exception as exc:
        return {"violations": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_violations_list)
