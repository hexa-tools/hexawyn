"""MCP tool: policy_explain_denial — Explain why a resource was rejected."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.policy_explain_denial.policy_explain_denial_use_case import (
    PolicyExplainDenialUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_explain_denial(
    resource_kind: str, resource_name: str, namespace: str
) -> dict[str, object]:
    """Explain in natural language why a resource was rejected by the policy engine."""
    from hexawyn.application.service.policy_explain_denial_service import (
        PolicyExplainDenialService,
    )
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        service = PolicyExplainDenialService(policy_port=adapter)
        use_case = PolicyExplainDenialUseCase(service=service)
        r = use_case.execute(
            PolicyExplainDenialCommand(
                resource_kind=resource_kind,
                resource_name=resource_name,
                namespace=namespace,
            )
        )
        return {
            "policy_name": r.policy_name,
            "rule_name": r.rule_name,
            "raw_message": r.raw_message,
            "human_explanation": r.human_explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "policy_name": "",
            "rule_name": "",
            "raw_message": "",
            "human_explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_explain_denial)
