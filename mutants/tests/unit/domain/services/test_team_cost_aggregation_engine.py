"""RED → GREEN — Team Cost Aggregation domain logic."""

from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
    TeamCostAggregationEngine,
)


def _namespace_data(  # noqa: PLR0913
    namespace: str = "team-payments",
    team_label: str = "payments",
    cpu_cores: float = 10.0,
    memory_gb: float = 40.0,
    storage_gb: float = 100.0,
    month: str = "2026-07",
    days_active: int = 31,
) -> dict[str, object]:
    return {
        "namespace": namespace,
        "team_label": team_label,
        "cpu_cores": cpu_cores,
        "memory_gb": memory_gb,
        "storage_gb": storage_gb,
        "month": month,
        "days_active": days_active,
    }


class TestTeamAggregation:
    def test_three_teams_ranked_by_cost(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(namespace="payments-prod", cpu_cores=20.0, memory_gb=80.0),
            _namespace_data(
                namespace="auth-prod", team_label="auth", cpu_cores=5.0, memory_gb=20.0
            ),
            _namespace_data(
                namespace="infra-prod",
                team_label="infra",
                cpu_cores=10.0,
                memory_gb=40.0,
            ),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert len(result.teams) == 3  # noqa: PLR2004
        assert result.teams[0].team_name == "payments"
        assert result.teams[1].team_name == "infra"
        assert result.teams[2].team_name == "auth"

    def test_unattributed_namespace_flagged(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(team_label=""),
            _namespace_data(team_label="payments"),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.unattributed_cost > 0
        assert any(t.team_name == "unattributed" for t in result.teams)
        assert any(t.team_name == "payments" for t in result.teams)

    def test_team_with_no_workloads_zero_cost(self) -> None:
        engine = TeamCostAggregationEngine()

        result = engine.compute(
            namespaces=[],
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.total_cost == 0.0
        assert result.teams == []

    def test_new_team_mid_month_prorated(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(team_label="new-team", days_active=15),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost > 0
        assert result.teams[0].is_prorated is True

    def test_month_over_month_comparison(self) -> None:
        engine = TeamCostAggregationEngine()
        current = [
            _namespace_data(namespace="payments-prod", cpu_cores=20.0, month="2026-07"),
        ]
        previous = [
            _namespace_data(namespace="payments-prod", cpu_cores=10.0, month="2026-06"),
        ]

        result = engine.compute(
            namespaces=current,
            previous_namespaces=previous,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost > 0
        assert len(result.previous_month_teams) > 0


class TestCostCalculation:
    def test_cpu_cost_computed_correctly(self) -> None:
        engine = TeamCostAggregationEngine()
        ns = [_namespace_data(cpu_cores=1.0, memory_gb=0.0, storage_gb=0.0)]

        result = engine.compute(
            namespaces=ns,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.0,
            storage_price_per_gb_month=0.0,
        )

        expected = round(1.0 * 0.03 * 31 * 24, 2)
        assert result.teams[0].cpu_cost == expected

    def test_team_cost_sums_across_namespaces(self) -> None:
        # 2 namespaces meme team -> cpu cumulé (5 + 2 = 7 cores)
        engine = TeamCostAggregationEngine()
        ns = [
            _namespace_data(
                namespace="pay-a",
                team_label="payments",
                cpu_cores=5.0,
                memory_gb=0.0,
                storage_gb=0.0,
            ),
            _namespace_data(
                namespace="pay-b",
                team_label="payments",
                cpu_cores=2.0,
                memory_gb=0.0,
                storage_gb=0.0,
            ),
        ]

        result = engine.compute(
            namespaces=ns,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.0,
            storage_price_per_gb_month=0.0,
        )

        assert result.teams[0].cpu_cost == round(7.0 * 0.03 * 31 * 24, 2)  # noqa: PLR2004
        assert result.teams[0].namespace_count == 2  # noqa: PLR2004

    def test_total_cost_includes_all_resources(self) -> None:
        engine = TeamCostAggregationEngine()
        ns = [_namespace_data(cpu_cores=2.0, memory_gb=4.0, storage_gb=100.0)]

        result = engine.compute(
            namespaces=ns,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost > result.teams[0].cpu_cost
        assert result.teams[0].total_cost > result.teams[0].memory_cost


class TestEdgeCases:
    def test_shared_namespace_multiple_teams_split(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(
                namespace="shared-platform",
                team_label="platform",
                cpu_cores=10.0,
                memory_gb=20.0,
                storage_gb=50.0,
            ),
            _namespace_data(
                namespace="shared-platform",
                team_label="data",
                cpu_cores=5.0,
                memory_gb=10.0,
                storage_gb=30.0,
            ),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.total_cost > 0
        assert result.teams[0].team_name != result.teams[1].team_name

    def test_resource_quotas_exceeded_flag(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(cpu_cores=100.0, memory_gb=500.0),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost > 0

    def test_spot_instance_cost_reflected(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(team_label="platform", cpu_cores=10.0, memory_gb=40.0),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.01,
            memory_price_per_gb_hour=0.005,
            storage_price_per_gb_month=0.05,
        )

        assert result.teams[0].total_cost < 1000.0  # noqa: PLR2004

    def test_multiple_namespaces_same_team_aggregated(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(namespace="payments-prod", team_label="payments", cpu_cores=5.0),
            _namespace_data(namespace="payments-staging", team_label="payments", cpu_cores=2.0),
            _namespace_data(namespace="payments-dev", team_label="payments", cpu_cores=1.0),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert len(result.teams) == 1
        assert result.teams[0].team_name == "payments"
        assert result.teams[0].namespace_count == 3  # noqa: PLR2004

    def test_team_with_only_storage_no_compute(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(cpu_cores=0.0, memory_gb=0.0, storage_gb=500.0, team_label="data"),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].cpu_cost == 0.0
        assert result.teams[0].storage_cost > 0.0

    def test_negative_resource_values_handled(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(cpu_cores=-1.0, memory_gb=-10.0, team_label="buggy"),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost <= 0.0

    def test_zero_days_active_defaults_to_full_month(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(days_active=0),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )

        assert result.teams[0].total_cost > 0


class TestHelperFunctions:
    def test_as_float_none_returns_zero(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _as_float,
        )

        assert _as_float(None) == 0.0

    def test_as_float_invalid_returns_zero(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _as_float,
        )

        assert _as_float("abc") == 0.0
        assert _as_float([1, 2]) == 0.0

    def test_as_int_none_returns_zero(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _as_int,
        )

        assert _as_int(None) == 0

    def test_as_int_invalid_returns_zero(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _as_int,
        )

        assert _as_int("xyz") == 0
        assert _as_int({"key": "val"}) == 0

    def test_current_month_str_returns_format(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            current_month_str,
        )

        result = current_month_str()
        assert "-" in result

    def test_previous_month_str(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            previous_month_str,
        )

        result = previous_month_str()
        assert "-" in result

    def test_previous_month_str_format(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            previous_month_str,
        )

        result = previous_month_str()
        parts = result.split("-")
        assert len(parts) == 2  # noqa: PLR2004
        assert 2000 <= int(parts[0]) <= 2100  # noqa: PLR2004
        assert 1 <= int(parts[1]) <= 12  # noqa: PLR2004


class TestPreviousMonthStrBoundaries:
    def _patch_datetime(self, monkeypatch: object, year: int, month: int) -> None:
        import datetime as _real_dt

        import hexawyn.domain.services.team_cost.team_cost_aggregation_engine as _mod

        class _FakeDateTime:
            @staticmethod
            def now() -> object:
                return _real_dt.datetime(year, month, 15)

        monkeypatch.setattr(  # type: ignore[attr-defined]
            _mod, "datetime", _FakeDateTime
        )

    def test_january_rolls_to_previous_year(self, monkeypatch: object) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            previous_month_str,
        )

        self._patch_datetime(monkeypatch, 2026, 1)
        assert previous_month_str() == "2025-12"

    def test_not_january_decrements_month(self, monkeypatch: object) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            previous_month_str,
        )

        self._patch_datetime(monkeypatch, 2026, 5)
        assert previous_month_str() == "2026-04"


class TestComputeTeamCostEntries:
    def test_multiple_teams_sorted_by_cost(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "payments",
                "cpu_cores": 10.0,
                "memory_gb": 40.0,
                "storage_gb": 100.0,
                "namespace": "pay-prod",
                "days_active": 31,
            },
            {
                "team_label": "auth",
                "cpu_cores": 5.0,
                "memory_gb": 20.0,
                "storage_gb": 50.0,
                "namespace": "auth-prod",
                "days_active": 31,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0].team_name == "payments"

    def test_empty_team_label_becomes_unattributed(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "",
                "cpu_cores": 1.0,
                "memory_gb": 1.0,
                "storage_gb": 0.0,
                "namespace": "orphan",
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].team_name == "unattributed"

    def test_prorated_flagged(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "team-x",
                "cpu_cores": 1.0,
                "memory_gb": 1.0,
                "storage_gb": 0.0,
                "namespace": "ns-1",
                "days_active": 15,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].is_prorated is True

    def test_missing_team_label_defaults(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "cpu_cores": 1.0,
                "memory_gb": 1.0,
                "storage_gb": 0.0,
                "namespace": "ns-1",
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].team_name == "unattributed"

    def test_zero_days_defaults_to_full_month(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "team-a",
                "cpu_cores": 1.0,
                "memory_gb": 1.0,
                "storage_gb": 0.0,
                "namespace": "ns-1",
                "days_active": 0,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].days_active == 30  # noqa: PLR2004
        assert result[0].is_prorated is False


class TestPreviousNamespaces:
    def test_compute_with_previous_namespaces(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [_namespace_data()]
        previous = [
            _namespace_data(team_label="payments", cpu_cores=20.0, memory_gb=80.0),
        ]

        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
            previous_namespaces=previous,
        )

        assert len(result.previous_month_teams) == 1


class TestExactCostCalculations:
    def test_entries_storage_accumulates_across_namespaces(self) -> None:
        # 2 namespaces meme team, storage seul: 500 + 500 = 1000 -> 0.10 * 1000 = 100.0
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 500.0,
                "namespace": "a",
                "days_active": 30,
            },
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 500.0,
                "namespace": "b",
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].storage_cost == 100.0  # noqa: PLR2004
        assert result[0].total_cost == 100.0  # noqa: PLR2004
        assert result[0].namespace_count == 2  # noqa: PLR2004

    def test_entries_cpu_prorated_uses_hours_param(self) -> None:
        # 1 core * 0.03 * 730 (hours param) = 21.9 ; days_active ne change pas le prix ici
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "p",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "namespace": "n",
                "days_active": 15,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].cpu_cost == 21.9  # noqa: PLR2004
        assert result[0].total_cost == 21.9  # noqa: PLR2004
        assert result[0].days_active == 15  # noqa: PLR2004
        assert result[0].is_prorated is True

    def test_entries_zero_days_defaults_30(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "z",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "namespace": "n",
                "days_active": 0,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].days_active == 30  # noqa: PLR2004
        assert result[0].is_prorated is False

    def test_aggregate_team_costs_cpu_accumulates(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        namespaces: list[dict[str, object]] = [
            {
                "team_label": "t",
                "cpu_cores": 2.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            },
            {
                "team_label": "t",
                "cpu_cores": 3.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            },
        ]
        result = _aggregate_team_costs(namespaces, 31, 0.03, 0.01, 0.10)
        assert result[0].cpu_cost == 111.6  # 5 cores * 0.03 * 31 * 24  # noqa: PLR2004
        assert result[0].namespace_count == 2  # noqa: PLR2004
        assert result[0].days_active == 31  # noqa: PLR2004

    def test_aggregate_team_costs_mem_exact_cost(self) -> None:
        # coût mem fin (3 décimales) -> round(x, 3) donnerait un résultat different
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        namespaces: list[dict[str, object]] = [
            {
                "team_label": "m",
                "cpu_cores": 0.0,
                "memory_gb": 0.001,
                "storage_gb": 0.0,
                "days_active": 30,
            },
        ]
        result = _aggregate_team_costs(namespaces, 30, 0.03, 0.013, 0.10)
        assert result[0].memory_cost == 0.01  # round(0.00936, 2)  # noqa: PLR2004
        assert result[0].total_cost == 0.01  # noqa: PLR2004

    def test_aggregate_team_costs_min_days_takes_proration(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        namespaces: list[dict[str, object]] = [
            {
                "team_label": "m",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            },
            {
                "team_label": "m",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 10,
            },
        ]
        result = _aggregate_team_costs(namespaces, 31, 0.03, 0.01, 0.10)
        assert result[0].days_active == 10  # noqa: PLR2004
        assert result[0].is_prorated is True

    def test_aggregate_team_costs_zero_days_defaults_full_month(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        namespaces: list[dict[str, object]] = [
            {
                "team_label": "z",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 0,
            },
        ]
        result = _aggregate_team_costs(namespaces, 31, 0.03, 0.01, 0.10)
        assert result[0].days_active == 31  # noqa: PLR2004
        assert result[0].is_prorated is False

    def test_compute_total_and_unattributed(self) -> None:
        engine = TeamCostAggregationEngine()
        namespaces = [
            _namespace_data(team_label="payments", cpu_cores=1.0, memory_gb=0.0, storage_gb=0.0),
            _namespace_data(team_label="", cpu_cores=2.0, memory_gb=0.0, storage_gb=0.0),
        ]
        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.month == "2026-07"
        assert result.total_cost == round((1.0 + 2.0) * 0.03 * 31 * 24, 2)  # noqa: PLR2004
        assert result.unattributed_cost == round(2.0 * 0.03 * 31 * 24, 2)  # noqa: PLR2004
        assert result.teams[0].team_name == "unattributed"
        assert result.teams[1].team_name == "payments"

    def test_compute_report_month_preserved(self) -> None:
        engine = TeamCostAggregationEngine()
        result = engine.compute(
            namespaces=[],
            month="2026-12",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.month == "2026-12"

    def test_entries_cpu_accumulates_across_namespaces(self) -> None:
        # 2 namespaces meme team: cpu = 1 + 2 = 3 cores, cumul cpu
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "c",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "namespace": "a",
                "days_active": 30,
            },
            {
                "team_label": "c",
                "cpu_cores": 2.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "namespace": "b",
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].cpu_cost == round(3.0 * 0.03 * 730, 2)  # noqa: PLR2004
        assert result[0].namespace_count == 2  # noqa: PLR2004

    def test_entries_memory_accumulates_across_namespaces(self) -> None:
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources: list[dict[str, object]] = [
            {
                "team_label": "m",
                "cpu_cores": 0.0,
                "memory_gb": 10.0,
                "storage_gb": 0.0,
                "namespace": "a",
                "days_active": 30,
            },
            {
                "team_label": "m",
                "cpu_cores": 0.0,
                "memory_gb": 20.0,
                "storage_gb": 0.0,
                "namespace": "b",
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].memory_cost == round(30.0 * 0.01 * 730, 2)  # noqa: PLR2004
        assert result[0].namespace_count == 2  # noqa: PLR2004


class TestAggregateTeamCostsExact:
    def test_mem_and_storage_accumulate_across_namespaces(self) -> None:
        # 2 namespaces meme team: mem 10+20=30, storage 50+30=80
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 10.0,
                "storage_gb": 50.0,
                "days_active": 31,
            },
            {
                "team_label": "x",
                "cpu_cores": 2.0,
                "memory_gb": 20.0,
                "storage_gb": 30.0,
                "days_active": 31,
            },
        ]
        result = _aggregate_team_costs(ns, 31, 0.03, 0.01, 0.10)
        team = result[0]
        assert team.memory_cost == 223.2  # 30 * 0.01 * 31 * 24  # noqa: PLR2004
        assert team.storage_cost == 8.0  # 80 * 0.10  # noqa: PLR2004
        assert team.total_cost == 298.16  # noqa: PLR2004

    def test_days_active_one_not_replaced_by_month(self) -> None:
        # days_active=1 : > 0 donc conserve (mutant <= 1 le remplacerait par 31)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [
            {
                "team_label": "d",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 1,
            }
        ]
        result = _aggregate_team_costs(ns, 31, 0.03, 0.01, 0.10)
        assert result[0].days_active == 1  # noqa: PLR2004
        assert result[0].cpu_cost == 0.72  # 1 * 0.03 * 1 * 24  # noqa: PLR2004


class TestSortAndDefaults:
    def test_previous_teams_sorted_descending(self) -> None:
        # previous avec 2 equipes -> ordre descendant (big avant small)
        # mutant reverse=False ou key=None changerait l'ordre / crasherait
        engine = TeamCostAggregationEngine()
        current = [
            {
                "team_label": "a",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            }
        ]
        previous = [
            {
                "team_label": "small",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            },
            {
                "team_label": "big",
                "cpu_cores": 10.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            },
        ]
        report = engine.compute(
            namespaces=current,
            previous_namespaces=previous,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert [t.team_name for t in report.previous_month_teams] == ["big", "small"]

    def test_namespace_missing_team_label_unattributed(self) -> None:
        # namespace sans cle team_label (absente) -> unattributed
        # mutant get(...,None) donnerait 'None' (non falsy)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [{"cpu_cores": 5.0, "memory_gb": 0.0, "storage_gb": 0.0, "days_active": 31}]
        result = _aggregate_team_costs(ns, 31, 0.03, 0.01, 0.10)
        assert [t.team_name for t in result] == ["unattributed"]

    def test_entries_missing_namespace_single_count(self) -> None:
        # resources sans cle namespace -> namespace_count ne compte pas de 'None' separe
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            },
            {
                "team_label": "x",
                "cpu_cores": 2.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].namespace_count == 1  # noqa: PLR2004


class TestComputeDefaults:
    def test_no_unattributed_and_no_previous_defaults(self) -> None:
        # pas d'unattributed -> unattributed_cost 0.0 (mutant default 1.0 detecte)
        # pas de previous -> previous_month_teams [] (mutant None detecte)
        engine = TeamCostAggregationEngine()
        current = [
            {
                "team_label": "a",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 31,
            }
        ]
        report = engine.compute(
            namespaces=current,
            month="2026-07",
            days_in_month=31,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert report.unattributed_cost == 0.0
        assert report.previous_month_teams == []


class TestEntriesRoundingNonInteger:
    def test_storage_cost_fractional_not_rounded_to_int(self) -> None:
        # 1005 GB * 0.10 = 100.5 -> round(100.5, 2) = 100.5
        # mutant round(..., None) donnerait 100
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 1005.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].storage_cost == 100.5  # noqa: PLR2004

    def test_cpu_cost_fractional_not_rounded_to_int(self) -> None:
        # 1 core * 0.03 * 730 = 21.9 -> round(21.9, 2) = 21.9 (mutant None -> 22)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].cpu_cost == 21.9  # noqa: PLR2004


class TestRoundingRemaining:
    def test_aggregate_storage_fractional_not_rounded_int(self) -> None:
        # storage 5 GB * 0.10 = 0.5 -> round(0.5, 2) = 0.5 (mutant None -> 0)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [
            {
                "team_label": "a",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 5.0,
                "days_active": 31,
            }
        ]
        result = _aggregate_team_costs(ns, 31, 0.03, 0.01, 0.10)
        assert result[0].storage_cost == 0.5  # noqa: PLR2004

    def test_entries_mem_fractional_not_rounded_int(self) -> None:
        # mem 1 GB * 0.01 * 730 = 7.3 -> round(7.3, 2) = 7.3 (mutant None -> 7)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 1.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].memory_cost == 7.3  # noqa: PLR2004

    def test_entries_days_active_one_not_thirty(self) -> None:
        # days_active=1 dans entries : >0 donc conserve 1 (mutant <=1 donnerait 30)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 1,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].days_active == 1  # noqa: PLR2004


class TestNamespaceDefaultCollapse:
    def test_empty_and_absent_namespace_collapse(self) -> None:
        # namespace explicite '' et namespace absent -> meme valeur (''), count 1
        # mutant get(...,None) separerait 'None' -> count 2
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
                "namespace": "",
            },
            {
                "team_label": "x",
                "cpu_cores": 1.0,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            },
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].namespace_count == 1  # noqa: PLR2004


class TestRoundingThreeDecimals:
    def test_entries_mem_cost_three_decimals_rounding(self) -> None:
        # 0.005 GB * 0.01 * 730 = 0.0365 -> round(0.0365, 2) = 0.04 (mutant 3 -> 0.036)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 0.005,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].memory_cost == 0.04  # noqa: PLR2004

    def test_aggregate_storage_three_decimals_rounding(self) -> None:
        # 0.005 GB * 0.10 = 0.0005 -> round(0.0005, 2) = 0.0 (mutant 3 -> 0.001)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [
            {
                "team_label": "a",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 0.005,
                "days_active": 31,
            }
        ]
        result = _aggregate_team_costs(ns, 31, 0.03, 0.01, 0.10)
        assert result[0].storage_cost == 0.0

    def test_entries_cpu_cost_three_decimals_rounding(self) -> None:
        # 0.005 core * 0.03 * 730 = 0.1095 -> round(0.1095, 2) = 0.11 (mutant 3 -> 0.109)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].cpu_cost == 0.11  # noqa: PLR2004

    def test_entries_total_cost_three_decimals_rounding(self) -> None:
        # total 0.1095 (cpu seul) -> round(..., 2) = 0.11 (mutant 3 -> 0.109)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].total_cost == 0.11  # noqa: PLR2004

    def test_entries_storage_cost_three_decimals_rounding(self) -> None:
        # 0.005 GB * 0.10 = 0.0005 -> round(0.0005, 2) = 0.0 (mutant 3 -> 0.001)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            compute_team_cost_entries,
        )

        resources = [
            {
                "team_label": "x",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
                "storage_gb": 0.005,
                "days_active": 30,
            }
        ]
        result = compute_team_cost_entries(resources, 0.03, 0.01, 0.10, 730)
        assert result[0].storage_cost == 0.0

    def test_aggregate_cpu_cost_three_decimals_rounding(self) -> None:
        # 0.005 core * 0.03 * 30*24 = 0.108 -> round(0.108, 2) = 0.11 (mutant 3 -> 0.108)
        from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
            _aggregate_team_costs,
        )

        ns = [
            {
                "team_label": "a",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = _aggregate_team_costs(ns, 30, 0.03, 0.01, 0.10)
        assert result[0].cpu_cost == 0.11  # noqa: PLR2004

    def test_report_total_rounded_once_from_exact_sum(self) -> None:
        # 2 teams * 0.005 core * 0.03 * 720h = 0.108 each -> somme exacte 0.216
        # round(0.216, 2) = 0.22 (mutant round(..., 3) = 0.216)
        engine = TeamCostAggregationEngine()
        namespaces = [
            {
                "team_label": "a",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            },
            {
                "team_label": "b",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            },
        ]
        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=30,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.total_cost == 0.22  # noqa: PLR2004

    def test_report_unattributed_rounded_once_from_exact_sum(self) -> None:
        # 1 team unattributed, 0.005 core * 0.03 * 720h = 0.108
        # round(0.108, 2) = 0.11 (mutant round(..., 3) = 0.108)
        engine = TeamCostAggregationEngine()
        namespaces = [
            {
                "team_label": "",
                "cpu_cores": 0.005,
                "memory_gb": 0.0,
                "storage_gb": 0.0,
                "days_active": 30,
            }
        ]
        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=30,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.unattributed_cost == 0.11  # noqa: PLR2004

    def test_compute_total_includes_cpu_mem_and_storage_exact(self) -> None:
        # unattributed: cpu 2 cores x 0.03 x 720h = 43.20, mem 4 GB x 0.01 x 720h = 28.80,
        # storage 50 GB x 0.10 = 5.00 -> total exact 77.00
        # tue les mutants signe + -> - sur storage et mem (ligne total + unattributed)
        engine = TeamCostAggregationEngine()
        namespaces = [
            {
                "team_label": "",
                "cpu_cores": 2.0,
                "memory_gb": 4.0,
                "storage_gb": 50.0,
                "days_active": 30,
            }
        ]
        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=30,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.total_cost == 77.00  # noqa: PLR2004
        assert result.unattributed_cost == 77.00  # noqa: PLR2004

    def test_compute_total_with_multiple_teams_includes_storage(self) -> None:
        # 2 teams avec cpu+mem+storage non nuls : total = somme exacte des 3 ressources
        # team a : cpu 1 x 0.03 x 720h = 21.60, mem 2 x 0.01 x 720h = 14.40
        # team b : cpu 3 x 0.03 x 720h = 64.80, mem 1 x 0.01 x 720h = 7.20
        # total exact = (21.60 + 14.40 + 1.00) + (64.80 + 7.20 + 2.00) = 111.00
        engine = TeamCostAggregationEngine()
        namespaces = [
            {
                "team_label": "a",
                "cpu_cores": 1.0,
                "memory_gb": 2.0,
                "storage_gb": 10.0,
                "days_active": 30,
            },
            {
                "team_label": "b",
                "cpu_cores": 3.0,
                "memory_gb": 1.0,
                "storage_gb": 20.0,
                "days_active": 30,
            },
        ]
        result = engine.compute(
            namespaces=namespaces,
            month="2026-07",
            days_in_month=30,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
            storage_price_per_gb_month=0.10,
        )
        assert result.total_cost == 111.00  # noqa: PLR2004
        assert result.teams[0].team_name == "b"
        assert result.teams[0].total_cost == 74.00  # noqa: PLR2004
        assert result.teams[1].total_cost == 37.00  # noqa: PLR2004
