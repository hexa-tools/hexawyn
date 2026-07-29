"""MCP tool: policy_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_detect.command import PolicyDetectCommand
from hexawyn.application.use_case.governance.policy_detect.policy_detect_use_case import (
    PolicyDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_detect)
