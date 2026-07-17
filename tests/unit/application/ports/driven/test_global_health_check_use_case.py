"""Unit tests for the global_health_check use case — domain logic + wiring."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driving.global_health_check.global_health_check_command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_service_port import (
    GlobalHealthCheckServicePort,
)
from hexawyn.application.service.global_health_check_service import (
    GlobalHealthCheckService,
    _compute_fleet_trend,
)
from hexawyn.application.use_case.global_health_check.global_health_check_use_case import (
    GlobalHealthCheckUseCase,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.fleet_health import ClusterRawMetrics
from hexawyn.domain.services.fleet_health.fleet_health_score_service import (
    aggregate_fleet,
    build_categories,
    build_cluster_report,
    compute_health_score,
    make_unreachable_report,
)

# ── helpers ───────────────────────────────────────────────────────────────


def _metrics(
    *,
    context_name: str = "ctx",
    nodes_total: int = 5,
    nodes_not_ready: int = 0,
    pods_total: int = 100,
    pods_running: int = 100,
    pods_crashloop: int = 0,
    cpu_utilization: float | None = 0.50,
    memory_utilization: float | None = 0.50,
    certs_expiring_critical: int = 0,
    certs_expiring_warning: int = 0,
    security_violations: int = 0,
    pipelines_failing: int = 0,
    prometheus_available: bool = True,
) -> ClusterRawMetrics:
    return ClusterRawMetrics(
        context_name=context_name,
        nodes_total=nodes_total,
        nodes_not_ready=nodes_not_ready,
        pods_total=pods_total,
        pods_running=pods_running,
        pods_crashloop=pods_crashloop,
        cpu_utilization=cpu_utilization,
        memory_utilization=memory_utilization,
        certs_expiring_critical=certs_expiring_critical,
        certs_expiring_warning=certs_expiring_warning,
        security_violations=security_violations,
        pipelines_failing=pipelines_failing,
        prometheus_available=prometheus_available,
    )


# ── Score formula ─────────────────────────────────────────────────────────


class TestComputeHealthScore:
    def test_healthy_cluster_score_100(self) -> None:
        m = _metrics()
        assert compute_health_score(m) == 100

    def test_prod_eu_from_test_data(self) -> None:
        """prod-eu: 3 crashloop / 120 total → crash_ratio=2.5% → -1pt; 1 cert critical → -10pt; expected ~76."""
        m = _metrics(
            context_name="prod-eu",
            nodes_total=5,
            nodes_not_ready=0,
            pods_total=120,
            pods_crashloop=3,
            cpu_utilization=0.72,
            memory_utilization=0.65,
            certs_expiring_critical=1,
        )
        assert compute_health_score(m) == 89

    def test_node_not_ready_deducts_20_each(self) -> None:
        m = _metrics(nodes_not_ready=2)
        assert compute_health_score(m) == 60

    def test_crash_ratio_40pts(self) -> None:
        """3 crashloop / 10 pods = 30% → deducts 12pts (int(0.30 * 40))."""
        m = _metrics(pods_total=10, pods_crashloop=3)
        score = compute_health_score(m)
        expected = 100 - int((3 / 10) * 40)
        assert score == expected

    def test_cpu_over_90_deducts_15(self) -> None:
        m = _metrics(cpu_utilization=0.95)
        assert compute_health_score(m) == 85

    def test_cpu_over_80_deducts_8(self) -> None:
        m = _metrics(cpu_utilization=0.85)
        assert compute_health_score(m) == 92

    def test_memory_over_90_deducts_15(self) -> None:
        m = _metrics(memory_utilization=0.91)
        assert compute_health_score(m) == 85

    def test_memory_over_80_deducts_8(self) -> None:
        m = _metrics(memory_utilization=0.82)
        assert compute_health_score(m) == 92

    def test_cert_critical_deducts_10(self) -> None:
        m = _metrics(certs_expiring_critical=1)
        assert compute_health_score(m) == 90

    def test_cert_warning_deducts_5(self) -> None:
        m = _metrics(certs_expiring_warning=2)
        assert compute_health_score(m) == 95

    def test_cert_critical_takes_precedence_over_warning(self) -> None:
        m = _metrics(certs_expiring_critical=1, certs_expiring_warning=3)
        assert compute_health_score(m) == 90

    def test_security_violations_capped_at_15(self) -> None:
        m = _metrics(security_violations=10)
        assert compute_health_score(m) == 85

    def test_security_3_violations_deducts_9(self) -> None:
        m = _metrics(security_violations=3)
        assert compute_health_score(m) == 91

    def test_score_floored_at_zero(self) -> None:
        m = _metrics(nodes_not_ready=10, pods_total=10, pods_crashloop=10, security_violations=10)
        assert compute_health_score(m) == 0

    def test_cpu_utilization_none_not_penalized(self) -> None:
        m = _metrics(cpu_utilization=None)
        assert compute_health_score(m) == 100

    def test_memory_utilization_none_not_penalized(self) -> None:
        m = _metrics(memory_utilization=None)
        assert compute_health_score(m) == 100

    def test_empty_cluster_score_100(self) -> None:
        """Empty cluster (no workloads) → score 100."""
        m = _metrics(
            nodes_total=0,
            pods_total=0,
            pods_running=0,
            pods_crashloop=0,
            cpu_utilization=None,
            memory_utilization=None,
        )
        assert compute_health_score(m) == 100

    def test_combined_degraded_scenario(self) -> None:
        """3 crashloop + 1 cert expiring in 5 days → score ~76."""
        m = _metrics(pods_total=10, pods_crashloop=3, certs_expiring_critical=1)
        crash_deduction = int((3 / 10) * 40)
        cert_deduction = 10
        assert compute_health_score(m) == 100 - crash_deduction - cert_deduction


# ── Category status ───────────────────────────────────────────────────────


class TestBuildCategories:
    def test_all_ok_when_healthy(self) -> None:
        cats = build_categories(_metrics())
        for name, cat in cats.items():
            assert cat.status == "OK", f"Expected OK for {name!r}, got {cat.status!r}"

    def test_node_warning_one_not_ready(self) -> None:
        cats = build_categories(_metrics(nodes_not_ready=1))
        assert cats["nodes"].status == "WARNING"

    def test_node_critical_two_not_ready(self) -> None:
        cats = build_categories(_metrics(nodes_not_ready=2))
        assert cats["nodes"].status == "CRITICAL"

    def test_pod_warning_low_crashloop(self) -> None:
        cats = build_categories(_metrics(pods_total=100, pods_crashloop=3))
        assert cats["pods"].status == "WARNING"

    def test_pod_critical_high_crashloop(self) -> None:
        cats = build_categories(_metrics(pods_total=10, pods_crashloop=2))
        assert cats["pods"].status == "CRITICAL"

    def test_cpu_unknown_when_none(self) -> None:
        cats = build_categories(_metrics(cpu_utilization=None))
        assert cats["cpu"].status == "UNKNOWN"

    def test_cpu_warning_above_80(self) -> None:
        cats = build_categories(_metrics(cpu_utilization=0.85))
        assert cats["cpu"].status == "WARNING"

    def test_cpu_critical_above_90(self) -> None:
        cats = build_categories(_metrics(cpu_utilization=0.95))
        assert cats["cpu"].status == "CRITICAL"

    def test_memory_unknown_when_none(self) -> None:
        cats = build_categories(_metrics(memory_utilization=None))
        assert cats["memory"].status == "UNKNOWN"

    def test_memory_warning_above_80(self) -> None:
        cats = build_categories(_metrics(memory_utilization=0.85))
        assert cats["memory"].status == "WARNING"

    def test_memory_critical_above_90(self) -> None:
        cats = build_categories(_metrics(memory_utilization=0.95))
        assert cats["memory"].status == "CRITICAL"

    def test_cert_critical(self) -> None:
        cats = build_categories(_metrics(certs_expiring_critical=1))
        assert cats["certificates"].status == "CRITICAL"

    def test_cert_warning(self) -> None:
        cats = build_categories(_metrics(certs_expiring_warning=1))
        assert cats["certificates"].status == "WARNING"

    def test_pipelines_ok_zero(self) -> None:
        cats = build_categories(_metrics(pipelines_failing=0))
        assert cats["pipelines"].status == "OK"

    def test_pipelines_warning_1(self) -> None:
        cats = build_categories(_metrics(pipelines_failing=1))
        assert cats["pipelines"].status == "WARNING"

    def test_pipelines_critical_3_plus(self) -> None:
        cats = build_categories(_metrics(pipelines_failing=3))
        assert cats["pipelines"].status == "CRITICAL"

    def test_security_warning(self) -> None:
        cats = build_categories(_metrics(security_violations=1))
        assert cats["security"].status == "WARNING"

    def test_security_critical(self) -> None:
        cats = build_categories(_metrics(security_violations=5))
        assert cats["security"].status == "CRITICAL"

    def test_prometheus_down_shows_unknown_cpu(self) -> None:
        """When Prometheus is down, cpu/memory utilization is None → UNKNOWN, not OK."""
        m = _metrics(cpu_utilization=None, memory_utilization=None, prometheus_available=False)
        cats = build_categories(m)
        assert cats["cpu"].status == "UNKNOWN"
        assert cats["memory"].status == "UNKNOWN"


# ── health_status from score ──────────────────────────────────────────────


class TestBuildClusterReport:
    def test_healthy_status_for_high_score(self) -> None:
        report = build_cluster_report(_metrics())
        assert report.health_status == "healthy"
        assert report.health_score == 100
        assert report.reachable is True
        assert report.unreachable_reason is None

    def test_degraded_status_for_mid_score(self) -> None:
        m = _metrics(nodes_not_ready=1, cpu_utilization=0.85)
        report = build_cluster_report(m)
        assert report.health_status == "degraded"

    def test_critical_status_for_low_score(self) -> None:
        m = _metrics(nodes_not_ready=3)
        report = build_cluster_report(m)
        assert report.health_status == "critical"

    def test_unreachable_report(self) -> None:
        report = make_unreachable_report("prod-eu", "connection_timeout")
        assert report.reachable is False
        assert report.health_score is None
        assert report.health_status == "unreachable"
        assert report.unreachable_reason == "connection_timeout"
        assert report.categories == {}


# ── Fleet aggregation ─────────────────────────────────────────────────────


class TestAggregateFleet:
    def test_fleet_score_avg_of_reachable(self) -> None:
        """Fleet of 3: 1 healthy (100), 1 degraded (60), 1 unreachable → avg=80."""
        r1 = build_cluster_report(_metrics(context_name="prod-eu"))
        r2 = build_cluster_report(_metrics(context_name="prod-us", nodes_not_ready=2))
        r3 = make_unreachable_report("staging-eu", "connection_timeout")
        fleet = aggregate_fleet([r1, r2, r3])
        assert fleet.reachable_count == 2
        assert fleet.unreachable_count == 1
        assert fleet.fleet_score == round((r1.health_score + r2.health_score) / 2)  # type: ignore[operator]

    def test_all_unreachable_fleet_score_none(self) -> None:
        r1 = make_unreachable_report("prod-eu", "timeout")
        fleet = aggregate_fleet([r1])
        assert fleet.fleet_score is None
        assert fleet.fleet_status == "no_cluster_reachable"

    def test_empty_report_list(self) -> None:
        fleet = aggregate_fleet([])
        assert fleet.fleet_score is None
        assert fleet.fleet_status == "unknown"

    def test_unreachable_not_included_in_aggregate(self) -> None:
        """Verify unreachable clusters are excluded from fleet score calculation."""
        healthy = build_cluster_report(_metrics(context_name="ok"))
        unreachable = make_unreachable_report("dead", "timeout")
        fleet = aggregate_fleet([healthy, unreachable])
        assert fleet.fleet_score == healthy.health_score

    def test_worst_status_propagates(self) -> None:
        r1 = build_cluster_report(_metrics(context_name="ok"))
        r2 = build_cluster_report(_metrics(context_name="bad", nodes_not_ready=4))
        fleet = aggregate_fleet([r1, r2])
        assert fleet.fleet_status == "critical"

    def test_prod_eu_prod_us_staging_scenario(self) -> None:
        """Acceptance test: 2 reachable, 1 unreachable → aggregate computed on 2."""
        prod_eu = build_cluster_report(
            _metrics(
                context_name="prod-eu",
                pods_total=120,
                pods_crashloop=3,
                certs_expiring_critical=1,
            )
        )
        prod_us = build_cluster_report(
            _metrics(
                context_name="prod-us",
                pods_total=80,
                pods_crashloop=0,
                cpu_utilization=0.45,
                memory_utilization=0.50,
            )
        )
        staging = make_unreachable_report("staging-eu", "connection_timeout")
        fleet = aggregate_fleet([prod_eu, prod_us, staging])
        assert fleet.reachable_count == 2
        assert fleet.unreachable_count == 1
        assert fleet.fleet_score is not None
        assert prod_us.health_score == 100
        expected = round((prod_eu.health_score + prod_us.health_score) / 2)  # type: ignore[operator]
        assert fleet.fleet_score == expected


# ── _compute_fleet_trend ──────────────────────────────────────────────────


class TestComputeFleetTrend:
    def test_improving(self) -> None:
        assert _compute_fleet_trend(70.0, 85.0) == "improving"

    def test_degrading(self) -> None:
        assert _compute_fleet_trend(85.0, 60.0) == "degrading"

    def test_stable(self) -> None:
        assert _compute_fleet_trend(80.0, 82.0) == "stable"

    def test_none_when_previous_none(self) -> None:
        assert _compute_fleet_trend(None, 80.0) is None

    def test_none_when_previous_zero(self) -> None:
        assert _compute_fleet_trend(0.0, 80.0) is None

    def test_none_when_current_none(self) -> None:
        assert _compute_fleet_trend(80.0, None) is None


# ── Use Case wiring ───────────────────────────────────────────────────────


class _StubServicePort(GlobalHealthCheckServicePort):
    def __init__(self, response: object) -> None:
        self._response = response

    def global_health_check(self, command: GlobalHealthCheckCommand) -> object:
        return self._response


class TestGlobalHealthCheckUseCase:
    def test_delegates_to_service(self) -> None:
        from hexawyn.application.ports.driving.global_health_check.global_health_check_response import (
            GlobalHealthCheckResponse,
        )
        from hexawyn.domain.models.fleet_health import FleetHealthReport

        expected = GlobalHealthCheckResponse(report=FleetHealthReport(fleet_score=95))
        svc = _StubServicePort(expected)
        use_case = GlobalHealthCheckUseCase(service=svc)
        cmd = GlobalHealthCheckCommand()
        result = use_case.execute(cmd)
        assert result is expected


# ── Application service ───────────────────────────────────────────────────


class _FakeFleetPort(FleetHealthPort):
    def __init__(self, contexts: list[str], metrics: dict[str, ClusterRawMetrics]) -> None:
        self._contexts = contexts
        self._metrics = metrics

    def list_contexts(self) -> list[str]:
        return self._contexts

    def get_cluster_raw_metrics(self, context_name: str) -> ClusterRawMetrics:
        if context_name not in self._metrics:
            raise ClusterUnreachableError(f"Unreachable: {context_name}", context={})
        return self._metrics[context_name]


class TestGlobalHealthCheckService:
    def test_healthy_fleet_single_cluster(self) -> None:
        m = _metrics(context_name="prod")
        port = _FakeFleetPort(["prod"], {"prod": m})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand())
        assert resp.report.reachable_count == 1
        assert resp.report.unreachable_count == 0
        assert resp.report.fleet_score == 100

    def test_unreachable_cluster_marked_not_failed(self) -> None:
        port = _FakeFleetPort(["dead"], {})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand())
        assert resp.report.unreachable_count == 1
        assert resp.report.fleet_status == "no_cluster_reachable"

    def test_mixed_fleet(self) -> None:
        """1 healthy + 1 unreachable → fleet computed on 1 reachable."""
        m = _metrics(context_name="ok")
        port = _FakeFleetPort(["ok", "dead"], {"ok": m})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand())
        assert resp.report.reachable_count == 1
        assert resp.report.unreachable_count == 1
        assert resp.report.fleet_score == 100

    def test_max_clusters_respected(self) -> None:
        ctxs = [f"ctx-{i}" for i in range(10)]
        metrics = {ctx: _metrics(context_name=ctx) for ctx in ctxs}
        port = _FakeFleetPort(ctxs, metrics)
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand(max_clusters=3))
        assert resp.report.reachable_count + resp.report.unreachable_count <= 3

    def test_trend_improving(self) -> None:
        m = _metrics(context_name="prod")
        port = _FakeFleetPort(["prod"], {"prod": m})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand(previous_fleet_score=70.0))
        assert resp.fleet_score_trend == "improving"

    def test_trend_degrading(self) -> None:
        m = _metrics(context_name="prod", nodes_not_ready=3)
        port = _FakeFleetPort(["prod"], {"prod": m})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand(previous_fleet_score=100.0))
        assert resp.fleet_score_trend == "degrading"

    def test_all_unreachable_fleet_score_none(self) -> None:
        port = _FakeFleetPort(["d1", "d2"], {})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand())
        assert resp.report.fleet_score is None
        assert resp.report.fleet_status == "no_cluster_reachable"

    def test_empty_context_list(self) -> None:
        port = _FakeFleetPort([], {})
        svc = GlobalHealthCheckService(port=port)
        resp = svc.global_health_check(GlobalHealthCheckCommand())
        assert resp.report.fleet_score is None
        assert resp.report.reachable_count == 0


# ── MCP tool ─────────────────────────────────────────────────────────────


class TestGlobalHealthCheckMCPTool:
    def test_tool_returns_expected_keys(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        fake_report = MagicMock()
        fake_report.cluster_reports = []
        fake_report.fleet_score = 95
        fake_report.fleet_status = "healthy"
        fake_report.reachable_count = 1
        fake_report.unreachable_count = 0
        from datetime import UTC, datetime

        fake_report.checked_at = datetime.now(UTC)

        fake_resp = MagicMock()
        fake_resp.report = fake_report
        fake_resp.fleet_score_trend = None

        with (
            patch("hexawyn.mcp.server.build_fleet_health_adapter"),
            patch("hexawyn.mcp.tools.global_health_check.GlobalHealthCheckUseCase") as mock_uc_cls,
        ):
            mock_uc_cls.return_value.execute.return_value = fake_resp
            result = global_health_check()

        assert "clusters" in result
        assert "fleet_score" in result
        assert "fleet_status" in result
        assert "reachable_count" in result
        assert "fleet_score_trend" in result
        assert result["error"] is None

    def test_tool_error_returns_error_key(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            side_effect=RuntimeError("boom"),
        ):
            result = global_health_check()

        assert result["error"] == "boom"
        assert result["fleet_score"] is None
        assert result["fleet_status"] == "error"

    def test_tool_serializes_cluster_reports(self) -> None:
        """Covers the cluster_reports serialization loop in the MCP tool."""
        from datetime import UTC, datetime

        from hexawyn.mcp.tools.global_health_check import global_health_check

        m = _metrics(context_name="prod-eu", nodes_not_ready=1)
        real_report = build_cluster_report(m)

        from hexawyn.domain.models.fleet_health import FleetHealthReport

        fleet_report = FleetHealthReport(
            cluster_reports=[real_report],
            fleet_score=80,
            fleet_status="degraded",
            reachable_count=1,
            unreachable_count=0,
            checked_at=datetime.now(UTC),
        )

        fake_resp = MagicMock()
        fake_resp.report = fleet_report
        fake_resp.fleet_score_trend = "stable"

        with (
            patch("hexawyn.mcp.server.build_fleet_health_adapter"),
            patch("hexawyn.mcp.tools.global_health_check.GlobalHealthCheckUseCase") as mock_uc_cls,
        ):
            mock_uc_cls.return_value.execute.return_value = fake_resp
            result = global_health_check()

        assert len(result["clusters"]) == 1  # type: ignore[arg-type]
        cluster = result["clusters"][0]  # type: ignore[index]
        assert cluster["context_name"] == "prod-eu"
        assert cluster["reachable"] is True
        assert "categories" in cluster
        assert result["fleet_score_trend"] == "stable"
        assert result["error"] is None


# ── Adapter pure helpers ──────────────────────────────────────────────────


class TestFleetHealthAdapterHelpers:
    def test_items_returns_list(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _items

        class FakeList:
            items = [1, 2, 3]

        assert _items(FakeList()) == [1, 2, 3]

    def test_items_returns_empty_on_missing_attr(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _items

        assert _items(object()) == []

    def test_node_ready_true(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _node_ready

        node = MagicMock()
        node.status.conditions = [MagicMock(type="Ready", status="True")]
        assert _node_ready(node) is True

    def test_node_ready_false(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _node_ready

        node = MagicMock()
        node.status.conditions = [MagicMock(type="Ready", status="False")]
        assert _node_ready(node) is False

    def test_node_ready_no_conditions(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _node_ready

        node = MagicMock()
        node.status.conditions = []
        assert _node_ready(node) is False

    def test_pod_is_crashloop_true(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _pod_is_crashloop

        pod = MagicMock()
        cs = MagicMock()
        cs.state.waiting.reason = "CrashLoopBackOff"
        pod.status.container_statuses = [cs]
        assert _pod_is_crashloop(pod) is True

    def test_pod_is_crashloop_false_running(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _pod_is_crashloop

        pod = MagicMock()
        cs = MagicMock()
        cs.state.waiting = None
        pod.status.container_statuses = [cs]
        assert _pod_is_crashloop(pod) is False

    def test_pod_phase(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _pod_phase

        pod = MagicMock()
        pod.status.phase = "Running"
        assert _pod_phase(pod) == "Running"

    def test_get_resource_utilization_no_url(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_resource_utilization

        cpu, mem = _get_resource_utilization("ctx", "")
        assert cpu is None
        assert mem is None

    def test_get_node_counts_happy_path(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_node_counts

        ready_node = MagicMock()
        ready_node.status.conditions = [MagicMock(type="Ready", status="True")]
        bad_node = MagicMock()
        bad_node.status.conditions = [MagicMock(type="Ready", status="False")]

        api = MagicMock()
        api.list_node.return_value = MagicMock(items=[ready_node, bad_node])
        total, not_ready = _get_node_counts(api)
        assert total == 2
        assert not_ready == 1

    def test_get_node_counts_api_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_node_counts

        api = MagicMock()
        api.list_node.side_effect = RuntimeError("connection refused")
        total, not_ready = _get_node_counts(api)
        assert total == 0
        assert not_ready == 0

    def test_get_pod_counts_happy_path(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_pod_counts

        running_pod = MagicMock()
        running_pod.status.phase = "Running"
        running_pod.status.container_statuses = []

        crash_pod = MagicMock()
        crash_pod.status.phase = "Running"
        cs = MagicMock()
        cs.state.waiting.reason = "CrashLoopBackOff"
        crash_pod.status.container_statuses = [cs]

        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = MagicMock(items=[running_pod, crash_pod])
        total, running, crashloop = _get_pod_counts(api)
        assert total == 2
        assert running == 2
        assert crashloop == 1

    def test_get_pod_counts_api_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_pod_counts

        api = MagicMock()
        api.list_pod_for_all_namespaces.side_effect = RuntimeError("boom")
        total, running, crash = _get_pod_counts(api)
        assert total == 0

    def test_get_security_violations_none(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_security_violations

        pod = MagicMock()
        container = MagicMock()
        container.security_context.privileged = False
        pod.spec.containers = [container]
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = MagicMock(items=[pod])
        assert _get_security_violations(api) == 0

    def test_get_security_violations_privileged(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_security_violations

        pod = MagicMock()
        container = MagicMock()
        container.security_context.privileged = True
        pod.spec.containers = [container]
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = MagicMock(items=[pod])
        assert _get_security_violations(api) == 1

    def test_get_security_violations_api_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_security_violations

        api = MagicMock()
        api.list_pod_for_all_namespaces.side_effect = RuntimeError("boom")
        assert _get_security_violations(api) == 0

    def test_get_failing_pipelines_none(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_failing_pipelines

        crd = MagicMock()
        crd.list_cluster_custom_object.return_value = {"items": []}
        assert _get_failing_pipelines(crd) == 0

    def test_get_failing_pipelines_one_failed(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_failing_pipelines

        item = {"status": {"conditions": [{"type": "Succeeded", "status": "False"}]}}
        crd = MagicMock()
        crd.list_cluster_custom_object.return_value = {"items": [item]}
        assert _get_failing_pipelines(crd) == 1

    def test_get_failing_pipelines_api_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_failing_pipelines

        crd = MagicMock()
        crd.list_cluster_custom_object.side_effect = RuntimeError("tekton not installed")
        assert _get_failing_pipelines(crd) == 0

    def test_get_cert_counts_api_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_cert_counts

        api = MagicMock()
        api.list_secret_for_all_namespaces.side_effect = RuntimeError("forbidden")
        critical, warning = _get_cert_counts(api)
        assert critical == 0
        assert warning == 0

    def test_get_cert_counts_no_tls_secrets(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_cert_counts

        secret = MagicMock()
        secret.type = "Opaque"
        api = MagicMock()
        api.list_secret_for_all_namespaces.return_value = MagicMock(items=[secret])
        critical, warning = _get_cert_counts(api)
        assert critical == 0
        assert warning == 0

    def test_list_contexts(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter.list_available_contexts",
            return_value=[{"name": "prod-eu"}, {"name": "prod-us"}],
        ):
            adapter = FleetHealthAdapter()
            ctxs = adapter.list_contexts()
        assert ctxs == ["prod-eu", "prod-us"]

    def test_get_cluster_raw_metrics_unreachable(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig",
            side_effect=RuntimeError("bad cert"),
        ):
            adapter = FleetHealthAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_cluster_raw_metrics("dead-ctx")

    def test_get_cluster_raw_metrics_validate_fails(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        with (
            patch("hexawyn.adapters.secondary.fleet_health_adapter.load_kubeconfig"),
            patch(
                "hexawyn.adapters.secondary.fleet_health_adapter.validate_connection",
                return_value={"status": "unreachable", "error": "timeout"},
            ),
        ):
            adapter = FleetHealthAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_cluster_raw_metrics("prod-eu")

    def test_get_cluster_raw_metrics_happy_path(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

        _mod = "hexawyn.adapters.secondary.fleet_health_adapter"
        with (
            patch(f"{_mod}.load_kubeconfig", return_value=MagicMock()),
            patch(f"{_mod}.validate_connection", return_value={"status": "connected"}),
            patch(f"{_mod}._get_node_counts", return_value=(5, 0)),
            patch(f"{_mod}._get_pod_counts", return_value=(100, 98, 2)),
            patch(f"{_mod}._get_resource_utilization", return_value=(0.60, 0.55)),
            patch(f"{_mod}._get_cert_counts", return_value=(0, 1)),
            patch(f"{_mod}._get_security_violations", return_value=0),
            patch(f"{_mod}._get_failing_pipelines", return_value=0),
            patch("kubernetes.client.CustomObjectsApi"),
        ):
            adapter = FleetHealthAdapter(prometheus_url="http://prom:9090")
            metrics = adapter.get_cluster_raw_metrics("prod-eu")

        assert metrics.context_name == "prod-eu"
        assert metrics.nodes_total == 5
        assert metrics.pods_total == 100
        assert metrics.cpu_utilization == 0.60
        assert metrics.certs_expiring_warning == 1

    def test_get_resource_utilization_with_prometheus(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_resource_utilization

        mock_resp = MagicMock()
        mock_resp.json.return_value = {"data": {"result": [{"value": [0, "0.72"]}]}}
        mock_resp.raise_for_status.return_value = None

        with patch("requests.get", return_value=mock_resp):
            cpu, mem = _get_resource_utilization("ctx", "http://prometheus:9090")

        assert cpu == 0.72
        assert mem == 0.72

    def test_get_resource_utilization_prometheus_error(self) -> None:
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_resource_utilization

        with patch("requests.get", side_effect=RuntimeError("connection refused")):
            cpu, mem = _get_resource_utilization("ctx", "http://prometheus:9090")

        assert cpu is None
        assert mem is None

    def test_get_cert_counts_tls_secret_invalid_data(self) -> None:
        """TLS secret with invalid base64/cert data is skipped gracefully."""
        from hexawyn.adapters.secondary.fleet_health_adapter import _get_cert_counts

        secret = MagicMock()
        secret.type = "kubernetes.io/tls"
        secret.data = {"tls.crt": "not-valid-base64!!"}
        api = MagicMock()
        api.list_secret_for_all_namespaces.return_value = MagicMock(items=[secret])
        critical, warning = _get_cert_counts(api)
        assert critical == 0
        assert warning == 0


# ── TimeoutError branch in service ───────────────────────────────────────


class TestGlobalHealthCheckServiceTimeout:
    def test_timeout_marks_pending_as_unreachable(self) -> None:
        """When iterating as_completed raises TimeoutError, futures not done → unreachable."""
        from hexawyn.application.service.global_health_check_service import GlobalHealthCheckService

        port = _FakeFleetPort(["slow1", "slow2"], {})

        def _timeout_iterator(*_args: object, **_kwargs: object) -> object:
            raise TimeoutError("fleet timeout")
            yield  # make it a generator

        with patch(
            "hexawyn.application.service.global_health_check_service.as_completed",
            side_effect=_timeout_iterator,
        ):
            svc = GlobalHealthCheckService(port=port)
            resp = svc.global_health_check(GlobalHealthCheckCommand(timeout_seconds=0.01))

        assert resp.report.fleet_status == "no_cluster_reachable"
