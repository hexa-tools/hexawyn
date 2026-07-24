"""MCP tool: policy_violations_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.policy_violations_list.command import PolicyViolationsListCommand
from hexawyn.application.use_case.policy_violations_list.policy_violations_list_use_case import (
    PolicyViolationsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_violations_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_violations_list)
