"""Unit tests for check_resource_constraints use case — TDD Red phase."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.pod_resource_metrics_port import (
    ContainerMetricsRecord,
    PodResourceMetricsPort,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_response import (
    CheckResourceConstraintsResponse,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_service_port import (
    CheckResourceConstraintsServicePort,
)
from hexawyn.application.service.resource_constraint_service import (
    ResourceConstraintService,
    _classify_container,
    _sort_key,
)
from hexawyn.application.use_case.check_resource_constraints.check_resource_constraints_use_case import (
    CheckResourceConstraintsUseCase,
)
from hexawyn.domain.errors import InsufficientPermissionsError, MetricsUnavailableError
from hexawyn.domain.models.resource_constraint import (
    ResourceConstraintReport,
    RiskLevel,
)

# ── Stub port ─────────────────────────────────────────────────────────────


class _StubPodResourceMetricsPort(PodResourceMetricsPort):
    def __init__(
        self,
        records: list[ContainerMetricsRecord],
        raise_exc: Exception | None = None,
    ) -> None:
        self._records = records
        self._raise_exc = raise_exc

    def list_container_resources(self, namespace: str) -> list[ContainerMetricsRecord]:
        if self._raise_exc is not None:
            raise self._raise_exc
        return self._records


# ── Helpers ────────────────────────────────────────────────────────────────

_MiB = 1024 * 1024
_GiB = 1024 * _MiB


def _container(
    container_name: str = "app",
    pod_name: str = "pod-1",
    namespace: str = "production",
    cpu_usage_millicores: int = 100,
    cpu_limit_millicores: int | None = 500,
    memory_usage_bytes: int = 200 * _MiB,
    memory_limit_bytes: int | None = 512 * _MiB,
    is_init_container: bool = False,
) -> ContainerMetricsRecord:
    return ContainerMetricsRecord(
        container_name=container_name,
        pod_name=pod_name,
        namespace=namespace,
        cpu_usage_millicores=cpu_usage_millicores,
        cpu_limit_millicores=cpu_limit_millicores,
        memory_usage_bytes=memory_usage_bytes,
        memory_limit_bytes=memory_limit_bytes,
        is_init_container=is_init_container,
    )


def _make_service(
    records: list[ContainerMetricsRecord],
    raise_exc: Exception | None = None,
) -> ResourceConstraintService:
    port = _StubPodResourceMetricsPort(records, raise_exc)
    return ResourceConstraintService(port=port)


# ── Tests: _classify_container ─────────────────────────────────────────────


class TestClassifyContainer:
    def test_cpu_critical_above_threshold(self) -> None:
        record = _container(
            cpu_usage_millicores=480,
            cpu_limit_millicores=500,  # 96%
            memory_usage_bytes=200 * _MiB,
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "throttled" in entry.tags
        assert entry.cpu_pct is not None
        assert entry.cpu_pct == pytest.approx(96.0)

    def test_memory_critical_above_threshold(self) -> None:
        record = _container(
            cpu_usage_millicores=100,
            cpu_limit_millicores=500,  # 20%
            memory_usage_bytes=471 * _MiB,
            memory_limit_bytes=512 * _MiB,  # 91.99%
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "oomkill_risk" in entry.tags
        assert "throttled" not in entry.tags

    def test_both_cpu_and_memory_critical(self) -> None:
        record = _container(
            cpu_usage_millicores=450,  # 90%
            cpu_limit_millicores=500,
            memory_usage_bytes=450 * _MiB,  # 87.9%
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "throttled" in entry.tags
        assert "oomkill_risk" in entry.tags

    def test_ok_below_both_thresholds(self) -> None:
        # TC2: 45% CPU, 50% memory → OK
        record = _container(
            cpu_usage_millicores=225,  # 45%
            cpu_limit_millicores=500,
            memory_usage_bytes=256 * _MiB,  # 50%
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.OK
        assert entry.tags == []

    def test_no_cpu_limit_returns_no_limits(self) -> None:
        # TC3: no resource limits
        record = _container(cpu_limit_millicores=None, memory_limit_bytes=None)
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.NO_LIMITS
        assert "no_limits" in entry.tags
        assert entry.cpu_pct is None
        assert entry.memory_pct is None

    def test_cpu_limit_zero_treated_as_unlimited(self) -> None:
        # Edge case: CPU limit = 0 → unlimited, no CPU risk
        record = _container(
            cpu_usage_millicores=9999,
            cpu_limit_millicores=0,  # explicitly unlimited
            memory_usage_bytes=200 * _MiB,
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.cpu_pct is None
        assert "cpu_unlimited" in entry.tags

    def test_cpu_unlimited_but_memory_critical_stays_critical(self) -> None:
        record = _container(
            cpu_usage_millicores=9999,
            cpu_limit_millicores=0,  # unlimited
            memory_usage_bytes=450 * _MiB,  # 87.9% → CRITICAL
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "oomkill_risk" in entry.tags
        assert "cpu_unlimited" in entry.tags

    def test_memory_limit_zero_treated_as_unlimited(self) -> None:
        # Edge case: memory limit = 0 → unlimited, no memory risk, stays OK
        record = _container(
            cpu_usage_millicores=100,
            cpu_limit_millicores=500,
            memory_usage_bytes=999 * _MiB,
            memory_limit_bytes=0,  # explicitly unlimited
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.memory_pct is None
        assert "memory_unlimited" in entry.tags
        assert entry.risk_level == RiskLevel.OK

    def test_init_container_flag_propagated(self) -> None:
        record = _container(is_init_container=True)
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.is_init_container is True
        assert "init_container" in entry.tags

    def test_init_container_at_risk_flagged_critical(self) -> None:
        record = _container(
            cpu_usage_millicores=480,
            cpu_limit_millicores=500,
            is_init_container=True,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "init_container" in entry.tags
        assert "throttled" in entry.tags

    def test_custom_thresholds_respected(self) -> None:
        record = _container(
            cpu_usage_millicores=750,  # 75%
            cpu_limit_millicores=1000,
            memory_usage_bytes=80 * _MiB,  # 80%
            memory_limit_bytes=100 * _MiB,
        )
        # With 70% CPU threshold, 75% CPU is CRITICAL
        entry_strict = _classify_container(record, cpu_thr=70.0, mem_thr=85.0)
        assert entry_strict.risk_level == RiskLevel.CRITICAL

        # With 80% CPU threshold, 75% CPU is OK
        entry_loose = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry_loose.risk_level == RiskLevel.OK

    def test_at_exact_cpu_threshold_is_not_critical(self) -> None:
        record = _container(
            cpu_usage_millicores=400,  # exactly 80%
            cpu_limit_millicores=500,
            memory_usage_bytes=200 * _MiB,
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.OK

    def test_just_above_cpu_threshold_is_critical(self) -> None:
        record = _container(
            cpu_usage_millicores=401,  # 80.2%
            cpu_limit_millicores=500,
            memory_usage_bytes=200 * _MiB,
            memory_limit_bytes=512 * _MiB,
        )
        entry = _classify_container(record, cpu_thr=80.0, mem_thr=85.0)
        assert entry.risk_level == RiskLevel.CRITICAL


# ── Tests: _sort_key ──────────────────────────────────────────────────────


class TestSortKey:
    def test_critical_sorts_before_no_limits(self) -> None:
        assert _sort_key(RiskLevel.CRITICAL) < _sort_key(RiskLevel.NO_LIMITS)

    def test_no_limits_sorts_before_ok(self) -> None:
        assert _sort_key(RiskLevel.NO_LIMITS) < _sort_key(RiskLevel.OK)


# ── Tests: ResourceConstraintService ──────────────────────────────────────


class TestResourceConstraintService:
    def test_tc1_memory_critical_oomkill_risk(self) -> None:
        # TC1: Pod at 92% memory limit → CRITICAL OOMKill risk
        records = [
            _container(
                pod_name="risky-app",
                memory_usage_bytes=471 * _MiB,  # 91.99% of 512Mi
                memory_limit_bytes=512 * _MiB,
                cpu_usage_millicores=100,
                cpu_limit_millicores=500,
            )
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.critical_count == 1
        critical = [c for c in report.containers if c.risk_level == RiskLevel.CRITICAL]
        assert len(critical) == 1
        assert "oomkill_risk" in critical[0].tags

    def test_tc2_ok_pod_not_at_risk(self) -> None:
        # TC2: Pod at 45% CPU, 50% memory → OK
        records = [
            _container(
                pod_name="auth-service",
                cpu_usage_millicores=225,
                cpu_limit_millicores=500,
                memory_usage_bytes=256 * _MiB,
                memory_limit_bytes=512 * _MiB,
            )
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.critical_count == 0
        assert report.ok_count == 1
        assert report.containers[0].risk_level == RiskLevel.OK

    def test_tc3_no_limits_flagged_as_warning(self) -> None:
        # TC3: Pod with no resource limits → NO_LIMITS
        records = [
            _container(
                pod_name="unconfigured-svc",
                cpu_limit_millicores=None,
                memory_limit_bytes=None,
            )
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.no_limits_count == 1
        assert report.critical_count == 0
        entry = report.containers[0]
        assert entry.risk_level == RiskLevel.NO_LIMITS
        assert "no_limits" in entry.tags

    def test_tc4_all_healthy_clean_report(self) -> None:
        # TC4: All pods healthy
        records = [
            _container(pod_name=f"svc-{i}", cpu_usage_millicores=100, cpu_limit_millicores=500)
            for i in range(5)
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.critical_count == 0
        assert report.no_limits_count == 0
        assert report.ok_count == 5
        assert all(c.risk_level == RiskLevel.OK for c in report.containers)

    def test_mixed_risks_sorted_critical_first(self) -> None:
        records = [
            _container(
                pod_name="ok-svc",
                cpu_usage_millicores=100,
                cpu_limit_millicores=500,
                memory_usage_bytes=200 * _MiB,
                memory_limit_bytes=512 * _MiB,
            ),
            _container(
                pod_name="critical-svc",
                cpu_usage_millicores=480,
                cpu_limit_millicores=500,
                memory_usage_bytes=200 * _MiB,
                memory_limit_bytes=512 * _MiB,
            ),
            _container(
                pod_name="no-limits-svc",
                cpu_limit_millicores=None,
                memory_limit_bytes=None,
            ),
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.containers[0].risk_level == RiskLevel.CRITICAL
        assert report.containers[1].risk_level == RiskLevel.NO_LIMITS
        assert report.containers[2].risk_level == RiskLevel.OK

    def test_payment_api_test_data(self) -> None:
        # Test data from task: payment-api CPU 480m/500m (96%), memory 400Mi/512Mi (78%)
        records = [
            _container(
                pod_name="payment-api",
                container_name="payment-api",
                cpu_usage_millicores=480,
                cpu_limit_millicores=500,
                memory_usage_bytes=400 * _MiB,
                memory_limit_bytes=512 * _MiB,
            ),
            _container(
                pod_name="auth-service",
                container_name="auth-service",
                cpu_usage_millicores=100,
                cpu_limit_millicores=500,
                memory_usage_bytes=200 * _MiB,
                memory_limit_bytes=512 * _MiB,
            ),
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        # payment-api: CPU 96% > 80% → CRITICAL
        # auth-service: CPU 20%, memory 39% → OK
        assert report.critical_count == 1
        assert report.ok_count == 1
        critical = [c for c in report.containers if c.pod_name == "payment-api"]
        assert len(critical) == 1
        assert critical[0].risk_level == RiskLevel.CRITICAL
        assert "throttled" in critical[0].tags
        assert critical[0].cpu_pct == pytest.approx(96.0)
        # memory 78% < 85% → not oomkill_risk
        assert "oomkill_risk" not in critical[0].tags

    def test_empty_namespace_returns_empty_report(self) -> None:
        service = _make_service([])
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="empty-ns")
        )
        report = response.report
        assert report.total_containers == 0
        assert report.critical_count == 0
        assert report.containers == []

    def test_rbac_error_propagates(self) -> None:
        service = _make_service([], raise_exc=InsufficientPermissionsError("RBAC denied"))
        with pytest.raises(InsufficientPermissionsError):
            service.check_resource_constraints(
                CheckResourceConstraintsCommand(namespace="production")
            )

    def test_metrics_unavailable_propagates(self) -> None:
        service = _make_service(
            [], raise_exc=MetricsUnavailableError("metrics-server not installed")
        )
        with pytest.raises(MetricsUnavailableError):
            service.check_resource_constraints(
                CheckResourceConstraintsCommand(namespace="production")
            )

    def test_total_pods_scanned_counted(self) -> None:
        records = [
            _container(pod_name="pod-a", container_name="c1"),
            _container(pod_name="pod-a", container_name="c2"),
            _container(pod_name="pod-b", container_name="app"),
        ]
        service = _make_service(records)
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        report = response.report
        assert report.total_containers == 3
        # Two distinct pod names
        assert report.total_pods_scanned == 2

    def test_generated_at_is_recent(self) -> None:
        service = _make_service([])
        response = service.check_resource_constraints(
            CheckResourceConstraintsCommand(namespace="production")
        )
        diff = (datetime.now(UTC) - response.report.generated_at).total_seconds()
        assert abs(diff) < 5


# ── Tests: CheckResourceConstraintsUseCase ────────────────────────────────


class TestCheckResourceConstraintsUseCase:
    def test_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckResourceConstraintsServicePort)
        mock_service.check_resource_constraints.return_value = CheckResourceConstraintsResponse(
            report=ResourceConstraintReport(
                namespace="production",
                total_pods_scanned=1,
                total_containers=1,
            )
        )
        use_case = CheckResourceConstraintsUseCase(service=mock_service)
        command = CheckResourceConstraintsCommand(namespace="production")
        response = use_case.execute(command)
        mock_service.check_resource_constraints.assert_called_once_with(command)
        assert isinstance(response, CheckResourceConstraintsResponse)

    def test_use_case_returns_response_report(self) -> None:
        records = [_container()]
        port = _StubPodResourceMetricsPort(records)
        service = ResourceConstraintService(port=port)
        use_case = CheckResourceConstraintsUseCase(service=service)
        response = use_case.execute(CheckResourceConstraintsCommand(namespace="production"))
        assert isinstance(response.report, ResourceConstraintReport)


# ── Tests: MCP Tool ───────────────────────────────────────────────────────


class TestCheckResourceConstraintsMCPTool:
    def test_happy_path_returns_expected_keys(self) -> None:
        from hexawyn.mcp.tools.check_resource_constraints import check_resource_constraints

        records = [
            _container(
                pod_name="payment-api",
                cpu_usage_millicores=480,
                cpu_limit_millicores=500,
                memory_usage_bytes=400 * _MiB,
                memory_limit_bytes=512 * _MiB,
            )
        ]

        def _fake_build_adapter() -> PodResourceMetricsPort:
            return _StubPodResourceMetricsPort(records)

        with patch(
            "hexawyn.mcp.tools.check_resource_constraints._build_adapter",
            side_effect=_fake_build_adapter,
        ):
            result = check_resource_constraints(namespace="production")

        assert result["namespace"] == "production"
        assert result["total_containers"] == 1
        assert result["critical_count"] == 1
        assert result["error"] is None
        assert isinstance(result["containers"], list)

    def test_error_returns_error_key(self) -> None:
        from hexawyn.mcp.tools.check_resource_constraints import check_resource_constraints

        def _fail() -> PodResourceMetricsPort:
            raise MetricsUnavailableError("metrics-server not installed")

        with patch(
            "hexawyn.mcp.tools.check_resource_constraints._build_adapter",
            side_effect=_fail,
        ):
            result = check_resource_constraints(namespace="production")

        assert result["error"] is not None
        assert "metrics-server" in result["error"]
        assert result["total_containers"] == 0

    def test_register_adds_tool_to_mcp(self) -> None:
        from hexawyn.mcp.tools.check_resource_constraints import register

        mock_mcp = MagicMock()
        register(mock_mcp)
        mock_mcp.tool.assert_called_once()


# ── Tests: KubernetesPodResourceAdapter ───────────────────────────────────


class TestKubernetesPodResourceAdapter:
    def _make_adapter(self, mock_core_api: object, mock_custom_api: object) -> object:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        adapter = KubernetesPodResourceAdapter()
        return adapter

    def test_list_container_resources_happy_path(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()
        mock_custom_api = MagicMock()

        pod = MagicMock()
        pod.metadata.name = "payment-api-abc"
        pod.metadata.namespace = "production"
        container_spec = MagicMock()
        container_spec.name = "payment-api"
        container_spec.resources.limits = {"cpu": "500m", "memory": "512Mi"}
        pod.spec.containers = [container_spec]
        pod.spec.init_containers = []
        mock_core_api.list_namespaced_pod.return_value.items = [pod]

        mock_custom_api.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "payment-api-abc"},
                    "containers": [
                        {"name": "payment-api", "usage": {"cpu": "480m", "memory": "400Mi"}}
                    ],
                }
            ]
        }

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            records = adapter.list_container_resources("production")

        assert len(records) == 1
        r = records[0]
        assert r["pod_name"] == "payment-api-abc"
        assert r["container_name"] == "payment-api"
        assert r["cpu_usage_millicores"] == 480
        assert r["cpu_limit_millicores"] == 500
        assert r["memory_limit_bytes"] == 512 * _MiB
        assert r["memory_usage_bytes"] == 400 * _MiB
        assert r["is_init_container"] is False

    def test_list_container_resources_no_limits_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()
        mock_custom_api = MagicMock()

        pod = MagicMock()
        pod.metadata.name = "unlimit-pod"
        pod.metadata.namespace = "production"
        container_spec = MagicMock()
        container_spec.name = "app"
        container_spec.resources.limits = None
        pod.spec.containers = [container_spec]
        pod.spec.init_containers = []
        mock_core_api.list_namespaced_pod.return_value.items = [pod]

        mock_custom_api.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "unlimit-pod"},
                    "containers": [{"name": "app", "usage": {"cpu": "100m", "memory": "100Mi"}}],
                }
            ]
        }

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            records = adapter.list_container_resources("production")

        assert len(records) == 1
        assert records[0]["cpu_limit_millicores"] is None
        assert records[0]["memory_limit_bytes"] is None

    def test_metrics_api_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()
        mock_core_api.list_namespaced_pod.return_value.items = []

        mock_custom_api = MagicMock()

        class _ForbiddenError(Exception):
            status = 403

        mock_custom_api.list_namespaced_custom_object.side_effect = _ForbiddenError()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_container_resources("production")

    def test_metrics_api_404_raises_metrics_unavailable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()
        mock_core_api.list_namespaced_pod.return_value.items = []

        mock_custom_api = MagicMock()

        class _NotFoundError(Exception):
            status = 404

        mock_custom_api.list_namespaced_custom_object.side_effect = _NotFoundError()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            with pytest.raises(MetricsUnavailableError):
                adapter.list_container_resources("production")

    def test_core_api_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()

        class _ForbiddenError(Exception):
            status = 403

        mock_core_api.list_namespaced_pod.side_effect = _ForbiddenError()

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core_api):
            adapter = KubernetesPodResourceAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_container_resources("production")

    def test_init_containers_included(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )

        mock_core_api = MagicMock()
        mock_custom_api = MagicMock()

        pod = MagicMock()
        pod.metadata.name = "my-pod"
        pod.metadata.namespace = "production"

        init_spec = MagicMock()
        init_spec.name = "init-db"
        init_spec.resources.limits = {"cpu": "200m", "memory": "256Mi"}

        main_spec = MagicMock()
        main_spec.name = "app"
        main_spec.resources.limits = {"cpu": "500m", "memory": "512Mi"}

        pod.spec.init_containers = [init_spec]
        pod.spec.containers = [main_spec]
        mock_core_api.list_namespaced_pod.return_value.items = [pod]

        mock_custom_api.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "my-pod"},
                    "containers": [
                        {"name": "init-db", "usage": {"cpu": "50m", "memory": "100Mi"}},
                        {"name": "app", "usage": {"cpu": "100m", "memory": "200Mi"}},
                    ],
                }
            ]
        }

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            records = adapter.list_container_resources("production")

        assert len(records) == 2
        init_record = next(r for r in records if r["container_name"] == "init-db")
        main_record = next(r for r in records if r["container_name"] == "app")
        assert init_record["is_init_container"] is True
        assert main_record["is_init_container"] is False

    def test_unknown_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_core_api = MagicMock()
        mock_core_api.list_namespaced_pod.side_effect = RuntimeError("connection refused")

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core_api):
            adapter = KubernetesPodResourceAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_container_resources("production")

    def test_metrics_api_unknown_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_core_api = MagicMock()
        pod = MagicMock()
        pod.metadata.name = "pod-1"
        pod.metadata.namespace = "production"
        container_spec = MagicMock()
        container_spec.name = "app"
        container_spec.resources.limits = None
        pod.spec.containers = [container_spec]
        pod.spec.init_containers = []
        mock_core_api.list_namespaced_pod.return_value.items = [pod]

        mock_custom_api = MagicMock()

        class _UnknownError(Exception):
            status = 500

        mock_custom_api.list_namespaced_custom_object.side_effect = _UnknownError()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=mock_core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api),
        ):
            adapter = KubernetesPodResourceAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_container_resources("production")


# ── Tests: _parse_cpu ──────────────────────────────────────────────────────


class TestParseCpu:
    def test_bare_integer_returns_millicores(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu("1") == 1000
        assert _parse_cpu("2") == 2000

    def test_none_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu(None) is None

    def test_empty_string_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu("") is None

    def test_millicores_value(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu("500m") == 500

    def test_invalid_string_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu("invalid") is None


# ── Tests: _parse_memory ───────────────────────────────────────────────────


class TestParseMemory:
    def test_none_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory(None) is None

    def test_empty_string_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("") is None

    def test_mebibytes_value(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("512Mi") == 512 * (1024**2)

    def test_gibibytes_value(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("1Gi") == 1024**3

    def test_bare_integer_returns_bytes(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("1024") == 1024

    def test_invalid_suffix_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("512Xi") is None

    def test_valid_suffix_invalid_number_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("foobarMi") is None

    def test_invalid_bare_string_returns_none(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            _parse_memory,
        )

        assert _parse_memory("not-a-number") is None


# ── Tests: _build_adapter ──────────────────────────────────────────────────


class TestBuildAdapter:
    def test_returns_pod_resource_metrics_port(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
            KubernetesPodResourceAdapter,
        )
        from hexawyn.mcp.tools.check_resource_constraints import (
            _build_adapter,
        )

        with patch("kubernetes.client.CoreV1Api"), patch("kubernetes.client.CustomObjectsApi"):
            adapter = _build_adapter()
            assert isinstance(adapter, KubernetesPodResourceAdapter)
