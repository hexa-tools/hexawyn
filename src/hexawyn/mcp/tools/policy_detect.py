"""MCP tool: policy_detect — Detect Kyverno or OPA Gatekeeper."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.policy_detect.policy_detect_command import (
    PolicyDetectCommand,
)
from hexawyn.application.use_case.policy_detect.policy_detect_use_case import (
    PolicyDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_detect() -> dict[str, object]:
    """Detect which policy engine is installed (Kyverno or OPA Gatekeeper)."""
    from hexawyn.application.service.policy_detect_service import PolicyDetectService
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        service = PolicyDetectService(policy_port=adapter)
        use_case = PolicyDetectUseCase(service=service)
        r = use_case.execute(PolicyDetectCommand())
        return {
            "engine": r.engine,
            "version": r.version,
            "namespace": r.namespace,
            "total_policies": r.total_policies,
            "enforce_policies": r.enforce_policies,
            "audit_policies": r.audit_policies,
            "total_violations": r.total_violations,
            "high_severity": r.high_severity,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "engine": "unknown",
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
