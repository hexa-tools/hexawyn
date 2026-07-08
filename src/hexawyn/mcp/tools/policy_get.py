"""MCP tool: policy_get — Get detail of a specific policy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.policy_get.policy_get_command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.policy_get.policy_get_use_case import (
    PolicyGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def policy_get(name: str, namespace: str | None = None) -> dict[str, object]:
    """Get detailed status of a specific policy."""
    from hexawyn.application.service.policy_get_service import PolicyGetService
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        service = PolicyGetService(policy_port=adapter)
        use_case = PolicyGetUseCase(service=service)
        r = use_case.execute(PolicyGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "engine": r.engine,
            "kind": r.kind,
            "action": r.action,
            "description": r.description,
            "rules_count": r.rules_count,
            "violations_count": r.violations_count,
            "ready": r.ready,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_get)
