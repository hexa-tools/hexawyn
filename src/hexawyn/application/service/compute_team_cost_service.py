from __future__ import annotations

from calendar import monthrange
from datetime import UTC, datetime

from hexawyn.application.ports.driven.team_cost_port import TeamCostPort
from hexawyn.application.use_case.compute_team_cost.command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.use_case.compute_team_cost.response import (
    ComputeTeamCostResponse,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_service_port import (
    ComputeTeamCostServicePort,
)
from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
    TeamCostAggregationEngine,
)


class ComputeTeamCostService(ComputeTeamCostServicePort):
    def __init__(self, cost_port: TeamCostPort) -> None:
        self._port = cost_port
        self._engine = TeamCostAggregationEngine()

    def compute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)


def _days_in_month(year: int, month: int) -> int:
    return monthrange(year, month)[1]


def _previous_month(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"
