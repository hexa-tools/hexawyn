"""MCP tool: check_cluster_operator_health — Check cluster operator health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.check_cluster_operator_health.check_cluster_operator_health_use_case import (
    CheckClusterOperatorHealthUseCase,
)
from hexawyn.application.use_case.check_cluster_operator_health.command import (
    CheckClusterOperatorHealthCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_cluster_operator_health() -> dict[str, object]:
    from hexawyn.mcp.server import build_cluster_operator_status_adapter

    try:
        use_case = CheckClusterOperatorHealthUseCase(
            operator_port=build_cluster_operator_status_adapter()
        )
        _ = use_case.execute(CheckClusterOperatorHealthCommand())
        return {"operators": [], "error": None}
    except Exception as exc:
        return {"operators": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_operator_health)
