"""RED → GREEN — Team Cost Aggregation domain logic."""

from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
    TeamCostAggregationEngine,
)


def _namespace_data(
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
                namespace="infra-prod", team_label="infra", cpu_cores=10.0, memory_gb=40.0
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

        assert len(result.teams) == 3
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

        assert result.teams[0].total_cost < 1000.0

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
        assert result.teams[0].namespace_count == 3

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
