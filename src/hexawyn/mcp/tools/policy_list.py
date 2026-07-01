"""MCP tool: policy_list — List all policies (ClusterPolicy/ConstraintTemplate)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.policy_list.policy_list_command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.policy_list.policy_list_use_case import (
    PolicyListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_list(namespace: str | None = None) -> dict[str, object]:
    """List all policies with action, violations count, and readiness."""
    from hexawyn.application.service.policy_list_service import PolicyListService
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        service = PolicyListService(policy_port=adapter)
        use_case = PolicyListUseCase(service=service)
        r = use_case.execute(PolicyListCommand(namespace=namespace))
        return {"policies": r.policies, "error": r.error}
    except Exception as exc:
        return {"policies": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_list)
