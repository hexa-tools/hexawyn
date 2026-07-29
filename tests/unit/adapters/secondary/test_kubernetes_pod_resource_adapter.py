from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
    KubernetesPodResourceAdapter,
)
from hexawyn.application.ports.driven.pod_resource_metrics_port import (
    PodResourceMetricsPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)


class TestKubernetesPodResourceAdapter:
    def test_implements_port(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        assert isinstance(adapter, PodResourceMetricsPort)


class TestFetchPodLimits:
    def test_fetches_pod_limits(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        mock_pod = _make_pod("my-pod", "my-ns", containers={"app": ("500m", "256Mi")})
        pod_list = MagicMock()
        pod_list.items = [mock_pod]

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_namespaced_pod.return_value = pod_list
            mock_core_cls.return_value = mock_core

            limits = adapter._fetch_pod_limits("my-ns")

        assert "my-pod" in limits
        assert len(limits["my-pod"]) == 1  # noqa: PLR2004
        assert limits["my-pod"][0][0] == "app"

    def test_rbac_403_raises(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_core.list_namespaced_pod.side_effect = api_exc
            mock_core_cls.return_value = mock_core

            with pytest.raises(InsufficientPermissionsError):
                adapter._fetch_pod_limits("ns1")

    def test_other_error_raises_cluster_unreachable(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_namespaced_pod.side_effect = Exception("connection refused")
            mock_core_cls.return_value = mock_core

            with pytest.raises(ClusterUnreachableError):
                adapter._fetch_pod_limits("ns1")

    def test_includes_init_containers(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        mock_pod = _make_pod(
            "pod1",
            "ns1",
            containers={"main": ("1", "1Gi")},
            init_containers={"init-db": ("250m", "512Mi")},
        )
        pod_list = MagicMock()
        pod_list.items = [mock_pod]

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_namespaced_pod.return_value = pod_list
            mock_core_cls.return_value = mock_core

            limits = adapter._fetch_pod_limits("ns1")

        assert len(limits["pod1"]) == 2  # noqa: PLR2004
        _, _, _, is_init = limits["pod1"][0]
        assert is_init is True
        _, _, _, is_not_init = limits["pod1"][1]
        assert is_not_init is False

    def test_no_resources_set(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        mock_pod = _make_pod("pod1", "ns1", containers={"app": (None, None)})
        pod_list = MagicMock()
        pod_list.items = [mock_pod]

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_namespaced_pod.return_value = pod_list
            mock_core_cls.return_value = mock_core

            limits = adapter._fetch_pod_limits("ns1")

        container_cpu = limits["pod1"][0][1]
        container_mem = limits["pod1"][0][2]
        assert container_cpu is None
        assert container_mem is None


class TestFetchMetrics:
    def test_fetches_metrics(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            mock_custom.list_namespaced_custom_object.return_value = {
                "items": [
                    {
                        "metadata": {"name": "my-pod", "namespace": "ns1"},
                        "containers": [
                            {
                                "name": "app",
                                "usage": {"cpu": "200m", "memory": "128Mi"},
                            }
                        ],
                    }
                ]
            }
            mock_custom_cls.return_value = mock_custom

            usage = adapter._fetch_metrics("ns1")

        assert "my-pod" in usage
        cpu, mem = usage["my-pod"]["app"]
        assert cpu == 200  # noqa: PLR2004
        assert mem == 128 * 1024 * 1024

    def test_metrics_403_raises(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_custom.list_namespaced_custom_object.side_effect = api_exc
            mock_custom_cls.return_value = mock_custom

            with pytest.raises(InsufficientPermissionsError):
                adapter._fetch_metrics("ns1")

    def test_metrics_404_raises_metrics_unavailable(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            api_exc = Exception("not found")
            api_exc.status = 404
            mock_custom.list_namespaced_custom_object.side_effect = api_exc
            mock_custom_cls.return_value = mock_custom

            with pytest.raises(MetricsUnavailableError):
                adapter._fetch_metrics("ns1")

    def test_metrics_other_error_raises_cluster_unreachable(self) -> None:
        adapter = KubernetesPodResourceAdapter()

        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            mock_custom.list_namespaced_custom_object.side_effect = Exception("timeout")
            mock_custom_cls.return_value = mock_custom

            with pytest.raises(ClusterUnreachableError):
                adapter._fetch_metrics("ns1")


class TestListContainerResources:
    def test_merges_limits_and_usage(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        adapter._fetch_pod_limits = MagicMock(  # type: ignore[method-assign]
            return_value={"my-pod": [("app", 500, 256 * 1024 * 1024, False)]}
        )
        adapter._fetch_metrics = MagicMock(  # type: ignore[method-assign]
            return_value={"my-pod": {"app": (200, 128 * 1024 * 1024)}}
        )

        result = adapter.list_container_resources("ns1")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["container_name"] == "app"
        assert result[0]["cpu_usage_millicores"] == 200  # noqa: PLR2004
        assert result[0]["cpu_limit_millicores"] == 500  # noqa: PLR2004
        assert result[0]["memory_usage_bytes"] == 128 * 1024 * 1024
        assert result[0]["memory_limit_bytes"] == 256 * 1024 * 1024

    def test_default_usage_when_no_metrics(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        adapter._fetch_pod_limits = MagicMock(  # type: ignore[method-assign]
            return_value={"my-pod": [("app", 500, None, False)]}
        )
        adapter._fetch_metrics = MagicMock(  # type: ignore[method-assign]
            return_value={}
        )

        result = adapter.list_container_resources("ns1")

        assert result[0]["cpu_usage_millicores"] == 0  # noqa: PLR2004
        assert result[0]["memory_usage_bytes"] == 0  # noqa: PLR2004

    def test_multiple_pods(self) -> None:
        adapter = KubernetesPodResourceAdapter()
        adapter._fetch_pod_limits = MagicMock(  # type: ignore[method-assign]
            return_value={
                "pod-a": [("app", 1000, 512 * 1024 * 1024, False)],
                "pod-b": [("worker", 500, 256 * 1024 * 1024, False)],
            }
        )
        adapter._fetch_metrics = MagicMock(  # type: ignore[method-assign]
            return_value={
                "pod-a": {"app": (300, 128 * 1024 * 1024)},
                "pod-b": {"worker": (100, 64 * 1024 * 1024)},
            }
        )

        result = adapter.list_container_resources("ns1")

        assert len(result) == 2  # noqa: PLR2004


def _make_container(name: str, cpu: str | None = None, memory: str | None = None) -> MagicMock:
    container = MagicMock()
    container.name = name
    container.resources = MagicMock()
    container.resources.limits = {}
    if cpu:
        container.resources.limits["cpu"] = cpu
    if memory:
        container.resources.limits["memory"] = memory
    return container


def _make_pod(
    name: str,
    namespace: str,
    containers: dict[str, tuple[str | None, str | None]] | None = None,
    init_containers: dict[str, tuple[str | None, str | None]] | None = None,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.spec.containers = [
        _make_container(cname, cpu, mem) for cname, (cpu, mem) in (containers or {}).items()
    ]
    pod.spec.init_containers = [
        _make_container(cname, cpu, mem) for cname, (cpu, mem) in (init_containers or {}).items()
    ]
    return pod
