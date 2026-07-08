from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class TeamCost:
    team_name: str
    total_cost: float
    cpu_cost: float
    memory_cost: float
    storage_cost: float
    namespace_count: int
    days_active: int
    is_prorated: bool


@dataclass
class TeamCostReport:
    month: str = ""
    teams: list[TeamCost] = field(default_factory=list)
    previous_month_teams: list[TeamCost] = field(default_factory=list)
    total_cost: float = 0.0
    unattributed_cost: float = 0.0
