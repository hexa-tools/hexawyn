# mypy: ignore-errors
"""MCP tool: policy_explain_denial."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.governance.policy_explain_denial.policy_explain_denial_use_case import (  # noqa: E501
    PolicyExplainDenialUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_explain_denial(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(policy_explain_denial)
