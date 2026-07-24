from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime

from hexawyn.application.ports.driven.team_cost_port import NamespaceResourceData, TeamCostPort
from hexawyn.application.use_case.compute_team_cost.command import ComputeTeamCostCommand
from hexawyn.application.use_case.compute_team_cost.response import (
    ComputeTeamCostResponse,
    TeamCostEntry,
    TeamCostResult,
    TeamCostSummary,
)

HOURS_PER_MONTH = 730


@dataclass
class _TeamAggregation:
    cpu: float = 0.0
    mem: float = 0.0
    stor: float = 0.0
    namespaces: set[str] = field(default_factory=set)
    days: int = 0
    prorated: bool = False


def _current_month() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def _previous_month() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def _compute_team_entries(
    resources: list[NamespaceResourceData],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
) -> list[TeamCostEntry]:
    teams: dict[str, _TeamAggregation] = defaultdict(_TeamAggregation)
    for r in resources:
        team = r.get("team_label") or "unattributed"
        t = teams[team]
        t.cpu += r["cpu_cores"]
        t.mem += r["memory_gb"]
        t.stor += r["storage_gb"]
        t.namespaces.add(r["namespace"])
        if r.get("days_active", 30) < 30:
            t.prorated = True
        t.days = max(t.days, r.get("days_active", 30))

    entries: list[TeamCostEntry] = []
    for team, data in teams.items():
        cpu_cost = data.cpu * cpu_price * HOURS_PER_MONTH
        mem_cost = data.mem * memory_price * HOURS_PER_MONTH
        stor_cost = data.stor * storage_price
        entries.append(
            TeamCostEntry(
                team_name=team,
                total_cost=round(cpu_cost + mem_cost + stor_cost, 2),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


class ComputeTeamCostUseCase:
    def __init__(self, port: TeamCostPort) -> None:
        self._port = port

    def execute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        current_month = _current_month()
        prev_month = _previous_month()

        current = self._port.fetch_namespace_resources(current_month)
        previous = self._port.fetch_namespace_resources(prev_month)

        teams = _compute_team_entries(
            current,
            command.cpu_price_per_core_hour,
            command.memory_price_per_gb_hour,
            command.storage_price_per_gb_month,
        )
        prev_teams = _compute_team_entries(
            previous,
            command.cpu_price_per_core_hour,
            command.memory_price_per_gb_hour,
            command.storage_price_per_gb_month,
        )
        prev_summaries = [
            TeamCostSummary(team_name=t.team_name, total_cost=t.total_cost) for t in prev_teams[:5]
        ]

        unattributed = next((t.total_cost for t in teams if t.team_name == "unattributed"), 0.0)
        total = sum(t.total_cost for t in teams)

        result = TeamCostResult(
            month=current_month,
            total_cost=round(total, 2),
            unattributed_cost=round(unattributed, 2),
            teams=teams,
            previous_month_teams=prev_summaries,
        )
        return ComputeTeamCostResponse(result=result)
