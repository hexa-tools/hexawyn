"""MCP tool: check_cluster_operator_health — Check cluster operator health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.check_cluster_operator_health.check_cluster_operator_health_use_case import (  # noqa: E501
    CheckClusterOperatorHealthUseCase,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.command import (
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
        response = use_case.execute(CheckClusterOperatorHealthCommand())
        operators_list = [
            {
                "name": op.name,
                "available": op.available,
                "progressing": op.progressing,
                "degraded": op.degraded,
                "health": op.health,
                "message": op.message,
                "degraded_duration_minutes": op.degraded_duration_minutes,
                "is_chronic": op.is_chronic,
            }
            for op in response.result.operators
        ]
        return {
            "total": response.result.total,
            "healthy": response.result.healthy,
            "degraded": response.result.degraded,
            "progressing": response.result.progressing,
            "all_healthy": response.result.all_healthy,
            "operators": operators_list,
            "error": None,
        }
    except Exception as exc:
        return {
            "total": 0,
            "healthy": 0,
            "degraded": 0,
            "progressing": 0,
            "all_healthy": False,
            "operators": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_operator_health)
