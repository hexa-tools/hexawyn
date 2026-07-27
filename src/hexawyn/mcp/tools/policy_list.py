"""MCP tool: policy_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_list.command import PolicyListCommand
from hexawyn.application.use_case.governance.policy_list.policy_list_use_case import (
    PolicyListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_list)
