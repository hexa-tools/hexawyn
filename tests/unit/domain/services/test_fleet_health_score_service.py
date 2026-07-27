"""Tests for fleet_health_score_service — comprehensive with edge cases."""

from __future__ import annotations

from hexawyn.domain.models.fleet_health import (
    ClusterRawMetrics,
)
from hexawyn.domain.services.fleet_health.fleet_health_score_service import (
    aggregate_fleet,
    build_cluster_report,
    compute_fleet_trend,
    compute_health_score,
    make_unreachable_report,
)


def _metrics(**overrides: object) -> ClusterRawMetrics:
    defaults: dict[str, object] = {
        "context_name": "test-cluster",
        "nodes_total": 10,
        "nodes_not_ready": 0,
        "pods_total": 100,
        "pods_running": 99,
        "pods_crashloop": 1,
        "cpu_utilization": 0.5,
        "memory_utilization": 0.5,
        "certs_expiring_critical": 0,
        "certs_expiring_warning": 0,
        "security_violations": 0,
        "pipelines_failing": 0,
        "prometheus_available": True,
    }
    return ClusterRawMetrics(**{**defaults, **overrides})  # type: ignore[arg-type]


class TestComputeHealthScore:
    def test_perfect_cluster(self) -> None:
        score = compute_health_score(_metrics())
        assert score == 100  # noqa: PLR2004

    def test_nodes_not_ready_penalty(self) -> None:
        score = compute_health_score(_metrics(nodes_not_ready=3))
        assert score == 40  # 100 - 20*3  # noqa: PLR2004

    def test_crashloop_penalty(self) -> None:
        score = compute_health_score(_metrics(pods_crashloop=50, pods_total=100))
        assert score < 100  # noqa: PLR2004
        assert score >= 60  # 100 - int(0.5 * 40) = 80  # noqa: PLR2004

    def test_crashloop_empty_cluster_no_penalty(self) -> None:
        score = compute_health_score(_metrics(pods_total=0, pods_crashloop=0))
        assert score == 100  # noqa: PLR2004

    def test_cpu_critical(self) -> None:
        score = compute_health_score(_metrics(cpu_utilization=0.95))
        assert score == 85  # 100 - 15  # noqa: PLR2004

    def test_cpu_warning(self) -> None:
        score = compute_health_score(_metrics(cpu_utilization=0.85))
        assert score == 92  # 100 - 8  # noqa: PLR2004

    def test_cpu_unknown_no_penalty(self) -> None:
        score = compute_health_score(_metrics(cpu_utilization=None))
        assert score == 100  # noqa: PLR2004

    def test_memory_critical(self) -> None:
        score = compute_health_score(_metrics(memory_utilization=0.95))
        assert score == 85  # noqa: PLR2004

    def test_certs_critical(self) -> None:
        score = compute_health_score(_metrics(certs_expiring_critical=2))
        assert score == 90  # 100 - 10 (flat)  # noqa: PLR2004

    def test_certs_warning(self) -> None:
        score = compute_health_score(_metrics(certs_expiring_warning=3))
        assert score == 95  # 100 - 5 (flat)  # noqa: PLR2004

    def test_security_violations_capped(self) -> None:
        score = compute_health_score(_metrics(security_violations=20))
        assert score == 85  # min(20*3, 15) = 15 penalty  # noqa: PLR2004

    def test_pipelines_failing(self) -> None:
        score = compute_health_score(_metrics(pipelines_failing=3))
        assert score == 100  # pipelines don't affect score  # noqa: PLR2004

    def test_score_never_below_zero(self) -> None:
        score = compute_health_score(
            _metrics(
                nodes_not_ready=10,
                pods_crashloop=1000,
                cpu_utilization=0.99,
                memory_utilization=0.99,
                certs_expiring_critical=100,
                security_violations=100,
            )
        )
        assert score == 0

    def test_max_penalty(self) -> None:
        score = compute_health_score(_metrics(nodes_not_ready=5))
        assert score == 0


class TestBuildClusterReport:
    def test_healthy(self) -> None:
        m = _metrics()
        report = build_cluster_report(m)
        assert report.reachable
        assert report.health_status == "healthy"
        assert report.health_score == 100  # noqa: PLR2004
        assert len(report.categories) == 7  # noqa: PLR2004

    def test_degraded(self) -> None:
        m = _metrics(nodes_not_ready=2)
        report = build_cluster_report(m)
        assert report.health_status == "degraded"

    def test_critical(self) -> None:
        m = _metrics(nodes_not_ready=5)
        report = build_cluster_report(m)
        assert report.health_status == "critical"


class TestMakeUnreachableReport:
    def test(self) -> None:
        report = make_unreachable_report("ctx", "timeout")
        assert not report.reachable
        assert report.health_status == "unreachable"
        assert report.health_score is None
        assert report.unreachable_reason == "timeout"


class TestAggregateFleet:
    def test_empty(self) -> None:
        report = aggregate_fleet([])
        assert report.fleet_score is None
        assert report.fleet_status == "unknown"

    def test_mixed(self) -> None:
        healthy = build_cluster_report(_metrics(context_name="a"))
        degraded = build_cluster_report(_metrics(context_name="b", nodes_not_ready=3))
        unreachable = make_unreachable_report("c", "timeout")
        report = aggregate_fleet([healthy, degraded, unreachable])
        assert report.reachable_count == 2  # noqa: PLR2004
        assert report.unreachable_count == 1

    def test_all_unreachable(self) -> None:
        reports = [make_unreachable_report("a", "x"), make_unreachable_report("b", "y")]
        report = aggregate_fleet(reports)
        assert report.fleet_status == "no_cluster_reachable"
        assert report.fleet_score is None


class TestComputeFleetTrend:
    def test_improving(self) -> None:
        assert compute_fleet_trend(100.0, 120.0) == "improving"

    def test_degrading(self) -> None:
        assert compute_fleet_trend(100.0, 80.0) == "degrading"

    def test_stable(self) -> None:
        assert compute_fleet_trend(100.0, 105.0) == "stable"

    def test_none_previous(self) -> None:
        assert compute_fleet_trend(None, 100.0) is None

    def test_none_current(self) -> None:
        assert compute_fleet_trend(100.0, None) is None

    def test_zero_previous(self) -> None:
        assert compute_fleet_trend(0.0, 100.0) is None

    def test_exact_boundary_10pct(self) -> None:
        assert compute_fleet_trend(100.0, 110.0) == "stable"
