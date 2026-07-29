from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.use_case.cluster.global_health_check.command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.use_case.cluster.global_health_check.global_health_check_use_case import (
    GlobalHealthCheckUseCase,
    _compute_fleet_trend,
)
from hexawyn.application.use_case.cluster.global_health_check.response import (
    GlobalHealthCheckResponse,
)
from hexawyn.domain.models.fleet_health import (
    ClusterRawMetrics,
    FleetHealthReport,
)


def _make_raw_metrics(  # noqa: PLR0913
    context_name: str = "test-cluster",
    nodes_total: int = 3,
    nodes_not_ready: int = 0,
    pods_total: int = 20,
    pods_running: int = 20,
    pods_crashloop: int = 0,
    cpu_utilization: float | None = 0.5,
    memory_utilization: float | None = 0.5,
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


class TestGlobalHealthCheckUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics()

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert isinstance(result, GlobalHealthCheckResponse)
        assert isinstance(result.report, FleetHealthReport)

    def test_execute_with_no_contexts(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = []

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert isinstance(result.report, FleetHealthReport)
        assert len(result.report.cluster_reports) == 0  # noqa: PLR2004

    def test_execute_multiple_clusters(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a", "ctx-b", "ctx-c"]
        port.get_cluster_raw_metrics.side_effect = [
            _make_raw_metrics("ctx-a"),
            _make_raw_metrics("ctx-b"),
            _make_raw_metrics("ctx-c"),
        ]

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert len(result.report.cluster_reports) == 3  # noqa: PLR2004
        assert result.report.reachable_count == 3  # noqa: PLR2004
        assert result.report.unreachable_count == 0  # noqa: PLR2004

    def test_execute_max_clusters_limit(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a", "ctx-b", "ctx-c", "ctx-d", "ctx-e"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics()

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=2))

        assert len(result.report.cluster_reports) == 2  # noqa: PLR2004

    def test_execute_cluster_unreachable(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.side_effect = RuntimeError("connection refused")

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert len(result.report.cluster_reports) == 1  # noqa: PLR2004
        assert result.report.cluster_reports[0].reachable is False
        assert result.report.cluster_reports[0].health_status == "unreachable"
        assert result.report.unreachable_count == 1  # noqa: PLR2004

    def test_execute_healthy_cluster_score_100(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["healthy-cluster"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            context_name="healthy-cluster",
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        report = result.report.cluster_reports[0]
        assert report.health_score == 100  # noqa: PLR2004
        assert report.health_status == "healthy"

    def test_execute_critical_cluster(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["critical-cluster"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            context_name="critical-cluster",
            nodes_not_ready=2,
            pods_crashloop=10,
            pods_total=20,
            cpu_utilization=0.95,
            memory_utilization=0.95,
            security_violations=5,
            certs_expiring_critical=3,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        report = result.report.cluster_reports[0]
        assert report.health_status == "critical"
        assert report.health_score is not None
        assert report.health_score < 50  # noqa: PLR2004

    def test_execute_with_previous_fleet_score_improving_trend(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics()

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(
            GlobalHealthCheckCommand(max_clusters=10, previous_fleet_score=60.0)
        )

        assert result.fleet_score_trend == "improving"

    def test_execute_with_previous_fleet_score_degrading_trend(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            nodes_not_ready=2,
            pods_crashloop=5,
            pods_total=20,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(
            GlobalHealthCheckCommand(max_clusters=10, previous_fleet_score=100.0)
        )

        assert result.fleet_score_trend == "degrading"

    def test_execute_with_previous_fleet_score_stable_trend(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics()

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(
            GlobalHealthCheckCommand(max_clusters=10, previous_fleet_score=99.0)
        )

        assert result.fleet_score_trend == "stable"

    def test_execute_mixed_reachable_unreachable(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ok", "down"]
        port.get_cluster_raw_metrics.side_effect = [
            _make_raw_metrics("ok"),
            RuntimeError("timeout"),
        ]

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert result.report.reachable_count == 1  # noqa: PLR2004
        assert result.report.unreachable_count == 1  # noqa: PLR2004
        assert result.report.fleet_score is not None

    def test_execute_all_unreachable(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["down-a", "down-b"]
        port.get_cluster_raw_metrics.side_effect = RuntimeError("all down")

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        assert result.report.reachable_count == 0  # noqa: PLR2004
        assert result.report.unreachable_count == 2  # noqa: PLR2004
        assert result.report.fleet_status == "no_cluster_reachable"

    def test_execute_with_null_metrics(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            cpu_utilization=None,
            memory_utilization=None,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        report = result.report.cluster_reports[0]
        assert report.categories["cpu"].status == "UNKNOWN"
        assert report.categories["memory"].status == "UNKNOWN"

    def test_execute_high_cpu_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            cpu_utilization=0.95,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        cpu_cat = result.report.cluster_reports[0].categories["cpu"]
        assert cpu_cat.status == "CRITICAL"

    def test_execute_high_memory_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            memory_utilization=0.85,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        mem_cat = result.report.cluster_reports[0].categories["memory"]
        assert mem_cat.status == "WARNING"

    def test_execute_with_cert_expiry_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            certs_expiring_critical=2,
            certs_expiring_warning=0,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        cert_cat = result.report.cluster_reports[0].categories["certificates"]
        assert cert_cat.status == "CRITICAL"

    def test_execute_with_cert_expiry_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            certs_expiring_warning=1,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        cert_cat = result.report.cluster_reports[0].categories["certificates"]
        assert cert_cat.status == "WARNING"

    def test_execute_with_pipeline_failures_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            pipelines_failing=3,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        pipe_cat = result.report.cluster_reports[0].categories["pipelines"]
        assert pipe_cat.status == "CRITICAL"

    def test_execute_with_pipeline_failures_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            pipelines_failing=1,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        pipe_cat = result.report.cluster_reports[0].categories["pipelines"]
        assert pipe_cat.status == "WARNING"

    def test_execute_with_security_violations_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            security_violations=5,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        sec_cat = result.report.cluster_reports[0].categories["security"]
        assert sec_cat.status == "CRITICAL"

    def test_execute_with_security_violations_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            security_violations=1,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        sec_cat = result.report.cluster_reports[0].categories["security"]
        assert sec_cat.status == "WARNING"

    def test_execute_with_nodes_not_ready_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            nodes_not_ready=1,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        node_cat = result.report.cluster_reports[0].categories["nodes"]
        assert node_cat.status == "WARNING"

    def test_execute_with_nodes_not_ready_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            nodes_not_ready=2,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        node_cat = result.report.cluster_reports[0].categories["nodes"]
        assert node_cat.status == "CRITICAL"

    def test_execute_with_crashloop_pods_warning(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            pods_total=10,
            pods_crashloop=1,
            pods_running=9,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        pod_cat = result.report.cluster_reports[0].categories["pods"]
        assert pod_cat.status == "WARNING"

    def test_execute_with_crashloop_pods_critical(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            pods_total=10,
            pods_crashloop=2,
            pods_running=8,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        pod_cat = result.report.cluster_reports[0].categories["pods"]
        assert pod_cat.status == "CRITICAL"

    def test_execute_degraded_cluster(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["degraded"]
        port.get_cluster_raw_metrics.return_value = _make_raw_metrics(
            context_name="degraded",
            nodes_not_ready=1,
            memory_utilization=0.85,
        )

        use_case = GlobalHealthCheckUseCase(port=port)
        result = use_case.execute(GlobalHealthCheckCommand(max_clusters=10))

        report = result.report.cluster_reports[0]
        assert report.health_status == "degraded"
        assert report.health_score is not None
        assert 50 <= report.health_score < 80  # noqa: PLR2004

    def test_execute_timeout_path(self) -> None:
        port = MagicMock()
        port.list_contexts.return_value = ["ctx-a", "ctx-b"]

        def _timeout_generator():
            raise TimeoutError("timed out")
            yield  # type: ignore

        use_case = GlobalHealthCheckUseCase(port=port)

        with patch(
            "hexawyn.application.use_case.cluster.global_health_check.global_health_check_use_case.as_completed",
            return_value=_timeout_generator(),
        ):
            result = use_case.execute(
                GlobalHealthCheckCommand(max_clusters=10, timeout_seconds=1.0)
            )

        assert isinstance(result, GlobalHealthCheckResponse)


class TestComputeFleetTrend:
    def test_improving_trend(self) -> None:
        assert _compute_fleet_trend(60.0, 90.0) == "improving"

    def test_degrading_trend(self) -> None:
        assert _compute_fleet_trend(100.0, 80.0) == "degrading"

    def test_stable_trend(self) -> None:
        assert _compute_fleet_trend(80.0, 82.0) == "stable"

    def test_no_previous_score_is_none(self) -> None:
        assert _compute_fleet_trend(None, 90.0) is None

    def test_no_current_score_is_none(self) -> None:
        assert _compute_fleet_trend(80.0, None) is None

    def test_zero_previous_score_is_none(self) -> None:
        assert _compute_fleet_trend(0, 90.0) is None
