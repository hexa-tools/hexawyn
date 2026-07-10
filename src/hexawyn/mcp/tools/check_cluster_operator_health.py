"""MCP tool: check_cluster_operator_health — OpenShift ClusterOperator health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.check_cluster_operator_health.check_cluster_operator_health_use_case import (  # noqa: E501
    CheckClusterOperatorHealthUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_cluster_operator_health() -> dict[str, object]:
    """Check the health of all OpenShift ClusterOperators.

    Lists every ClusterOperator with its Available/Progressing/Degraded
    conditions, highlights Degraded and Progressing operators with their
    root-cause message, flags operators degraded for more than 15 minutes as
    chronic, and returns a summary (total, healthy, degraded, progressing).
    """
    from hexawyn.application.service.check_cluster_operator_health_service import (
        CheckClusterOperatorHealthService,
    )
    from hexawyn.mcp.server import build_cluster_operator_status_adapter

    try:
        adapter = build_cluster_operator_status_adapter()
        service = CheckClusterOperatorHealthService(operator_port=adapter)
        use_case = CheckClusterOperatorHealthUseCase(service=service)
        response = use_case.execute(CheckClusterOperatorHealthCommand())
        report = response.result
        return {
            "all_healthy": report.all_healthy,
            "total": report.total,
            "healthy": report.healthy,
            "degraded": report.degraded,
            "progressing": report.progressing,
            "operators": [
                {
                    "name": operator.name,
                    "available": operator.available,
                    "progressing": operator.progressing,
                    "degraded": operator.degraded,
                    "health": operator.health,
                    "message": operator.message,
                    "degraded_duration_minutes": operator.degraded_duration_minutes,
                    "is_chronic": operator.is_chronic,
                }
                for operator in report.operators
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "all_healthy": False,
            "total": 0,
            "healthy": 0,
            "degraded": 0,
            "progressing": 0,
            "operators": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_operator_health)
