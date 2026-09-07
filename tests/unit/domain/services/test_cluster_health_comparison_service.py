from __future__ import annotations

from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


def _snapshot(  # noqa: PLR0913
    name: str = "prod-eu",
    failing: int = 0,
    total: int = 100,
    cpu: float = 0.0,
    memory: float = 0.0,
    nodes: int = 5,
    nodes_bad: int = 0,
    incidents: int = 0,
    health: str = "healthy",
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


def _raw(  # noqa: PLR0913
    name: str = "prod-eu",
    nodes_total: int = 12,
    nodes_not_ready: int = 0,
    pods_total: int = 200,
    pods_running: int = 195,
    cpu: float | None = 0.72,
    memory: float | None = 0.68,
    pipelines_failing: int = 1,
) -> ClusterRawMetrics:
    return ClusterRawMetrics(
        context_name=name,
        nodes_total=nodes_total,
        nodes_not_ready=nodes_not_ready,
        pods_total=pods_total,
        pods_running=pods_running,
        pods_crashloop=0,
        cpu_utilization=cpu,
        memory_utilization=memory,
        certs_expiring_critical=0,
        certs_expiring_warning=0,
        security_violations=0,
        pipelines_failing=pipelines_failing,
        prometheus_available=True,
    )


class TestToSnapshot:
    def test_maps_every_raw_field_exactly(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            to_snapshot,
        )

        result = to_snapshot(
            _raw(
                name="prod-eu",
                nodes_total=12,
                nodes_not_ready=2,
                pods_total=200,
                pods_running=180,
                pipelines_failing=4,
            )
        )

        assert result.cluster_name == "prod-eu"
        assert result.failing_pods == 20  # noqa: PLR2004
        assert result.total_pods == 200  # noqa: PLR2004
        assert result.cpu_utilization_pct == 72.0  # noqa: PLR2004
        assert result.memory_utilization_pct == 68.0  # noqa: PLR2004
        assert result.node_count == 12  # noqa: PLR2004
        assert result.nodes_not_ready == 2  # noqa: PLR2004
        assert result.active_incidents == 4  # noqa: PLR2004
        assert result.health_status == "degraded"
        assert result.in_maintenance is False
        assert result.reachable is True

    def test_zero_cpu_utilization_stays_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            to_snapshot,
        )

        result = to_snapshot(_raw(cpu=0.0, memory=0.0, pods_total=5, pods_running=5))

        assert result.cpu_utilization_pct == 0.0
        assert result.memory_utilization_pct == 0.0

    def test_none_utilization_becomes_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            to_snapshot,
        )

        result = to_snapshot(_raw(cpu=None, memory=None, pods_total=5, pods_running=5))

        assert result.cpu_utilization_pct == 0.0
        assert result.memory_utilization_pct == 0.0

    def test_healthy_when_no_failing_pods(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            to_snapshot,
        )

        result = to_snapshot(_raw(pods_total=10, pods_running=10))

        assert result.failing_pods == 0
        assert result.health_status == "healthy"

    def test_degraded_when_one_failing_pod(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            to_snapshot,
        )

        result = to_snapshot(_raw(pods_total=10, pods_running=9))

        assert result.failing_pods == 1  # noqa: PLR2004
        assert result.health_status == "degraded"


class TestScore:
    def test_score_combines_all_terms(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            score,
        )

        # normalized (5/200*100=2.5)*2 + cpu 0.72 + incidents 3*5 + nodes_bad 1*10
        result = score(_snapshot(failing=5, total=200, cpu=72.0, incidents=3, nodes_bad=1))

        assert result == 2.5 * 2 + 0.72 + 15.0 + 10.0  # noqa: PLR2004

    def test_score_zero_when_all_terms_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            score,
        )

        assert score(_snapshot(failing=0, total=100, cpu=0.0, incidents=0, nodes_bad=0)) == 0.0

    def test_score_single_failing_dominant(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            score,
        )

        # 2 failing/100 pods normalized -> 2*2 = 4
        assert score(_snapshot(failing=2, total=100)) == 4.0  # noqa: PLR2004


class TestFailingPerHundred:
    def test_zero_when_total_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            _failing_per_100,
        )

        assert _failing_per_100(_snapshot(failing=3, total=0)) == 0.0

    def test_negative_total_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            _failing_per_100,
        )

        assert _failing_per_100(_snapshot(failing=3, total=-5)) == 0.0

    def test_one_failing_one_total_not_zero(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            _failing_per_100,
        )

        assert _failing_per_100(_snapshot(failing=1, total=1)) == 100.0  # noqa: PLR2004

    def test_fractional_percentage_exact(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            _failing_per_100,
        )

        assert _failing_per_100(_snapshot(failing=3, total=10)) == 30.0  # noqa: PLR2004

    def test_plain_ratio(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            _failing_per_100,
        )

        assert _failing_per_100(_snapshot(failing=1, total=4)) == 25.0  # noqa: PLR2004


class TestComparison:
    def test_worse_cluster_and_exact_report(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        cluster_a = _snapshot("prod-eu", failing=5, total=200, cpu=72.0, incidents=1)
        cluster_b = _snapshot("prod-us", failing=1, total=100, cpu=45.0, incidents=0)

        result = compare(cluster_a, cluster_b)

        assert result.cluster_a is cluster_a
        assert result.cluster_b is cluster_b
        assert result.comparison.worse_cluster == "prod-eu"
        assert result.comparison.delta_failing_pods == 4  # noqa: PLR2004
        assert result.comparison.delta_cpu_pct == 27.0  # noqa: PLR2004
        assert result.comparison.delta_active_incidents == 1  # noqa: PLR2004
        assert result.comparison.normalized_a_failing_per_100 == 2.5  # noqa: PLR2004
        assert result.comparison.normalized_b_failing_per_100 == 1.0
        assert (
            result.comparison.reason
            == "prod-eu has 4 more failing pods, 27pp higher CPU, 1 more active incidents"
        )

    def test_tie_scores_prefer_cluster_b(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # equal failing ratio (2%) + equal cpu -> identical score => strict > picks cluster_b
        result = compare(
            _snapshot("eu", failing=2, total=100, cpu=50.0),
            _snapshot("us", failing=1, total=50, cpu=50.0),
        )

        assert result.comparison.worse_cluster == "us"
        assert result.comparison.delta_failing_pods == 1  # noqa: PLR2004

    def test_reason_uses_worse_name_and_absolute_deltas(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", failing=1, total=100),
            _snapshot("us", failing=6, total=100),
        )

        assert result.comparison.worse_cluster == "us"
        assert (
            result.comparison.reason
            == "us has 5 more failing pods, 0pp higher CPU, 0 more active incidents"
        )

    def test_score_gap_of_one_point_still_picks_better(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # cpu gap gives score diff 100*0.01 = 1.0 (>= 0.5) -> real winner, not "both_healthy"
        result = compare(
            _snapshot("eu", cpu=100.0),
            _snapshot("us", cpu=0.0),
        )

        assert result.comparison.worse_cluster == "eu"
        assert result.comparison.reason != "both_healthy"

    def test_score_gap_exactly_half_point_is_winner(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # cpu gap 50 -> score diff exactly 0.5; healthy requires < 0.5, so a winner exists
        result = compare(
            _snapshot("eu", cpu=50.0),
            _snapshot("us", cpu=0.0),
        )

        assert result.comparison.worse_cluster == "eu"
        assert result.comparison.delta_cpu_pct == 50.0  # noqa: PLR2004

    def test_delta_cpu_rounded_to_one_decimal(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", failing=2, total=10, cpu=72.34),
            _snapshot("us", failing=1, total=10, cpu=45.0),
        )

        assert result.comparison.delta_cpu_pct == 27.3  # noqa: PLR2004
        assert (
            result.comparison.reason
            == "eu has 1 more failing pods, 27pp higher CPU, 0 more active incidents"
        )

    def test_normalized_rounded_to_one_decimal(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # 1/3*100 = 33.333 -> round(1) = 33.3 (mutant round(2) -> 33.33 kills)
        result = compare(
            _snapshot("eu", failing=1, total=3),
            _snapshot("us", failing=0, total=3),
        )

        assert result.comparison.normalized_a_failing_per_100 == 33.3  # noqa: PLR2004

    def test_else_branch_normalized_b_rounded_to_one_decimal(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # both normalized fractional: a=66.667, b=33.333 -> winner exists (delta_failing=1).
        result = compare(
            _snapshot("eu", failing=2, total=3),
            _snapshot("us", failing=1, total=3),
        )

        assert result.comparison.worse_cluster == "eu"
        assert result.comparison.normalized_a_failing_per_100 == 66.7  # noqa: PLR2004
        assert result.comparison.normalized_b_failing_per_100 == 33.3  # noqa: PLR2004

    def test_rounding_in_healthy_branch_normalized(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", failing=0, total=3),
            _snapshot("us", failing=0, total=3),
        )

        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "both_healthy"
        assert result.comparison.normalized_a_failing_per_100 == 0.0
        assert result.comparison.normalized_b_failing_per_100 == 0.0

    def test_delta_incidents_signed_exact(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", failing=0, incidents=5),
            _snapshot("us", failing=0, incidents=2),
        )

        assert result.comparison.delta_active_incidents == 3  # noqa: PLR2004
        assert (
            result.comparison.reason
            == "eu has 0 more failing pods, 0pp higher CPU, 3 more active incidents"
        )


class TestBothHealthyBranch:
    def test_identical_failing_zero_reports_both_healthy(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", failing=0, incidents=0),
            _snapshot("us", failing=0, incidents=0),
        )

        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "both_healthy"
        assert result.cluster_a is not None
        assert result.cluster_b is not None

    def test_healthy_requires_zero_incident_delta(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # same failing delta zero but incidents differ -> NOT both_healthy
        result = compare(
            _snapshot("eu", failing=0, incidents=1),
            _snapshot("us", failing=0, incidents=0),
        )

        assert result.comparison.worse_cluster == "eu"
        assert result.comparison.reason != "both_healthy"

    def test_healthy_branch_preserves_fractional_normalized_values(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # failing delta 0 and incident delta 0 with equal scores -> both_healthy.
        # 1/3*100 = 33.333: round(,1)=33.3, round(,2)=33.33, round(,None)=33, default=0.0
        result = compare(
            _snapshot("eu", failing=1, total=3, incidents=0),
            _snapshot("us", failing=1, total=3, incidents=0),
        )

        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "both_healthy"
        assert result.comparison.normalized_a_failing_per_100 == 33.3  # noqa: PLR2004
        assert result.comparison.normalized_b_failing_per_100 == 33.3  # noqa: PLR2004

    def test_healthy_branch_requires_score_gap_below_half(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        # equal low cpu (score 0.3 each): |a-b|=0 < 0.5 but |a+b|=0.6 -> mutant |a+b|<0.5 breaks
        result = compare(
            _snapshot("eu", failing=0, cpu=30.0),
            _snapshot("us", failing=0, cpu=30.0),
        )

        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "both_healthy"


class TestUnreachable:
    def test_partial_unreachable_exact_reason(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        cluster_a = _snapshot("eu", reachable=True)
        cluster_b = _snapshot("us", reachable=False)

        result = compare(cluster_a, cluster_b)

        assert result.cluster_a is cluster_a
        assert result.cluster_b is cluster_b
        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "partial_comparison_unreachable"

    def test_partial_unreachable_other_side(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        cluster_a = _snapshot("eu", reachable=False)
        cluster_b = _snapshot("us", reachable=True)

        result = compare(cluster_a, cluster_b)

        assert result.comparison.reason == "partial_comparison_unreachable"

    def test_both_unreachable_exact_reason(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("eu", reachable=False),
            _snapshot("us", reachable=False),
        )

        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "both_clusters_unreachable"


class TestMaintenance:
    def test_cluster_a_in_maintenance_exact_reason(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        cluster_a = _snapshot("prod-eu", maintenance=True)
        cluster_b = _snapshot("prod-us")

        result = compare(cluster_a, cluster_b)

        assert result.cluster_a is cluster_a
        assert result.cluster_b is cluster_b
        assert result.comparison.worse_cluster is None
        assert result.comparison.reason == "prod-eu is in maintenance (not degraded)"

    def test_cluster_b_in_maintenance_exact_reason(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("prod-eu"),
            _snapshot("prod-us", maintenance=True),
        )

        assert result.comparison.reason == "prod-us is in maintenance (not degraded)"

    def test_both_in_maintenance_names_cluster_a(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("prod-eu", maintenance=True),
            _snapshot("prod-us", maintenance=True),
        )

        assert result.comparison.reason == "prod-eu is in maintenance (not degraded)"

    def test_unreachable_takes_precedence_over_maintenance(self) -> None:
        from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
            compare,
        )

        result = compare(
            _snapshot("prod-eu", maintenance=True),
            _snapshot("prod-us", reachable=False),
        )

        assert result.comparison.reason == "partial_comparison_unreachable"
