from dataclasses import dataclass, field


@dataclass
class TeamCostEntry:
    team_name: str = ""
    total_cost: float = 0.0
    cpu_cost: float = 0.0
    memory_cost: float = 0.0
    storage_cost: float = 0.0
    pod_count: int = 0
    namespace_count: int = 0


@dataclass
class TeamCostSummary:
    team_name: str = ""
    total_cost: float = 0.0


@dataclass
class TeamCostResult:
    month: str = ""
    total_cost: float = 0.0
    previous_total_cost: float = 0.0
    cost_delta_pct: float = 0.0
    teams: list[TeamCostEntry] = field(default_factory=list)
    previous_top_teams: list[TeamCostSummary] = field(default_factory=list)


@dataclass
class ComputeTeamCostResponse:
    result: TeamCostResult
    error: str | None = None
