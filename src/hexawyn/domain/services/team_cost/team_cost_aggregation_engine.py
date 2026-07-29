from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.team_cost import TeamCost, TeamCostReport


class TeamCostAggregationEngine:
    def compute(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_teams = _aggregate_team_costs(
            namespaces,
            month,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                month,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(t.total_cost for t in current_teams)
        unattributed = next(
            (t.total_cost for t in current_teams if t.team_name == "unattributed"), 0.0
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(unattributed, 2),
        )


def _aggregate_team_costs(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    month: str,
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map: dict[str, dict[str, float]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        storage_cost = round(storage * storage_price, 2)

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(data["cpu"], 2),
                memory_cost=round(data["mem"], 2),
                storage_cost=round(data["storage"], 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


@dataclass
class TeamAggregationData:
    cpu: float = 0.0
    mem: float = 0.0
    stor: float = 0.0
    namespaces: set[str] = field(default_factory=set)
    days: int = 0
    prorated: bool = False


def current_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def previous_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def compute_team_cost_entries(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    from collections import defaultdict

    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get("days_active"))
        if days_active <= 0:
            days_active = 30
        if days_active < 30:  # noqa: PLR2004
            t.prorated = True
        t.days = max(t.days, days_active)

    entries: list[TeamCost] = []
    for team_name, data in teams.items():
        cpu_cost = data.cpu * cpu_price * hours_per_month
        mem_cost = data.mem * memory_price * hours_per_month
        stor_cost = data.stor * storage_price
        entries.append(
            TeamCost(
                team_name=team_name,
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
