"""MCP tool: policy_get."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.policy_get.command import PolicyGetCommand
from hexawyn.application.use_case.policy_get.policy_get_use_case import PolicyGetUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_get(name="test-name") -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_get)
