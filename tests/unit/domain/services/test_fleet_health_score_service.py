"""Tests for fleet_health_score_service — comprehensive with edge cases."""

from __future__ import annotations

from hexawyn.domain.models.fleet_health import (
    ClusterRawMetrics,
)
from hexawyn.domain.services.fleet_health.fleet_health_score_service import (
    _cert_category,
    _cpu_category,
    _health_status_from_score,
    _memory_category,
    _node_category,
    _pipeline_category,
    _pod_category,
    _security_category,
    aggregate_fleet,
    build_categories,
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

    def test_memory_warning(self) -> None:
        score = compute_health_score(_metrics(memory_utilization=0.85))
        assert score == 92  # 100 - 8  # noqa: PLR2004

    def test_memory_exact_warning_boundary(self) -> None:
        # 0.80 n'est PAS > 0.80 -> pas de penalite; le mutant >= donnerait 92
        score = compute_health_score(_metrics(memory_utilization=0.80))
        assert score == 100  # noqa: PLR2004

    def test_certs_critical(self) -> None:
        score = compute_health_score(_metrics(certs_expiring_critical=2))
        assert score == 90  # 100 - 10 (flat)  # noqa: PLR2004

    def test_certs_critical_boundary(self) -> None:
        # critical=1, warning=0 -> penalty 10; le mutant critical>1 donnerait 0
        score = compute_health_score(_metrics(certs_expiring_critical=1))
        assert score == 90  # noqa: PLR2004

    def test_certs_warning_boundary(self) -> None:
        # warning=1, critical=0 -> penalty 5; le mutant warning>1 donnerait 0
        score = compute_health_score(_metrics(certs_expiring_warning=1))
        assert score == 95  # noqa: PLR2004

    def test_certs_warning(self) -> None:
        score = compute_health_score(_metrics(certs_expiring_warning=3))
        assert score == 95  # 100 - 5 (flat)  # noqa: PLR2004

    def test_security_violations_capped(self) -> None:
        score = compute_health_score(_metrics(security_violations=20))
        assert score == 85  # min(20*3, 15) = 15 penalty  # noqa: PLR2004

    def test_security_violations_below_cap(self) -> None:
        # 2 violations -> 6, pas de cap: le mutant *4 donnerait 8
        score = compute_health_score(_metrics(security_violations=2))
        assert score == 94  # noqa: PLR2004

    def test_cpu_exact_warning_boundary(self) -> None:
        # 0.80 n'est PAS > 0.80 -> pas de penalite (score 100)
        score = compute_health_score(_metrics(cpu_utilization=0.80))
        assert score == 100  # noqa: PLR2004

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

    def test_crashloop_zero_total_no_crash(self) -> None:
        # Division par zero evitee (max(pods_total, 1)), score inchange
        score = compute_health_score(_metrics(pods_total=0, pods_crashloop=0))
        assert score == 100  # noqa: PLR2004

    def test_crashloop_zero_total_with_crash(self) -> None:
        # pods_total=0 avec crashloop > 0: ratio <> 0, pas de division par zero
        score = compute_health_score(_metrics(pods_total=0, pods_crashloop=5))
        assert score < 100  # noqa: PLR2004

    def test_crashloop_single_pod_one_crash(self) -> None:
        # pods_total=1, pods_crashloop=1 -> max(1,1)=1 vs max(1,2)=2
        # ratio = 1.0 (mutant max(total,2) donnerait 0.5) -> score differ
        score = compute_health_score(_metrics(pods_total=1, pods_crashloop=1))
        assert score == 60  # 100 - int(1.0 * 40)  # noqa: PLR2004

    def test_cpu_exact_critical_boundary(self) -> None:
        # seuil > 0.90: 0.90 n'est PAS critique -> passe au warning (0.80)
        score = compute_health_score(_metrics(cpu_utilization=0.90))
        assert score == 92  # 100 - 8 (warning), mutant >=0.90 donnerait 85  # noqa: PLR2004

    def test_memory_exact_critical_boundary(self) -> None:
        score = compute_health_score(_metrics(memory_utilization=0.90))
        assert score == 92  # noqa: PLR2004


class TestBuildClusterReport:
    def test_healthy(self) -> None:
        m = _metrics()
        report = build_cluster_report(m)
        assert report.reachable
        assert report.health_status == "healthy"
        assert report.health_score == 100  # noqa: PLR2004
        assert report.context_name == "test-cluster"
        assert report.unreachable_reason is None
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
    def test_make_unreachable_report(self) -> None:
        report = make_unreachable_report("ctx", "timeout")
        assert report.reachable is False
        assert report.health_status == "unreachable"
        assert report.health_score is None
        assert report.unreachable_reason == "timeout"
        assert report.context_name == "ctx"
        assert report.categories == {}


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

    def test_fleet_score_average(self) -> None:
        healthy = build_cluster_report(_metrics(context_name="a"))
        report = aggregate_fleet([healthy])
        assert report.fleet_score == healthy.health_score
        assert report.fleet_status == "healthy"

    def test_fleet_score_average_multiple(self) -> None:
        # 2 clusters avec scores differents -> verifier la moyenne (pas la multiplication)
        c1 = build_cluster_report(_metrics(context_name="a"))
        c2 = build_cluster_report(_metrics(context_name="b", nodes_not_ready=1))
        report = aggregate_fleet([c1, c2])
        expected = round((c1.health_score + c2.health_score) / 2) if c2.health_score else 0
        assert report.fleet_score == expected

    def test_worst_status_critical_wins(self) -> None:
        d = build_cluster_report(_metrics(context_name="d", nodes_not_ready=2))
        c = build_cluster_report(_metrics(context_name="c", nodes_not_ready=5))
        report = aggregate_fleet([d, c])
        assert report.fleet_status == "critical"

    def test_status_order_healthy_degraded(self) -> None:
        a = build_cluster_report(_metrics(context_name="a"))
        b = build_cluster_report(_metrics(context_name="b", nodes_not_ready=2))
        report = aggregate_fleet([a, b])
        assert report.fleet_status == "degraded"

    def test_three_statuses_healthy_wins_critical_rank(self) -> None:
        h = build_cluster_report(_metrics(context_name="h"))
        d = build_cluster_report(_metrics(context_name="d", nodes_not_ready=2))
        c = build_cluster_report(_metrics(context_name="c", nodes_not_ready=5))
        report = aggregate_fleet([h, d, c])
        assert report.fleet_status == "critical"

    def test_cluster_reports_preserved(self) -> None:
        unreachable = make_unreachable_report("z", "timeout")
        report = aggregate_fleet([unreachable])
        assert report.cluster_reports == [unreachable]
        assert report.fleet_status == "no_cluster_reachable"


class TestHealthStatusBounds:
    def test_score_80_is_healthy(self) -> None:
        assert _health_status_from_score(80) == "healthy"

    def test_score_79_is_degraded(self) -> None:
        assert _health_status_from_score(79) == "degraded"

    def test_score_50_is_degraded(self) -> None:
        assert _health_status_from_score(50) == "degraded"

    def test_score_49_is_critical(self) -> None:
        assert _health_status_from_score(49) == "critical"


class TestCategoryFunctions:
    def test_node_category_ok(self) -> None:
        r = _node_category(_metrics())
        assert r.status == "OK"
        assert r.top_issue is None
        assert r.key_metric == "10/10 nodes ready"

    def test_node_category_warning(self) -> None:
        r = _node_category(_metrics(nodes_not_ready=1))
        assert r.status == "WARNING"
        assert r.top_issue == "1 node NotReady"
        assert r.key_metric == "9/10 nodes ready"

    def test_node_category_critical(self) -> None:
        r = _node_category(_metrics(nodes_not_ready=3))
        assert r.status == "CRITICAL"
        assert r.key_metric == "7/10 nodes ready"
        assert r.top_issue == "3 nodes NotReady"

    def test_pod_category_ok(self) -> None:
        r = _pod_category(_metrics(pods_crashloop=0))
        assert r.status == "OK"
        assert r.key_metric == "99/100 pods running, 0 CrashLoop"
        assert r.top_issue is None

    def test_pod_category_single_pod_no_crash(self) -> None:
        # pods_total=1 -> max(1,1)=1 vs max(1,2)=2 sous mutation
        r = _pod_category(_metrics(pods_total=1, pods_crashloop=0))
        assert r.status == "OK"
        assert r.key_metric == "99/1 pods running, 0 CrashLoop"

    def test_pod_category_single_pod_one_crash(self) -> None:
        # pods_total=1, pods_crashloop=1: ratio=1.0 (mutant max(total,2) donne 0.5)
        # 1.0 >= 0.15 -> CRITICAL ; 0.5 < 0.15 -> WARNING (mutant) -> diff detectee
        r = _pod_category(_metrics(pods_total=1, pods_crashloop=1, pods_running=0))
        assert r.status == "CRITICAL"
        assert r.top_issue == "1 CrashLoopBackOff pods"

    def test_pod_category_exact_warning_boundary(self) -> None:
        # crash_ratio vaut exactement 0.15 -> < 0.15 est FALSE (CRITICAL)
        r = _pod_category(_metrics(pods_crashloop=15, pods_total=100, pods_running=85))
        assert r.status == "CRITICAL"

    def test_pod_category_warning(self) -> None:
        r = _pod_category(_metrics(pods_crashloop=10, pods_total=100))
        assert r.status == "WARNING"
        assert r.key_metric == "99/100 pods running, 10 CrashLoop"
        assert r.top_issue == "10 CrashLoopBackOff pods"

    def test_pod_category_critical(self) -> None:
        r = _pod_category(_metrics(pods_crashloop=20, pods_total=100))
        assert r.status == "CRITICAL"
        assert r.key_metric == "99/100 pods running, 20 CrashLoop"
        assert r.top_issue == "20 CrashLoopBackOff pods"

    def test_cpu_category_unknown(self) -> None:
        r = _cpu_category(_metrics(cpu_utilization=None))
        assert r.status == "UNKNOWN"
        assert r.key_metric == "CPU usage unavailable"

    def test_cpu_category_critical(self) -> None:
        r = _cpu_category(_metrics(cpu_utilization=0.95))
        assert r.status == "CRITICAL"
        assert r.key_metric == "CPU 95% utilized"
        assert r.top_issue == "CPU pressure at 95%"

    def test_cpu_category_warning(self) -> None:
        r = _cpu_category(_metrics(cpu_utilization=0.85))
        assert r.status == "WARNING"
        assert r.key_metric == "CPU 85% utilized"
        assert r.top_issue == "CPU high at 85%"

    def test_cpu_category_ok(self) -> None:
        r = _cpu_category(_metrics(cpu_utilization=0.5))
        assert r.status == "OK"
        assert r.key_metric == "CPU 50% utilized"
        assert r.top_issue is None

    def test_cpu_category_exact_critical_boundary(self) -> None:
        # 0.90 n'est PAS > 0.90 -> warning; le mutant >= donnerait CRITICAL
        r = _cpu_category(_metrics(cpu_utilization=0.90))
        assert r.status == "WARNING"

    def test_cpu_category_exact_warning_boundary(self) -> None:
        # 0.80 n'est PAS > 0.80 -> OK; le mutant >= donnerait WARNING
        r = _cpu_category(_metrics(cpu_utilization=0.80))
        assert r.status == "OK"

    def test_cpu_category_top_issue_none_on_ok(self) -> None:
        r = _cpu_category(_metrics(cpu_utilization=0.5))
        assert r.key_metric == "CPU 50% utilized"

    def test_memory_category_unknown(self) -> None:
        r = _memory_category(_metrics(memory_utilization=None))
        assert r.status == "UNKNOWN"
        assert r.key_metric == "Memory usage unavailable"

    def test_memory_category_critical(self) -> None:
        r = _memory_category(_metrics(memory_utilization=0.95))
        assert r.status == "CRITICAL"
        assert r.key_metric == "Memory 95% utilized"
        assert r.top_issue == "Memory pressure at 95%"

    def test_memory_category_warning(self) -> None:
        r = _memory_category(_metrics(memory_utilization=0.85))
        assert r.status == "WARNING"
        assert r.key_metric == "Memory 85% utilized"
        assert r.top_issue == "Memory high at 85%"

    def test_memory_category_ok_key_metric(self) -> None:
        r = _memory_category(_metrics(memory_utilization=0.5))
        assert r.status == "OK"
        assert r.key_metric == "Memory 50% utilized"
        assert r.top_issue is None

    def test_memory_category_exact_critical_boundary(self) -> None:
        r = _memory_category(_metrics(memory_utilization=0.90))
        assert r.status == "WARNING"

    def test_memory_category_exact_warning_boundary(self) -> None:
        r = _memory_category(_metrics(memory_utilization=0.80))
        assert r.status == "OK"

    def test_cert_category_ok(self) -> None:
        r = _cert_category(_metrics())
        assert r.status == "OK"
        assert r.key_metric == "0 critical, 0 warning cert(s)"
        assert r.top_issue is None

    def test_cert_category_critical_boundary(self) -> None:
        # critical=1 et warning=0 -> warning=0, le mutant critical>1 donnerait OK
        r = _cert_category(_metrics(certs_expiring_critical=1))
        assert r.status == "CRITICAL"

    def test_cert_category_warning_boundary(self) -> None:
        # warning=1, critical=0 -> le mutant warning>1 donnerait OK
        r = _cert_category(_metrics(certs_expiring_warning=1))
        assert r.status == "WARNING"

    def test_cert_category_critical(self) -> None:
        r = _cert_category(_metrics(certs_expiring_critical=2))
        assert r.status == "CRITICAL"
        assert r.key_metric == "2 critical, 0 warning cert(s)"
        assert r.top_issue == "2 cert(s) expire within 7 days"

    def test_cert_category_warning(self) -> None:
        r = _cert_category(_metrics(certs_expiring_warning=3))
        assert r.status == "WARNING"
        assert r.key_metric == "0 critical, 3 warning cert(s)"
        assert r.top_issue == "3 cert(s) expire within 30 days"

    def test_pipeline_category_ok(self) -> None:
        r = _pipeline_category(_metrics())
        assert r.status == "OK"
        assert r.key_metric == "0 failing pipeline(s)"
        assert r.top_issue is None

    def test_pipeline_category_warning(self) -> None:
        r = _pipeline_category(_metrics(pipelines_failing=2))
        assert r.status == "WARNING"
        assert r.key_metric == "2 failing pipeline(s)"
        assert r.top_issue == "2 Tekton pipeline run(s) failed"

    def test_pipeline_category_critical(self) -> None:
        r = _pipeline_category(_metrics(pipelines_failing=3))
        assert r.status == "CRITICAL"
        assert r.key_metric == "3 failing pipeline(s)"
        assert r.top_issue == "3 Tekton pipeline run(s) failed"

    def test_security_category_ok(self) -> None:
        r = _security_category(_metrics())
        assert r.status == "OK"
        assert r.key_metric == "0 security violation(s)"
        assert r.top_issue is None

    def test_security_category_warning(self) -> None:
        r = _security_category(_metrics(security_violations=2))
        assert r.status == "WARNING"
        assert r.key_metric == "2 security violation(s)"
        assert r.top_issue == "2 privileged/non-compliant pod(s)"

    def test_security_category_critical(self) -> None:
        r = _security_category(_metrics(security_violations=3))
        assert r.status == "CRITICAL"
        assert r.key_metric == "3 security violation(s)"
        assert r.top_issue == "3 privileged/non-compliant pod(s)"


class TestBuildCategories:
    def test_contains_all_keys(self) -> None:
        cats = build_categories(_metrics())
        assert set(cats.keys()) == {
            "nodes",
            "pods",
            "cpu",
            "memory",
            "certificates",
            "pipelines",
            "security",
        }
        assert len(cats) == 7  # noqa: PLR2004


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

    def test_exact_boundary_negative_10pct(self) -> None:
        # delta = -10% exactement: < -10% est FALSE -> "stable"
        # (le mutant <= -10% donnerait "degrading")
        assert compute_fleet_trend(100.0, 90.0) == "stable"


class TestPercentIntRounding:
    def test_cpu_pct_int_fraction_not_rounded_up(self) -> None:
        # cpu 0.0199 -> int(0.0199*100) = 1 (mutant *101 -> 2)
        r = _cpu_category(_metrics(cpu_utilization=0.0199))
        assert r.key_metric == "CPU 1% utilized"

    def test_memory_pct_int_fraction_not_rounded_up(self) -> None:
        # mem 0.0199 -> int(0.0199*100) = 1 (mutant *101 -> 2)
        r = _memory_category(_metrics(memory_utilization=0.0199))
        assert r.key_metric == "Memory 1% utilized"


class TestWorstStatus:
    def test_unknown_statuses_empty(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status([]) == "unknown"

    def test_critical_present_wins(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["healthy", "critical", "degraded"]) == "critical"

    def test_critical_alone(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["critical"]) == "critical"

    def test_degraded_wins_over_healthy(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["healthy", "degraded"]) == "degraded"

    def test_degraded_alone(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["degraded"]) == "degraded"

    def test_all_healthy(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["healthy", "healthy"]) == "healthy"

    def test_healthy_alone(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["healthy"]) == "healthy"

    def test_unknown_status_only(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["weird"]) == "weird"

    def test_unknown_below_healthy(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["weird", "healthy"]) == "healthy"

    def test_unknown_below_critical(self) -> None:
        from hexawyn.domain.services.fleet_health.fleet_health_score_service import _worst_status

        assert _worst_status(["weird", "critical"]) == "critical"
