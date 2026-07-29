"""MCP tool: compute_team_cost — aggregate resource cost per team."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_team_cost.command import ComputeTeamCostCommand
from hexawyn.application.use_case.finops.compute_team_cost.compute_team_cost_use_case import (
    ComputeTeamCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_team_cost(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_team_cost)
