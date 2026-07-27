from __future__ import annotations

from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot


def _snap(  # noqa: PLR0913
    name: str = "prod-eu",
    failing: int = 5,
    total: int = 200,
    cpu: float = 72.0,
    memory: float = 68.0,
    nodes: int = 12,
    nodes_bad: int = 0,
    incidents: int = 1,
    health: str = "degraded",
    maintenance: bool = False,
    reachable: bool = True,
) -> ClusterHealthSnapshot:
    return ClusterHealthSnapshot(
        cluster_name=name,
        failing_pods=failing,
        total_pods=total,
        cpu_utilization_pct=cpu,
        memory_utilization_pct=memory,
        node_count=nodes,
        nodes_not_ready=nodes_bad,
        active_incidents=incidents,
        health_status=health,
        in_maintenance=maintenance,
        reachable=reachable,
    )


class TestComparison:
    def test_ticket_scenario(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", failing=5, total=200, cpu=72.0, incidents=1),
            _snap("prod-us", failing=1, total=100, cpu=45.0, incidents=0, health="healthy"),
        )

        assert result.comparison.worse_cluster == "prod-eu"
        assert result.comparison.delta_failing_pods == 4  # noqa: PLR2004
        assert result.comparison.delta_cpu_pct == 27.0  # noqa: PLR2004

    def test_both_healthy_no_winner(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", failing=0, incidents=0, health="healthy"),
            _snap("prod-us", failing=0, incidents=0, health="healthy"),
        )

        assert result.comparison.worse_cluster is None
        assert "both" in result.comparison.reason.lower()


class TestMaintenance:
    def test_cordoned_not_degraded(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", maintenance=True),
            _snap("prod-us", health="healthy"),
        )

        assert result.cluster_a.in_maintenance is True
        assert "maintenance" in result.comparison.reason.lower()


class TestUnreachable:
    def test_unreachable_shown_as_partial(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", reachable=True),
            _snap("prod-us", reachable=False),
        )

        assert result.cluster_b.reachable is False
        assert "unreachable" in result.comparison.reason.lower()

    def test_both_unreachable(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", reachable=False),
            _snap("prod-us", reachable=False),
        )

        assert result.comparison.worse_cluster is None
        assert "unreachable" in result.comparison.reason.lower()


class TestNormalization:
    def test_normalized_when_size_differs(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snap("prod-eu", failing=10, total=200),
            _snap("prod-us", failing=2, total=50),
        )

        # 10/200*100=5.0 vs 2/50*100=4.0 — normalized, prod-eu still worse.
        assert result.comparison.normalized_a_failing_per_100 > 0
        assert result.comparison.normalized_b_failing_per_100 > 0
