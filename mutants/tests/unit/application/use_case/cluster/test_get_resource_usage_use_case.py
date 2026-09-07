from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import PodInfo


class TestGetResourceUsageUseCase:
    def _make_pod(
        self,
        namespace: str,
        name: str = "test-pod",
        cpu_millicores: int | None = None,
        memory_mib: int | None = None,
    ) -> PodInfo:
        pod: PodInfo = {"name": name, "namespace": namespace, "status": "Running"}
        if cpu_millicores is not None:
            pod["cpu_request_millicores"] = cpu_millicores
        if memory_mib is not None:
            pod["memory_request_mib"] = memory_mib
        return pod

    def test_empty_cluster_returns_empty_report(self) -> None:
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = []

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        assert hasattr(result, "pods")
        assert hasattr(result, "metrics_server_available")
        assert result.pods == []
        assert result.namespace_summary == []
        assert result.metrics_server_available is True

    def test_metrics_server_unavailable_graceful_degradation(self) -> None:
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )
        from hexawyn.domain.errors import MetricsUnavailableError

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("dev", "pod-1", cpu_millicores=1000, memory_mib=1024),
        ]
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.side_effect = MetricsUnavailableError("not installed")

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        assert result.metrics_server_available is False
        assert result.source == ""
        pod = result.pods[0]
        assert pod["cpu_requested_cores"] == 1.0
        assert pod["cpu_used_cores"] == 0.0
        assert pod["cpu_utilization_pct"] == -1.0

    def test_single_pod_with_usage_computes_utilization(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import (
            PodMetricSnapshot,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("dev", "app-pod", cpu_millicores=2000, memory_mib=4096),
        ]
        metrics_port = MagicMock()
        metric: PodMetricSnapshot = {
            "name": "app-pod",
            "namespace": "dev",
            "cpu_cores": 0.5,
            "memory_gb": 2.0,
        }
        metrics_port.get_pod_metrics.return_value = [metric]

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        pod = result.pods[0]
        assert pod["name"] == "app-pod"
        assert pod["cpu_requested_cores"] == 2.0  # noqa: PLR2004
        assert pod["cpu_used_cores"] == 0.5  # noqa: PLR2004
        assert pod["cpu_utilization_pct"] == 25.0  # noqa: PLR2004
        assert pod["memory_requested_gb"] == 4.0  # noqa: PLR2004
        assert pod["memory_used_gb"] == 2.0  # noqa: PLR2004
        assert pod["memory_utilization_pct"] == 50.0  # noqa: PLR2004
        assert result.metrics_server_available is True
        assert result.source == "metrics-server"

    def test_pod_without_metrics_gets_zero_usage(self) -> None:
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("dev", "orphan-pod", cpu_millicores=1000, memory_mib=512),
        ]
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = []

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        pod = result.pods[0]
        assert pod["cpu_used_cores"] == 0.0
        assert pod["memory_used_gb"] == 0.0
        assert pod["cpu_utilization_pct"] == 0.0
        assert pod["memory_utilization_pct"] == 0.0

    def test_namespace_summary_aggregates_multiple_pods(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import (
            PodMetricSnapshot,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("dev", "pod-a", cpu_millicores=1000, memory_mib=1024),
            self._make_pod("dev", "pod-b", cpu_millicores=2000, memory_mib=2048),
            self._make_pod("prod", "pod-c", cpu_millicores=500, memory_mib=512),
        ]
        metrics: list[PodMetricSnapshot] = [
            {"name": "pod-a", "namespace": "dev", "cpu_cores": 0.3, "memory_gb": 0.5},
            {"name": "pod-b", "namespace": "dev", "cpu_cores": 1.0, "memory_gb": 1.0},
            {"name": "pod-c", "namespace": "prod", "cpu_cores": 0.2, "memory_gb": 0.3},
        ]
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = metrics

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        dev = next(s for s in result.namespace_summary if s["namespace"] == "dev")
        assert dev["pod_count"] == 2  # noqa: PLR2004
        assert dev["total_cpu_requested_cores"] == 3.0  # noqa: PLR2004
        assert dev["total_cpu_used_cores"] == 1.3  # noqa: PLR2004
        assert 40 < dev["total_cpu_utilization_pct"] < 50  # noqa: PLR2004

        prod = next(s for s in result.namespace_summary if s["namespace"] == "prod")
        assert prod["pod_count"] == 1

    def test_namespace_filter_only_returns_target_namespace(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import (
            PodMetricSnapshot,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        all_pods = [
            self._make_pod("dev", "pod-a", cpu_millicores=1000, memory_mib=1024),
            self._make_pod("prod", "pod-b", cpu_millicores=500, memory_mib=512),
        ]
        k8s_port = MagicMock()
        k8s_port.list_pods.side_effect = lambda namespace=None: [
            p for p in all_pods if namespace is None or p["namespace"] == namespace
        ]
        all_metrics: list[PodMetricSnapshot] = [
            {"name": "pod-a", "namespace": "dev", "cpu_cores": 0.3, "memory_gb": 0.5},
            {"name": "pod-b", "namespace": "prod", "cpu_cores": 0.2, "memory_gb": 0.3},
        ]
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = all_metrics

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand(namespace="dev"))

        assert len(result.pods) == 1  # noqa: PLR2004
        assert result.pods[0]["namespace"] == "dev"
        assert len(result.namespace_summary) == 1  # noqa: PLR2004

    def test_pod_without_requests_zero_division_protection(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import (
            PodMetricSnapshot,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("ns", "bare-pod"),
        ]
        metric: PodMetricSnapshot = {
            "name": "bare-pod",
            "namespace": "ns",
            "cpu_cores": 0.5,
            "memory_gb": 0.3,
        }
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = [metric]

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand())

        pod = result.pods[0]
        assert pod["cpu_requested_cores"] == 0.0
        assert pod["cpu_used_cores"] == 0.5  # noqa: PLR2004
        assert pod["cpu_utilization_pct"] == -1.0
        assert pod["memory_utilization_pct"] == -1.0

    def test_resource_filter_cpu_only(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import (
            PodMetricSnapshot,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.command import (
            GetResourceUsageCommand,
        )
        from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (  # noqa: E501
            GetResourceUsageUseCase,
        )

        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("ns", "pod", cpu_millicores=1000, memory_mib=1024),
        ]
        metric: PodMetricSnapshot = {
            "name": "pod",
            "namespace": "ns",
            "cpu_cores": 0.5,
            "memory_gb": 0.5,
        }
        metrics_port = MagicMock()
        metrics_port.get_pod_metrics.return_value = [metric]

        use_case = GetResourceUsageUseCase(k8s_port=k8s_port, metrics_port=metrics_port)
        result = use_case.execute(GetResourceUsageCommand(resource="cpu"))

        pod = result.pods[0]
        assert pod["cpu_utilization_pct"] == 50.0  # noqa: PLR2004
        assert pod["memory_requested_gb"] == 0.0
        assert pod["memory_used_gb"] == 0.0
