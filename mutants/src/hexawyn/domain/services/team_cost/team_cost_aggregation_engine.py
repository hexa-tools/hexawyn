from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime

from hexawyn.domain.models.team_cost import TeamCost, TeamCostReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class TeamCostAggregationEngine:
    @_mutmut_mutated(mutants_xǁTeamCostAggregationEngineǁcompute__mutmut)
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
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_orig(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_1(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = None
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_2(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            None,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_3(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            None,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_4(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            None,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_5(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            None,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_6(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            None,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_7(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_8(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_9(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_10(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_11(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_12(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = None
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_13(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            None,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_14(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            None,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_15(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            None,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_16(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            None,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_17(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            None,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_18(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_19(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_20(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_21(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_22(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_23(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=None, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_24(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=None)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_25(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_26(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, )

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_27(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: None, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_28(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=False)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_29(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = None
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                previous_namespaces,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_30(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = None
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_31(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                None,
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_32(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                None,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_33(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                None,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_34(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                None,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_35(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                None,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_36(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams.sort(key=lambda t: t.total_cost, reverse=True)

        prev_teams: list[TeamCost] = []
        if previous_namespaces:
            prev_teams = _aggregate_team_costs(
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_37(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_38(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_39(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_40(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_41(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=None, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_42(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=None)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_43(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_44(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, )

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_45(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: None, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_46(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=False)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_47(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = None
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_48(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(None)
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_49(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] - data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_50(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] - data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_51(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["XXcpuXX"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_52(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["CPU"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_53(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["XXmemXX"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_54(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["MEM"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_55(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["XXstorageXX"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_56(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["STORAGE"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_57(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = None

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_58(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            None,
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_59(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            None,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_60(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_61(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_62(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] - data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_63(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] - data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_64(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["XXcpuXX"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_65(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["CPU"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_66(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["XXmemXX"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_67(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["MEM"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_68(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["XXstorageXX"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_69(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["STORAGE"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_70(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team != "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_71(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "XXunattributedXX"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_72(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "UNATTRIBUTED"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_73(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            1.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_74(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=None,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_75(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=None,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_76(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=None,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_77(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=None,
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_78(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=None,
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_79(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_80(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_81(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_82(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_83(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_84(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(None, 2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_85(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, None),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_86(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(2),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_87(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, ),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_88(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 3),
            unattributed_cost=round(float(unattributed), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_89(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(None, 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_90(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), None),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_91(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_92(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), ),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_93(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(None), 2),
        )
    def xǁTeamCostAggregationEngineǁcompute__mutmut_94(  # noqa: PLR0913
        self,
        namespaces: list[dict[str, object]],
        month: str,
        days_in_month: int,
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
        storage_price_per_gb_month: float,
        previous_namespaces: list[dict[str, object]] | None = None,
    ) -> TeamCostReport:
        current_totals = _team_totals(
            namespaces,
            days_in_month,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
            storage_price_per_gb_month,
        )
        current_teams = _aggregate_team_costs(
            namespaces,
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
                days_in_month,
                cpu_price_per_core_hour,
                memory_price_per_gb_hour,
                storage_price_per_gb_month,
            )
            prev_teams.sort(key=lambda t: t.total_cost, reverse=True)

        total = sum(data["cpu"] + data["mem"] + data["storage"] for data in current_totals.values())
        unattributed = next(
            (
                data["cpu"] + data["mem"] + data["storage"]
                for team, data in current_totals.items()
                if team == "unattributed"
            ),
            0.0,
        )

        return TeamCostReport(
            month=month,
            teams=current_teams,
            previous_month_teams=prev_teams,
            total_cost=round(total, 2),
            unattributed_cost=round(float(unattributed), 3),
        )

mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['_mutmut_orig'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_1'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_2'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_3'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_4'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_5'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_6'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_7'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_8'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_9'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_10'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_11'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_12'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_13'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_14'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_15'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_16'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_17'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_18'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_19'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_20'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_21'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_22'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_23'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_24'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_25'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_26'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_27'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_28'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_29'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_30'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_31'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_32'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_33'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_34'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_35'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_36'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_37'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_38'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_39'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_40'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_41'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_42'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_43'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_44'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_45'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_46'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_47'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_48'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_49'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_50'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_51'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_52'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_53'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_54'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_55'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_56'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_57'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_58'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_59'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_60'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_61'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_62'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_63'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_64'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_65'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_66'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_67'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_68'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_69'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_70'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_71'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_72'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_73'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_74'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_75'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_76'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_77'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_78'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_79'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_80'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_81'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_82'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_83'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_84'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_85'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_86'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_87'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_88'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_89'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_90'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_91'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_92'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_93'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁTeamCostAggregationEngineǁcompute__mutmut['xǁTeamCostAggregationEngineǁcompute__mutmut_94'] = TeamCostAggregationEngine.xǁTeamCostAggregationEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__team_totals__mutmut)
def _team_totals(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_orig(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_1(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = None

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_2(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = None
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_3(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(None)
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_4(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get(None, ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_5(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", None))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_6(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get(""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_7(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_8(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("XXteam_labelXX", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_9(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("TEAM_LABEL", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_10(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", "XXXX"))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_11(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_12(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = None

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_13(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "XXunattributedXX"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_14(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "UNATTRIBUTED"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_15(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = None
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_16(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(None)
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_17(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get(None))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_18(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("XXcpu_coresXX"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_19(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("CPU_CORES"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_20(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = None
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_21(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(None)
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_22(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get(None))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_23(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("XXmemory_gbXX"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_24(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("MEMORY_GB"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_25(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = None
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_26(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(None)
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_27(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get(None))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_28(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("XXstorage_gbXX"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_29(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("STORAGE_GB"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_30(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = None
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_31(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(None)
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_32(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get(None))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_33(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("XXdays_activeXX"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_34(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("DAYS_ACTIVE"))
        if days_active <= 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_35(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active < 0:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_36(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 1:
            days_active = days_in_month

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_37(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

    for ns in namespaces:
        team = str(ns.get("team_label", ""))
        if not team:
            team = "unattributed"

        cpu = _as_float(ns.get("cpu_cores"))
        mem = _as_float(ns.get("memory_gb"))
        storage = _as_float(ns.get("storage_gb"))
        days_active = _as_int(ns.get("days_active"))
        if days_active <= 0:
            days_active = None

        hours = days_active * 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_38(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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

        hours = None
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_39(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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

        hours = days_active / 24
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_40(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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

        hours = days_active * 25
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_41(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = None
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_42(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price / hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_43(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu / cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_44(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = None
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_45(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price / hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_46(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem / mem_price * hours
        storage_cost = storage * storage_price

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

    return team_map


def x__team_totals__mutmut_47(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = None

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

    return team_map


def x__team_totals__mutmut_48(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage / storage_price

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

    return team_map


def x__team_totals__mutmut_49(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team in team_map:
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

    return team_map


def x__team_totals__mutmut_50(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = None

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_51(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "XXcpuXX": 0.0,
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

    return team_map


def x__team_totals__mutmut_52(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "CPU": 0.0,
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

    return team_map


def x__team_totals__mutmut_53(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 1.0,
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

    return team_map


def x__team_totals__mutmut_54(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "XXmemXX": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_55(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "MEM": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_56(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 1.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_57(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "XXstorageXX": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_58(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "STORAGE": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_59(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 1.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_60(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "XXns_countXX": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_61(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "NS_COUNT": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_62(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 1,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_63(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "XXmin_daysXX": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_64(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "MIN_DAYS": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_65(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] = cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_66(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] -= cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_67(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["XXcpuXX"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_68(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["CPU"] += cpu_cost
        team_map[team]["mem"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_69(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] = mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_70(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["mem"] -= mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_71(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["XXmemXX"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_72(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

        if team not in team_map:
            team_map[team] = {
                "cpu": 0.0,
                "mem": 0.0,
                "storage": 0.0,
                "ns_count": 0,
                "min_days": days_active,
            }

        team_map[team]["cpu"] += cpu_cost
        team_map[team]["MEM"] += mem_cost
        team_map[team]["storage"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_73(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["storage"] = storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_74(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["storage"] -= storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_75(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["XXstorageXX"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_76(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["STORAGE"] += storage_cost
        team_map[team]["ns_count"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_77(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["ns_count"] = 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_78(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["ns_count"] -= 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_79(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["XXns_countXX"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_80(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["NS_COUNT"] += 1
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_81(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["ns_count"] += 2
        team_map[team]["min_days"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_82(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = None

    return team_map


def x__team_totals__mutmut_83(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["XXmin_daysXX"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_84(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["MIN_DAYS"] = min(team_map[team]["min_days"], days_active)

    return team_map


def x__team_totals__mutmut_85(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(None, days_active)

    return team_map


def x__team_totals__mutmut_86(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(team_map[team]["min_days"], None)

    return team_map


def x__team_totals__mutmut_87(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(days_active)

    return team_map


def x__team_totals__mutmut_88(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(team_map[team]["min_days"], )

    return team_map


def x__team_totals__mutmut_89(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(team_map[team]["XXmin_daysXX"], days_active)

    return team_map


def x__team_totals__mutmut_90(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> dict[str, dict[str, float | int]]:
    """Aggregate raw costs per team without rounding (single source of truth)."""
    team_map: dict[str, dict[str, float | int]] = {}

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
        cpu_cost = cpu * cpu_price * hours
        mem_cost = mem * mem_price * hours
        storage_cost = storage * storage_price

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
        team_map[team]["min_days"] = min(team_map[team]["MIN_DAYS"], days_active)

    return team_map

mutants_x__team_totals__mutmut['_mutmut_orig'] = x__team_totals__mutmut_orig # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_1'] = x__team_totals__mutmut_1 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_2'] = x__team_totals__mutmut_2 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_3'] = x__team_totals__mutmut_3 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_4'] = x__team_totals__mutmut_4 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_5'] = x__team_totals__mutmut_5 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_6'] = x__team_totals__mutmut_6 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_7'] = x__team_totals__mutmut_7 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_8'] = x__team_totals__mutmut_8 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_9'] = x__team_totals__mutmut_9 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_10'] = x__team_totals__mutmut_10 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_11'] = x__team_totals__mutmut_11 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_12'] = x__team_totals__mutmut_12 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_13'] = x__team_totals__mutmut_13 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_14'] = x__team_totals__mutmut_14 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_15'] = x__team_totals__mutmut_15 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_16'] = x__team_totals__mutmut_16 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_17'] = x__team_totals__mutmut_17 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_18'] = x__team_totals__mutmut_18 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_19'] = x__team_totals__mutmut_19 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_20'] = x__team_totals__mutmut_20 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_21'] = x__team_totals__mutmut_21 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_22'] = x__team_totals__mutmut_22 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_23'] = x__team_totals__mutmut_23 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_24'] = x__team_totals__mutmut_24 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_25'] = x__team_totals__mutmut_25 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_26'] = x__team_totals__mutmut_26 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_27'] = x__team_totals__mutmut_27 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_28'] = x__team_totals__mutmut_28 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_29'] = x__team_totals__mutmut_29 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_30'] = x__team_totals__mutmut_30 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_31'] = x__team_totals__mutmut_31 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_32'] = x__team_totals__mutmut_32 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_33'] = x__team_totals__mutmut_33 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_34'] = x__team_totals__mutmut_34 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_35'] = x__team_totals__mutmut_35 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_36'] = x__team_totals__mutmut_36 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_37'] = x__team_totals__mutmut_37 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_38'] = x__team_totals__mutmut_38 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_39'] = x__team_totals__mutmut_39 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_40'] = x__team_totals__mutmut_40 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_41'] = x__team_totals__mutmut_41 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_42'] = x__team_totals__mutmut_42 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_43'] = x__team_totals__mutmut_43 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_44'] = x__team_totals__mutmut_44 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_45'] = x__team_totals__mutmut_45 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_46'] = x__team_totals__mutmut_46 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_47'] = x__team_totals__mutmut_47 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_48'] = x__team_totals__mutmut_48 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_49'] = x__team_totals__mutmut_49 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_50'] = x__team_totals__mutmut_50 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_51'] = x__team_totals__mutmut_51 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_52'] = x__team_totals__mutmut_52 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_53'] = x__team_totals__mutmut_53 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_54'] = x__team_totals__mutmut_54 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_55'] = x__team_totals__mutmut_55 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_56'] = x__team_totals__mutmut_56 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_57'] = x__team_totals__mutmut_57 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_58'] = x__team_totals__mutmut_58 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_59'] = x__team_totals__mutmut_59 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_60'] = x__team_totals__mutmut_60 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_61'] = x__team_totals__mutmut_61 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_62'] = x__team_totals__mutmut_62 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_63'] = x__team_totals__mutmut_63 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_64'] = x__team_totals__mutmut_64 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_65'] = x__team_totals__mutmut_65 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_66'] = x__team_totals__mutmut_66 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_67'] = x__team_totals__mutmut_67 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_68'] = x__team_totals__mutmut_68 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_69'] = x__team_totals__mutmut_69 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_70'] = x__team_totals__mutmut_70 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_71'] = x__team_totals__mutmut_71 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_72'] = x__team_totals__mutmut_72 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_73'] = x__team_totals__mutmut_73 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_74'] = x__team_totals__mutmut_74 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_75'] = x__team_totals__mutmut_75 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_76'] = x__team_totals__mutmut_76 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_77'] = x__team_totals__mutmut_77 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_78'] = x__team_totals__mutmut_78 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_79'] = x__team_totals__mutmut_79 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_80'] = x__team_totals__mutmut_80 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_81'] = x__team_totals__mutmut_81 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_82'] = x__team_totals__mutmut_82 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_83'] = x__team_totals__mutmut_83 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_84'] = x__team_totals__mutmut_84 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_85'] = x__team_totals__mutmut_85 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_86'] = x__team_totals__mutmut_86 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_87'] = x__team_totals__mutmut_87 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_88'] = x__team_totals__mutmut_88 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_89'] = x__team_totals__mutmut_89 # type: ignore # mutmut generated
mutants_x__team_totals__mutmut['x__team_totals__mutmut_90'] = x__team_totals__mutmut_90 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aggregate_team_costs__mutmut)
def _aggregate_team_costs(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_orig(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_1(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = None
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_2(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(None, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_3(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, None, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_4(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, None, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_5(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, None, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_6(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, None)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_7(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_8(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_9(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_10(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_11(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, )
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_12(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = None
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_13(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = None
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_14(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] - data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_15(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] - data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_16(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["XXcpuXX"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_17(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["CPU"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_18(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["XXmemXX"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_19(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["MEM"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_20(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["XXstorageXX"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_21(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["STORAGE"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_22(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            None
        )

    return result


def x__aggregate_team_costs__mutmut_23(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=None,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_24(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=None,
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_25(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=None,
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_26(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=None,
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_27(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=None,
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_28(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=None,
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_29(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=None,
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_30(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=None,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_31(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_32(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_33(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_34(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_35(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_36(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_37(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_38(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                )
        )

    return result


def x__aggregate_team_costs__mutmut_39(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(None, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_40(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, None),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_41(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_42(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, ),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_43(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 3),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_44(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(None, 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_45(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), None),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_46(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_47(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), ),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_48(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(None), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_49(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["XXcpuXX"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_50(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["CPU"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_51(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 3),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_52(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(None, 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_53(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), None),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_54(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_55(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), ),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_56(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(None), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_57(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["XXmemXX"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_58(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["MEM"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_59(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 3),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_60(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(None, 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_61(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), None),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_62(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_63(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), ),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_64(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(None), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_65(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["XXstorageXX"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_66(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["STORAGE"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_67(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 3),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_68(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(None),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_69(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["XXns_countXX"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_70(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["NS_COUNT"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_71(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(None),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_72(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["XXmin_daysXX"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_73(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["MIN_DAYS"]),
                is_prorated=int(data["min_days"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_74(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(None) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_75(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["XXmin_daysXX"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_76(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["MIN_DAYS"]) < days_in_month,
            )
        )

    return result


def x__aggregate_team_costs__mutmut_77(  # noqa: PLR0913
    namespaces: list[dict[str, object]],
    days_in_month: int,
    cpu_price: float,
    mem_price: float,
    storage_price: float,
) -> list[TeamCost]:
    team_map = _team_totals(namespaces, days_in_month, cpu_price, mem_price, storage_price)
    result: list[TeamCost] = []
    for team_name, data in team_map.items():
        total = data["cpu"] + data["mem"] + data["storage"]
        result.append(
            TeamCost(
                team_name=team_name,
                total_cost=round(total, 2),
                cpu_cost=round(float(data["cpu"]), 2),
                memory_cost=round(float(data["mem"]), 2),
                storage_cost=round(float(data["storage"]), 2),
                namespace_count=int(data["ns_count"]),
                days_active=int(data["min_days"]),
                is_prorated=int(data["min_days"]) <= days_in_month,
            )
        )

    return result

mutants_x__aggregate_team_costs__mutmut['_mutmut_orig'] = x__aggregate_team_costs__mutmut_orig # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_1'] = x__aggregate_team_costs__mutmut_1 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_2'] = x__aggregate_team_costs__mutmut_2 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_3'] = x__aggregate_team_costs__mutmut_3 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_4'] = x__aggregate_team_costs__mutmut_4 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_5'] = x__aggregate_team_costs__mutmut_5 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_6'] = x__aggregate_team_costs__mutmut_6 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_7'] = x__aggregate_team_costs__mutmut_7 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_8'] = x__aggregate_team_costs__mutmut_8 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_9'] = x__aggregate_team_costs__mutmut_9 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_10'] = x__aggregate_team_costs__mutmut_10 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_11'] = x__aggregate_team_costs__mutmut_11 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_12'] = x__aggregate_team_costs__mutmut_12 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_13'] = x__aggregate_team_costs__mutmut_13 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_14'] = x__aggregate_team_costs__mutmut_14 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_15'] = x__aggregate_team_costs__mutmut_15 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_16'] = x__aggregate_team_costs__mutmut_16 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_17'] = x__aggregate_team_costs__mutmut_17 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_18'] = x__aggregate_team_costs__mutmut_18 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_19'] = x__aggregate_team_costs__mutmut_19 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_20'] = x__aggregate_team_costs__mutmut_20 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_21'] = x__aggregate_team_costs__mutmut_21 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_22'] = x__aggregate_team_costs__mutmut_22 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_23'] = x__aggregate_team_costs__mutmut_23 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_24'] = x__aggregate_team_costs__mutmut_24 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_25'] = x__aggregate_team_costs__mutmut_25 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_26'] = x__aggregate_team_costs__mutmut_26 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_27'] = x__aggregate_team_costs__mutmut_27 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_28'] = x__aggregate_team_costs__mutmut_28 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_29'] = x__aggregate_team_costs__mutmut_29 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_30'] = x__aggregate_team_costs__mutmut_30 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_31'] = x__aggregate_team_costs__mutmut_31 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_32'] = x__aggregate_team_costs__mutmut_32 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_33'] = x__aggregate_team_costs__mutmut_33 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_34'] = x__aggregate_team_costs__mutmut_34 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_35'] = x__aggregate_team_costs__mutmut_35 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_36'] = x__aggregate_team_costs__mutmut_36 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_37'] = x__aggregate_team_costs__mutmut_37 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_38'] = x__aggregate_team_costs__mutmut_38 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_39'] = x__aggregate_team_costs__mutmut_39 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_40'] = x__aggregate_team_costs__mutmut_40 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_41'] = x__aggregate_team_costs__mutmut_41 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_42'] = x__aggregate_team_costs__mutmut_42 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_43'] = x__aggregate_team_costs__mutmut_43 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_44'] = x__aggregate_team_costs__mutmut_44 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_45'] = x__aggregate_team_costs__mutmut_45 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_46'] = x__aggregate_team_costs__mutmut_46 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_47'] = x__aggregate_team_costs__mutmut_47 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_48'] = x__aggregate_team_costs__mutmut_48 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_49'] = x__aggregate_team_costs__mutmut_49 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_50'] = x__aggregate_team_costs__mutmut_50 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_51'] = x__aggregate_team_costs__mutmut_51 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_52'] = x__aggregate_team_costs__mutmut_52 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_53'] = x__aggregate_team_costs__mutmut_53 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_54'] = x__aggregate_team_costs__mutmut_54 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_55'] = x__aggregate_team_costs__mutmut_55 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_56'] = x__aggregate_team_costs__mutmut_56 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_57'] = x__aggregate_team_costs__mutmut_57 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_58'] = x__aggregate_team_costs__mutmut_58 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_59'] = x__aggregate_team_costs__mutmut_59 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_60'] = x__aggregate_team_costs__mutmut_60 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_61'] = x__aggregate_team_costs__mutmut_61 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_62'] = x__aggregate_team_costs__mutmut_62 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_63'] = x__aggregate_team_costs__mutmut_63 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_64'] = x__aggregate_team_costs__mutmut_64 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_65'] = x__aggregate_team_costs__mutmut_65 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_66'] = x__aggregate_team_costs__mutmut_66 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_67'] = x__aggregate_team_costs__mutmut_67 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_68'] = x__aggregate_team_costs__mutmut_68 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_69'] = x__aggregate_team_costs__mutmut_69 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_70'] = x__aggregate_team_costs__mutmut_70 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_71'] = x__aggregate_team_costs__mutmut_71 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_72'] = x__aggregate_team_costs__mutmut_72 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_73'] = x__aggregate_team_costs__mutmut_73 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_74'] = x__aggregate_team_costs__mutmut_74 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_75'] = x__aggregate_team_costs__mutmut_75 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_76'] = x__aggregate_team_costs__mutmut_76 # type: ignore # mutmut generated
mutants_x__aggregate_team_costs__mutmut['x__aggregate_team_costs__mutmut_77'] = x__aggregate_team_costs__mutmut_77 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_orig(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_1(value: object) -> float:
    if value is not None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_2(value: object) -> float:
    if value is None:
        return 1.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_3(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_4(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1.0

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_2'] = x__as_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_3'] = x__as_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_4'] = x__as_float__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_1(value: object) -> int:
    if value is not None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_2(value: object) -> int:
    if value is None:
        return 1
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_3(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_4(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_5(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated


@dataclass
class TeamAggregationData:
    cpu: float = 0.0
    mem: float = 0.0
    stor: float = 0.0
    namespaces: set[str] = field(default_factory=set)
    days: int = 0
    prorated: bool = False
mutants_x_current_month_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_current_month_str__mutmut)
def current_month_str() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_current_month_str__mutmut_orig() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_current_month_str__mutmut_1() -> str:
    now = None
    return f"{now.year}-{now.month:02d}"

mutants_x_current_month_str__mutmut['_mutmut_orig'] = x_current_month_str__mutmut_orig # type: ignore # mutmut generated
mutants_x_current_month_str__mutmut['x_current_month_str__mutmut_1'] = x_current_month_str__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_previous_month_str__mutmut)
def previous_month_str() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_orig() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_1() -> str:
    now = None
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_2() -> str:
    now = datetime.now()
    if now.month != 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_3() -> str:
    now = datetime.now()
    if now.month == 2:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_4() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year + 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_5() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 2}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_6() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month + 1:02d}"


def x_previous_month_str__mutmut_7() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 2:02d}"

mutants_x_previous_month_str__mutmut['_mutmut_orig'] = x_previous_month_str__mutmut_orig # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_1'] = x_previous_month_str__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_2'] = x_previous_month_str__mutmut_2 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_3'] = x_previous_month_str__mutmut_3 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_4'] = x_previous_month_str__mutmut_4 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_5'] = x_previous_month_str__mutmut_5 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_6'] = x_previous_month_str__mutmut_6 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_7'] = x_previous_month_str__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_team_cost_entries__mutmut)
def compute_team_cost_entries(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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


def x_compute_team_cost_entries__mutmut_orig(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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


def x_compute_team_cost_entries__mutmut_1(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = None
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


def x_compute_team_cost_entries__mutmut_2(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(None)
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


def x_compute_team_cost_entries__mutmut_3(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = None
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


def x_compute_team_cost_entries__mutmut_4(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) and "unattributed"
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


def x_compute_team_cost_entries__mutmut_5(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(None) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_6(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get(None, "")) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_7(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", None)) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_8(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("")) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_9(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", )) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_10(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("XXteam_labelXX", "")) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_11(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("TEAM_LABEL", "")) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_12(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "XXXX")) or "unattributed"
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


def x_compute_team_cost_entries__mutmut_13(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "XXunattributedXX"
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


def x_compute_team_cost_entries__mutmut_14(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "UNATTRIBUTED"
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


def x_compute_team_cost_entries__mutmut_15(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = None
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


def x_compute_team_cost_entries__mutmut_16(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu = _as_float(r.get("cpu_cores"))
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


def x_compute_team_cost_entries__mutmut_17(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu -= _as_float(r.get("cpu_cores"))
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


def x_compute_team_cost_entries__mutmut_18(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(None)
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


def x_compute_team_cost_entries__mutmut_19(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get(None))
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


def x_compute_team_cost_entries__mutmut_20(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("XXcpu_coresXX"))
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


def x_compute_team_cost_entries__mutmut_21(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("CPU_CORES"))
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


def x_compute_team_cost_entries__mutmut_22(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem = _as_float(r.get("memory_gb"))
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


def x_compute_team_cost_entries__mutmut_23(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem -= _as_float(r.get("memory_gb"))
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


def x_compute_team_cost_entries__mutmut_24(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(None)
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


def x_compute_team_cost_entries__mutmut_25(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get(None))
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


def x_compute_team_cost_entries__mutmut_26(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("XXmemory_gbXX"))
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


def x_compute_team_cost_entries__mutmut_27(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("MEMORY_GB"))
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


def x_compute_team_cost_entries__mutmut_28(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor = _as_float(r.get("storage_gb"))
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


def x_compute_team_cost_entries__mutmut_29(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor -= _as_float(r.get("storage_gb"))
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


def x_compute_team_cost_entries__mutmut_30(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(None)
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


def x_compute_team_cost_entries__mutmut_31(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get(None))
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


def x_compute_team_cost_entries__mutmut_32(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("XXstorage_gbXX"))
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


def x_compute_team_cost_entries__mutmut_33(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("STORAGE_GB"))
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


def x_compute_team_cost_entries__mutmut_34(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(None)
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


def x_compute_team_cost_entries__mutmut_35(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(None))
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


def x_compute_team_cost_entries__mutmut_36(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get(None, "")))
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


def x_compute_team_cost_entries__mutmut_37(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", None)))
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


def x_compute_team_cost_entries__mutmut_38(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("")))
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


def x_compute_team_cost_entries__mutmut_39(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", )))
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


def x_compute_team_cost_entries__mutmut_40(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("XXnamespaceXX", "")))
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


def x_compute_team_cost_entries__mutmut_41(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("NAMESPACE", "")))
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


def x_compute_team_cost_entries__mutmut_42(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "XXXX")))
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


def x_compute_team_cost_entries__mutmut_43(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = None
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


def x_compute_team_cost_entries__mutmut_44(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(None)
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


def x_compute_team_cost_entries__mutmut_45(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get(None))
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


def x_compute_team_cost_entries__mutmut_46(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get("XXdays_activeXX"))
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


def x_compute_team_cost_entries__mutmut_47(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get("DAYS_ACTIVE"))
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


def x_compute_team_cost_entries__mutmut_48(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get("days_active"))
        if days_active < 0:
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


def x_compute_team_cost_entries__mutmut_49(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
    teams: dict[str, TeamAggregationData] = defaultdict(TeamAggregationData)
    for r in resources:
        team = str(r.get("team_label", "")) or "unattributed"
        t = teams[team]
        t.cpu += _as_float(r.get("cpu_cores"))
        t.mem += _as_float(r.get("memory_gb"))
        t.stor += _as_float(r.get("storage_gb"))
        t.namespaces.add(str(r.get("namespace", "")))
        days_active = _as_int(r.get("days_active"))
        if days_active <= 1:
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


def x_compute_team_cost_entries__mutmut_50(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
            days_active = None
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


def x_compute_team_cost_entries__mutmut_51(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
            days_active = 31
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


def x_compute_team_cost_entries__mutmut_52(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        if days_active <= 30:  # noqa: PLR2004
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


def x_compute_team_cost_entries__mutmut_53(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        if days_active < 31:  # noqa: PLR2004
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


def x_compute_team_cost_entries__mutmut_54(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
            t.prorated = None
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


def x_compute_team_cost_entries__mutmut_55(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
            t.prorated = False
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


def x_compute_team_cost_entries__mutmut_56(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        t.days = None

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


def x_compute_team_cost_entries__mutmut_57(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        t.days = max(None, days_active)

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


def x_compute_team_cost_entries__mutmut_58(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        t.days = max(t.days, None)

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


def x_compute_team_cost_entries__mutmut_59(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        t.days = max(days_active)

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


def x_compute_team_cost_entries__mutmut_60(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        t.days = max(t.days, )

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


def x_compute_team_cost_entries__mutmut_61(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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

    entries: list[TeamCost] = None
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


def x_compute_team_cost_entries__mutmut_62(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        cpu_cost = None
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


def x_compute_team_cost_entries__mutmut_63(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        cpu_cost = data.cpu * cpu_price / hours_per_month
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


def x_compute_team_cost_entries__mutmut_64(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        cpu_cost = data.cpu / cpu_price * hours_per_month
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


def x_compute_team_cost_entries__mutmut_65(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        mem_cost = None
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


def x_compute_team_cost_entries__mutmut_66(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        mem_cost = data.mem * memory_price / hours_per_month
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


def x_compute_team_cost_entries__mutmut_67(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        mem_cost = data.mem / memory_price * hours_per_month
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


def x_compute_team_cost_entries__mutmut_68(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        stor_cost = None
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


def x_compute_team_cost_entries__mutmut_69(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
        stor_cost = data.stor / storage_price
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


def x_compute_team_cost_entries__mutmut_70(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
            None
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_71(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                team_name=None,
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


def x_compute_team_cost_entries__mutmut_72(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=None,
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_73(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=None,
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_74(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=None,
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_75(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=None,
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_76(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                namespace_count=None,
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_77(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                days_active=None,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_78(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                is_prorated=None,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_79(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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


def x_compute_team_cost_entries__mutmut_80(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_81(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_82(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_83(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_84(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_85(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_86(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_87(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(None, 2),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_88(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(cpu_cost + mem_cost + stor_cost, None),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_89(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(2),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_90(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(cpu_cost + mem_cost + stor_cost, ),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_91(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(cpu_cost + mem_cost - stor_cost, 2),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_92(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(cpu_cost - mem_cost + stor_cost, 2),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_93(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                total_cost=round(cpu_cost + mem_cost + stor_cost, 3),
                cpu_cost=round(cpu_cost, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_94(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(None, 2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_95(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(cpu_cost, None),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_96(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(2),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_97(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(cpu_cost, ),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_98(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                cpu_cost=round(cpu_cost, 3),
                memory_cost=round(mem_cost, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_99(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(None, 2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_100(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(mem_cost, None),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_101(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(2),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_102(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(mem_cost, ),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_103(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                memory_cost=round(mem_cost, 3),
                storage_cost=round(stor_cost, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_104(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(None, 2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_105(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(stor_cost, None),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_106(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(2),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_107(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(stor_cost, ),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_108(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
                storage_cost=round(stor_cost, 3),
                namespace_count=len(data.namespaces),
                days_active=data.days,
                is_prorated=data.prorated,
            )
        )
    return sorted(entries, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_109(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(None, key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_110(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, key=None, reverse=True)


def x_compute_team_cost_entries__mutmut_111(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, key=lambda e: e.total_cost, reverse=None)


def x_compute_team_cost_entries__mutmut_112(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(key=lambda e: e.total_cost, reverse=True)


def x_compute_team_cost_entries__mutmut_113(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, reverse=True)


def x_compute_team_cost_entries__mutmut_114(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, key=lambda e: e.total_cost, )


def x_compute_team_cost_entries__mutmut_115(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, key=lambda e: None, reverse=True)


def x_compute_team_cost_entries__mutmut_116(
    resources: list[dict[str, object]],
    cpu_price: float,
    memory_price: float,
    storage_price: float,
    hours_per_month: int,
) -> list[TeamCost]:
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
    return sorted(entries, key=lambda e: e.total_cost, reverse=False)

mutants_x_compute_team_cost_entries__mutmut['_mutmut_orig'] = x_compute_team_cost_entries__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_1'] = x_compute_team_cost_entries__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_2'] = x_compute_team_cost_entries__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_3'] = x_compute_team_cost_entries__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_4'] = x_compute_team_cost_entries__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_5'] = x_compute_team_cost_entries__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_6'] = x_compute_team_cost_entries__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_7'] = x_compute_team_cost_entries__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_8'] = x_compute_team_cost_entries__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_9'] = x_compute_team_cost_entries__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_10'] = x_compute_team_cost_entries__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_11'] = x_compute_team_cost_entries__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_12'] = x_compute_team_cost_entries__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_13'] = x_compute_team_cost_entries__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_14'] = x_compute_team_cost_entries__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_15'] = x_compute_team_cost_entries__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_16'] = x_compute_team_cost_entries__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_17'] = x_compute_team_cost_entries__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_18'] = x_compute_team_cost_entries__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_19'] = x_compute_team_cost_entries__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_20'] = x_compute_team_cost_entries__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_21'] = x_compute_team_cost_entries__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_22'] = x_compute_team_cost_entries__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_23'] = x_compute_team_cost_entries__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_24'] = x_compute_team_cost_entries__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_25'] = x_compute_team_cost_entries__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_26'] = x_compute_team_cost_entries__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_27'] = x_compute_team_cost_entries__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_28'] = x_compute_team_cost_entries__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_29'] = x_compute_team_cost_entries__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_30'] = x_compute_team_cost_entries__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_31'] = x_compute_team_cost_entries__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_32'] = x_compute_team_cost_entries__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_33'] = x_compute_team_cost_entries__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_34'] = x_compute_team_cost_entries__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_35'] = x_compute_team_cost_entries__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_36'] = x_compute_team_cost_entries__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_37'] = x_compute_team_cost_entries__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_38'] = x_compute_team_cost_entries__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_39'] = x_compute_team_cost_entries__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_40'] = x_compute_team_cost_entries__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_41'] = x_compute_team_cost_entries__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_42'] = x_compute_team_cost_entries__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_43'] = x_compute_team_cost_entries__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_44'] = x_compute_team_cost_entries__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_45'] = x_compute_team_cost_entries__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_46'] = x_compute_team_cost_entries__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_47'] = x_compute_team_cost_entries__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_48'] = x_compute_team_cost_entries__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_49'] = x_compute_team_cost_entries__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_50'] = x_compute_team_cost_entries__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_51'] = x_compute_team_cost_entries__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_52'] = x_compute_team_cost_entries__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_53'] = x_compute_team_cost_entries__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_54'] = x_compute_team_cost_entries__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_55'] = x_compute_team_cost_entries__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_56'] = x_compute_team_cost_entries__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_57'] = x_compute_team_cost_entries__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_58'] = x_compute_team_cost_entries__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_59'] = x_compute_team_cost_entries__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_60'] = x_compute_team_cost_entries__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_61'] = x_compute_team_cost_entries__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_62'] = x_compute_team_cost_entries__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_63'] = x_compute_team_cost_entries__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_64'] = x_compute_team_cost_entries__mutmut_64 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_65'] = x_compute_team_cost_entries__mutmut_65 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_66'] = x_compute_team_cost_entries__mutmut_66 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_67'] = x_compute_team_cost_entries__mutmut_67 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_68'] = x_compute_team_cost_entries__mutmut_68 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_69'] = x_compute_team_cost_entries__mutmut_69 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_70'] = x_compute_team_cost_entries__mutmut_70 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_71'] = x_compute_team_cost_entries__mutmut_71 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_72'] = x_compute_team_cost_entries__mutmut_72 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_73'] = x_compute_team_cost_entries__mutmut_73 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_74'] = x_compute_team_cost_entries__mutmut_74 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_75'] = x_compute_team_cost_entries__mutmut_75 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_76'] = x_compute_team_cost_entries__mutmut_76 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_77'] = x_compute_team_cost_entries__mutmut_77 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_78'] = x_compute_team_cost_entries__mutmut_78 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_79'] = x_compute_team_cost_entries__mutmut_79 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_80'] = x_compute_team_cost_entries__mutmut_80 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_81'] = x_compute_team_cost_entries__mutmut_81 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_82'] = x_compute_team_cost_entries__mutmut_82 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_83'] = x_compute_team_cost_entries__mutmut_83 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_84'] = x_compute_team_cost_entries__mutmut_84 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_85'] = x_compute_team_cost_entries__mutmut_85 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_86'] = x_compute_team_cost_entries__mutmut_86 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_87'] = x_compute_team_cost_entries__mutmut_87 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_88'] = x_compute_team_cost_entries__mutmut_88 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_89'] = x_compute_team_cost_entries__mutmut_89 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_90'] = x_compute_team_cost_entries__mutmut_90 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_91'] = x_compute_team_cost_entries__mutmut_91 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_92'] = x_compute_team_cost_entries__mutmut_92 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_93'] = x_compute_team_cost_entries__mutmut_93 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_94'] = x_compute_team_cost_entries__mutmut_94 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_95'] = x_compute_team_cost_entries__mutmut_95 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_96'] = x_compute_team_cost_entries__mutmut_96 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_97'] = x_compute_team_cost_entries__mutmut_97 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_98'] = x_compute_team_cost_entries__mutmut_98 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_99'] = x_compute_team_cost_entries__mutmut_99 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_100'] = x_compute_team_cost_entries__mutmut_100 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_101'] = x_compute_team_cost_entries__mutmut_101 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_102'] = x_compute_team_cost_entries__mutmut_102 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_103'] = x_compute_team_cost_entries__mutmut_103 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_104'] = x_compute_team_cost_entries__mutmut_104 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_105'] = x_compute_team_cost_entries__mutmut_105 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_106'] = x_compute_team_cost_entries__mutmut_106 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_107'] = x_compute_team_cost_entries__mutmut_107 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_108'] = x_compute_team_cost_entries__mutmut_108 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_109'] = x_compute_team_cost_entries__mutmut_109 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_110'] = x_compute_team_cost_entries__mutmut_110 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_111'] = x_compute_team_cost_entries__mutmut_111 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_112'] = x_compute_team_cost_entries__mutmut_112 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_113'] = x_compute_team_cost_entries__mutmut_113 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_114'] = x_compute_team_cost_entries__mutmut_114 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_115'] = x_compute_team_cost_entries__mutmut_115 # type: ignore # mutmut generated
mutants_x_compute_team_cost_entries__mutmut['x_compute_team_cost_entries__mutmut_116'] = x_compute_team_cost_entries__mutmut_116 # type: ignore # mutmut generated
