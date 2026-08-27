from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import VanillaK8sAdapter
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.domain.errors import ClusterUnreachableError


def _fake_pod(name: str, namespace: str, phase: str = "Running") -> MagicMock:
    pod = MagicMock()
    metadata = MagicMock()
    metadata.name = name
    metadata.namespace = namespace
    metadata.creation_timestamp = None
    pod.metadata = metadata

    spec = MagicMock()
    spec.node_name = "node-1"
    spec.containers = []
    pod.spec = spec

    status = MagicMock()
    status.phase = phase
    status.container_statuses = []
    pod.status = status

    return pod


def _fake_namespace(name: str, phase: str = "Active") -> MagicMock:
    ns = MagicMock()
    metadata = MagicMock()
    metadata.name = name
    metadata.creation_timestamp = None
    ns.metadata = metadata

    status = MagicMock()
    status.phase = phase
    ns.status = status

    return ns


def _fake_node_ready(name: str) -> MagicMock:
    node = MagicMock()
    metadata = MagicMock()
    metadata.name = name
    node.metadata = metadata

    status = MagicMock()
    ready_cond = MagicMock()
    ready_cond.type = "Ready"
    ready_cond.status = "True"
    status.conditions = [ready_cond]

    allocatable = {"cpu": "2", "memory": "4Gi"}
    status.allocatable = allocatable

    node.status = status
    return node


class TestVanillaK8sAdapter:
    def test_implements_k8s_port(self) -> None:
        api = MagicMock()
        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        assert isinstance(adapter, K8sPort)

    def test_list_namespaces_returns_namespaces(self) -> None:
        api = MagicMock()
        ns = _fake_namespace("default")
        response = MagicMock()
        response.items = [ns]
        api.list_namespace.return_value = response

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        result = adapter.list_namespaces()

        assert len(result) == 1
        assert isinstance(result[0], dict)
        assert result[0]["name"] == "default"
        assert result[0]["status"] == "Active"

    def test_list_namespaces_empty(self) -> None:
        api = MagicMock()
        response = MagicMock()
        response.items = []
        api.list_namespace.return_value = response

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        result = adapter.list_namespaces()

        assert result == []

    def test_list_namespaces_api_error_raises_cluster_unreachable(self) -> None:
        api = MagicMock()
        api.list_namespace.side_effect = OSError("Connection refused")

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        with pytest.raises(ClusterUnreachableError):
            adapter.list_namespaces()

    def test_list_namespaces_surfaces_kubeconfig_load_failure(self) -> None:
        """Edge case: no injected api, and the lazy kubeconfig load fails.

        The MCP tool must surface the wrapped ``Cannot list namespaces`` error
        rather than crash, so a cluster without a reachable kubeconfig degrades
        gracefully instead of taking the tool down.
        """
        with patch(
            "hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter.load_kubeconfig",
            side_effect=ClusterUnreachableError("Unable to load kubeconfig."),
        ):
            adapter = VanillaK8sAdapter(
                api=None, metrics_api=MagicMock(), cluster_name="hetzner-preprod"
            )
            with pytest.raises(ClusterUnreachableError) as exc:
                adapter.list_namespaces()

        assert "Cannot list namespaces" in str(exc.value)
        assert "Unable to load kubeconfig" in str(exc.value)

    def test_get_cluster_context_returns_metadata(self) -> None:
        api = MagicMock()
        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="my-cluster")
        result = adapter.get_cluster_context()

        assert result["name"] == "my-cluster"
        assert result["cluster"] == "my-cluster"
        assert result["provider"] == "vanilla"
        assert result["namespace"] == "default"

    def test_get_cluster_context_kind_cluster(self) -> None:
        api = MagicMock()
        adapter = VanillaK8sAdapter(
            api=api, metrics_api=MagicMock(), cluster_name="kind-my-cluster"
        )
        result = adapter.get_cluster_context()

        assert result["provider"] == "kind"

    def test_list_pods_returns_pods(self) -> None:
        api = MagicMock()
        pod = _fake_pod("my-pod", "default")
        response = MagicMock()
        response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        result = adapter.list_pods()

        assert len(result) == 1
        assert result[0]["name"] == "my-pod"
        assert result[0]["namespace"] == "default"
        assert result[0]["status"] == "Running"

    def test_list_pods_namespace_filtered(self) -> None:
        api = MagicMock()
        pod = _fake_pod("my-pod", "default")
        response = MagicMock()
        response.items = [pod]
        api.list_namespaced_pod.return_value = response

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        result = adapter.list_pods(namespace="default")

        assert len(result) == 1
        api.list_namespaced_pod.assert_called_once_with(namespace="default", timeout_seconds=5)

    def test_list_pods_empty(self) -> None:
        api = MagicMock()
        response = MagicMock()
        response.items = []
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaK8sAdapter(api=api, metrics_api=MagicMock(), cluster_name="test")
        result = adapter.list_pods()

        assert result == []

    def test_get_cluster_metrics_returns_data(self) -> None:
        api = MagicMock()
        node = _fake_node_ready("node-1")
        node_response = MagicMock()
        node_response.items = [node]
        api.list_node.return_value = node_response

        pod = _fake_pod("my-pod", "default")
        pod_response = MagicMock()
        pod_response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = pod_response

        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": []}

        adapter = VanillaK8sAdapter(api=api, metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_cluster_metrics()

        assert result["node_count"] == 1
        assert result["pod_count"] == 1
        assert "cpu_usage_pct" in result
        assert "memory_usage_pct" in result

    def test_api_client_lazy_initialization(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter.load_kubeconfig",
            return_value=MagicMock(),
        ) as mock_load:
            adapter = VanillaK8sAdapter(api=None, metrics_api=MagicMock(), cluster_name="test")
            api = adapter._api_client()

        mock_load.assert_called_once_with(context="test")
        assert api is adapter._api

    def test_metrics_api_client_lazy_initialization(self) -> None:
        fake_core = MagicMock()
        fake_core.api_client = MagicMock()
        with (
            patch(
                "hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter.load_kubeconfig",
                return_value=fake_core,
            ) as mock_load,
            patch(
                "hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter.client.CustomObjectsApi"
            ) as mock_custom,
        ):
            adapter = VanillaK8sAdapter(api=None, metrics_api=None, cluster_name="test")
            metrics_api = adapter._metrics_api_client()

        mock_load.assert_called_once()
        mock_custom.assert_called_once_with(api_client=fake_core.api_client)
        assert metrics_api is adapter._metrics_api

    def test_context_name_unknown_cluster_returns_none(self) -> None:
        adapter = VanillaK8sAdapter(
            api=MagicMock(), metrics_api=MagicMock(), cluster_name="unknown"
        )
        assert adapter._context_name() is None

    def test_resource_requests_sums_containers(self) -> None:
        container = MagicMock()
        container.resources.requests = {"cpu": "500m", "memory": "256Mi"}
        container2 = MagicMock()
        container2.resources.requests = {"cpu": "1", "memory": "512Mi"}

        spec = MagicMock()
        spec.containers = [container, container2]

        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=MagicMock(), cluster_name="test")
        cpu, mem = adapter._resource_requests(spec)

        assert cpu == 1500  # noqa: PLR2004
        assert mem == 768  # noqa: PLR2004

    def test_resource_requests_handles_exception(self) -> None:
        class _BrokenSpec:
            @property
            def containers(self) -> list[object]:
                raise RuntimeError("broken spec")

        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=MagicMock(), cluster_name="test")
        cpu, mem = adapter._resource_requests(_BrokenSpec())

        assert cpu == 0
        assert mem == 0

    def test_resource_requests_skips_container_without_resources(self) -> None:
        container = MagicMock()
        container.resources = None

        spec = MagicMock()
        spec.containers = [container]

        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=MagicMock(), cluster_name="test")
        cpu, mem = adapter._resource_requests(spec)

        assert cpu == 0
        assert mem == 0

    def test_node_metrics_usage_returns_zero_on_error(self) -> None:
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.side_effect = RuntimeError("metrics down")

        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=metrics_api, cluster_name="test")
        cpu, memory = adapter._node_metrics_usage()

        assert cpu == 0.0
        assert memory == 0.0

    def test_pod_status_waiting_reason_wins(self) -> None:
        status = MagicMock()
        status.container_statuses = [
            MagicMock(
                state=MagicMock(
                    waiting=MagicMock(reason="CrashLoopBackOff"),
                ),
                restart_count=3,
            )
        ]

        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=MagicMock(), cluster_name="test")
        result = adapter._pod_status(status)

        assert result == "CrashLoop"
