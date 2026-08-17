# mypy: ignore-errors
"""Integration tests: GetResourceUsageUseCase → VanillaAdapter → mocked K8s API + metrics-server."""

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.use_case.cluster.get_resource_usage.command import (
    GetResourceUsageCommand,
)
from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (
    GetResourceUsageUseCase,
)


def _container(cpu: str | None = "500m", memory: str | None = "1Gi") -> MagicMock:
    c = MagicMock()
    requests: dict[str, str] = {}
    if cpu:
        requests["cpu"] = cpu
    if memory:
        requests["memory"] = memory
    c.resources.requests = requests or None
    return c


def _pod(
    namespace: str, name: str = "test-pod", cpu: str | None = "500m", memory: str | None = "1Gi"
) -> MagicMock:  # noqa: E501
    from datetime import UTC, datetime, timedelta

    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.metadata.creation_timestamp = datetime.now(UTC) - timedelta(days=30)
    pod.spec.containers = [_container(cpu, memory)]
    return pod


def _fake_core_api(pods: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    pod_list = MagicMock()
    pod_list.items = pods
    api.list_pod_for_all_namespaces.return_value = pod_list

    def _list_namespaced(namespace: str, **kwargs: object) -> MagicMock:  # noqa: ARG001
        filtered = MagicMock()
        filtered.items = [p for p in pods if p.metadata.namespace == namespace]
        return filtered

    api.list_namespaced_pod.side_effect = _list_namespaced
    return api


def _fake_metrics_api(pod_metrics: list[dict[str, object]]) -> MagicMock:
    api = MagicMock()
    raw = {"items": pod_metrics}
    api.list_cluster_custom_object.return_value = raw
    return api


def _pod_metric(
    name: str, namespace: str, cpu_nanocores: str = "500000000n", memory: str = "1048576Ki"
) -> dict[str, object]:  # noqa: E501
    return {
        "metadata": {"name": name, "namespace": namespace},
        "containers": [{"usage": {"cpu": cpu_nanocores, "memory": memory}}],
    }


def _build_use_case(
    api: MagicMock, metrics_api: MagicMock | None = None
) -> GetResourceUsageUseCase:  # noqa: E501
    adapter = VanillaAdapter("test-cluster", api=api, metrics_api=metrics_api)
    return GetResourceUsageUseCase(k8s_port=adapter, metrics_port=adapter)


@pytest.mark.integration
class TestGetResourceUsageIntegration:
    def test_vanilla_adapter_implements_both_ports(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import K8sPort
        from hexawyn.application.ports.driven.pod_metrics_port import PodMetricsPort

        adapter = VanillaAdapter("test")
        assert isinstance(adapter, K8sPort)
        assert isinstance(adapter, PodMetricsPort)

    def test_single_pod_with_metrics_computes_utilization(self) -> None:
        pods = [_pod("dev", "app-pod", cpu="2000m", memory="4096Mi")]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [_pod_metric("app-pod", "dev", cpu_nanocores="500000000n", memory="2097152Ki")]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand())

        assert len(result.pods) == 1  # noqa: PLR2004
        pod = result.pods[0]
        assert pod["name"] == "app-pod"
        assert pod["namespace"] == "dev"
        assert pod["cpu_requested_cores"] == 2.0  # noqa: PLR2004
        assert pod["cpu_used_cores"] == 0.5  # noqa: PLR2004
        assert pod["cpu_utilization_pct"] == 25.0  # noqa: PLR2004
        assert pod["memory_requested_gb"] == 4.0  # noqa: PLR2004
        assert pod["memory_used_gb"] == 2.0  # noqa: PLR2004
        assert pod["memory_utilization_pct"] == 50.0  # noqa: PLR2004
        assert result.metrics_server_available is True
        assert result.source == "metrics-server"

    def test_namespace_summary_aggregates_multiple_pods(self) -> None:
        pods = [
            _pod("dev", "pod-a", cpu="1000m", memory="1024Mi"),
            _pod("dev", "pod-b", cpu="2000m", memory="2048Mi"),
            _pod("prod", "pod-c", cpu="500m", memory="512Mi"),
        ]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [
                _pod_metric("pod-a", "dev", cpu_nanocores="300000000n", memory="524288Ki"),
                _pod_metric("pod-b", "dev", cpu_nanocores="1000000000n", memory="1048576Ki"),
                _pod_metric("pod-c", "prod", cpu_nanocores="200000000n", memory="262144Ki"),
            ]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand())

        assert len(result.pods) == 3  # noqa: PLR2004
        dev = next(s for s in result.namespace_summary if s["namespace"] == "dev")
        assert dev["pod_count"] == 2  # noqa: PLR2004
        assert dev["total_cpu_requested_cores"] == 3.0  # noqa: PLR2004
        assert dev["total_cpu_used_cores"] == 1.3  # noqa: PLR2004

    def test_metrics_server_unavailable_graceful(self) -> None:
        pods = [_pod("dev", "pod-1", cpu="1000m", memory="1024Mi")]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api, metrics_api=None)
        result = use_case.execute(GetResourceUsageCommand())

        assert result.metrics_server_available is False
        assert result.source == ""
        pod = result.pods[0]
        assert pod["cpu_requested_cores"] == 1.0  # noqa: PLR2004
        assert pod["cpu_used_cores"] == 0.0
        assert pod["cpu_utilization_pct"] == -1.0

    def test_pod_missing_from_metrics_gets_zero(self) -> None:
        pods = [
            _pod("dev", "tracked", cpu="1000m", memory="1024Mi"),
            _pod("dev", "untracked", cpu="500m", memory="512Mi"),
        ]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [_pod_metric("tracked", "dev", cpu_nanocores="200000000n", memory="524288Ki")]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand())

        tracked = next(p for p in result.pods if p["name"] == "tracked")
        untracked = next(p for p in result.pods if p["name"] == "untracked")
        assert tracked["cpu_used_cores"] == 0.2  # noqa: PLR2004
        assert untracked["cpu_used_cores"] == 0.0

    def test_namespace_filter_excludes_other_namespaces(self) -> None:
        pods = [
            _pod("dev", "pod-dev", cpu="1000m", memory="1024Mi"),
            _pod("prod", "pod-prod", cpu="2000m", memory="2048Mi"),
        ]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [
                _pod_metric("pod-dev", "dev", cpu_nanocores="300000000n", memory="524288Ki"),
                _pod_metric("pod-prod", "prod", cpu_nanocores="500000000n", memory="1048576Ki"),
            ]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand(namespace="dev"))

        assert len(result.pods) == 1  # noqa: PLR2004
        assert result.pods[0]["namespace"] == "dev"

    def test_resource_filter_cpu_only(self) -> None:
        pods = [_pod("ns", "pod", cpu="2000m", memory="4096Mi")]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [_pod_metric("pod", "ns", cpu_nanocores="1000000000n", memory="2097152Ki")]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand(resource="cpu"))

        pod = result.pods[0]
        assert pod["cpu_utilization_pct"] == 50.0  # noqa: PLR2004
        assert pod["memory_requested_gb"] == 0.0
        assert pod["memory_used_gb"] == 0.0

    def test_memory_only_filter(self) -> None:
        pods = [_pod("ns", "pod", cpu="2000m", memory="4096Mi")]
        api = _fake_core_api(pods)
        metrics_api = _fake_metrics_api(
            [_pod_metric("pod", "ns", cpu_nanocores="1000000000n", memory="2097152Ki")]
        )

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand(resource="memory"))

        pod = result.pods[0]
        assert pod["cpu_requested_cores"] == 0.0
        assert pod["memory_utilization_pct"] == 50.0  # noqa: PLR2004

    def test_metrics_api_raises_handled(self) -> None:
        pods = [_pod("dev", "pod-1", cpu="1000m", memory="1024Mi")]
        api = _fake_core_api(pods)
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.side_effect = RuntimeError("timeout")

        use_case = _build_use_case(api, metrics_api)
        result = use_case.execute(GetResourceUsageCommand())

        assert result.metrics_server_available is False
