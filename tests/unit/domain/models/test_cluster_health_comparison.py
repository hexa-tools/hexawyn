from dataclasses import fields


class TestClusterHealthSnapshot:
    def test_fields(self) -> None:
        from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot

        names = {f.name for f in fields(ClusterHealthSnapshot)}
        assert names == {
            "cluster_name",
            "failing_pods",
            "total_pods",
            "cpu_utilization_pct",
            "memory_utilization_pct",
            "node_count",
            "nodes_not_ready",
            "active_incidents",
            "health_status",
            "in_maintenance",
            "reachable",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot

        snap = ClusterHealthSnapshot(
            cluster_name="prod-eu",
            failing_pods=5,
            total_pods=200,
            cpu_utilization_pct=72.0,
            memory_utilization_pct=68.0,
            node_count=12,
            nodes_not_ready=0,
            active_incidents=1,
            health_status="degraded",
            in_maintenance=False,
            reachable=True,
        )

        assert snap.cluster_name == "prod-eu"
        assert snap.failing_pods == 5


class TestComparisonReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.cluster_health_comparison import ComparisonReport

        report = ComparisonReport(worse_cluster=None, reason="both_healthy")

        assert report.worse_cluster is None
        assert report.reason == "both_healthy"
        assert report.delta_failing_pods == 0

    def test_holds_delta(self) -> None:
        from hexawyn.domain.models.cluster_health_comparison import ComparisonReport

        report = ComparisonReport(
            worse_cluster="prod-eu",
            reason="prod-eu has 4 more failing pods, 27pp higher CPU",
            delta_failing_pods=4,
            delta_cpu_pct=27.0,
            delta_active_incidents=1,
        )

        assert report.worse_cluster == "prod-eu"
        assert report.delta_cpu_pct == 27.0


class TestHealthComparisonResult:
    def test_holds_both_snapshots(self) -> None:
        from hexawyn.domain.models.cluster_health_comparison import (
            ClusterHealthSnapshot,
            ComparisonReport,
            HealthComparisonResult,
        )

        a = ClusterHealthSnapshot(
            cluster_name="prod-eu",
            failing_pods=5,
            total_pods=200,
            cpu_utilization_pct=72.0,
            memory_utilization_pct=68.0,
            node_count=12,
            nodes_not_ready=0,
            active_incidents=1,
            health_status="degraded",
            in_maintenance=False,
            reachable=True,
        )
        b = ClusterHealthSnapshot(
            cluster_name="prod-us",
            failing_pods=1,
            total_pods=100,
            cpu_utilization_pct=45.0,
            memory_utilization_pct=52.0,
            node_count=10,
            nodes_not_ready=0,
            active_incidents=0,
            health_status="healthy",
            in_maintenance=False,
            reachable=True,
        )
        report = ComparisonReport(worse_cluster="prod-eu", reason="test")

        result = HealthComparisonResult(cluster_a=a, cluster_b=b, comparison=report)

        assert result.cluster_a.cluster_name == "prod-eu"
        assert result.cluster_b.cluster_name == "prod-us"
        assert result.comparison.worse_cluster == "prod-eu"
