"""MCP tool: policy_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.policy_detect.command import PolicyDetectCommand
from hexawyn.application.use_case.policy_detect.policy_detect_use_case import PolicyDetectUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_detect)
