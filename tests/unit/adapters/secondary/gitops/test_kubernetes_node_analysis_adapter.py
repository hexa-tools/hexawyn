from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
    KubernetesNodeAnalysisAdapter,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _make_node(name: str, cpu: str = "4", memory: str = "16Gi") -> MagicMock:
    node = MagicMock()
    node.metadata.name = name
    node.status.allocatable = {"cpu": cpu, "memory": memory}
    node.spec.unschedulable = False
    return node


def _make_cordoned_node(name: str, cpu: str = "8", memory: str = "32Gi") -> MagicMock:
    node = _make_node(name, cpu, memory)
    node.spec.unschedulable = True
    return node


def _make_pod(
    name: str,
    namespace: str,
    node_name: str,
    owner_kind: str | None = None,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.spec.node_name = node_name
    if owner_kind:
        owner = MagicMock()
        owner.kind = owner_kind
        pod.metadata.owner_references = [owner]
    else:
        pod.metadata.owner_references = None
    return pod


def _make_unscheduled_pod(
    name: str,
    namespace: str,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.spec.node_name = ""
    pod.metadata.owner_references = None
    return pod


class TestKubernetesNodeAnalysisAdapter:
    def test_implements_port(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()
        assert isinstance(adapter, HotNodeAnalysisPort)


class TestListNodes:
    def test_list_nodes(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            node_list = MagicMock()
            node_list.items = [
                _make_node("node-1", cpu="4", memory="16Gi"),
                _make_cordoned_node("node-2", cpu="8", memory="32Gi"),
            ]
            mock_core.list_node.return_value = node_list
            mock_core_cls.return_value = mock_core

            result = adapter.list_nodes()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "node-1"
        assert result[0]["allocatable_cpu_cores"] == 4.0  # noqa: PLR2004
        assert result[0]["allocatable_memory_gb"] == 16.0  # noqa: PLR2004
        assert result[0]["cordoned"] is False
        assert result[1]["cordoned"] is True

    def test_list_nodes_rbac_error(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_core.list_node.side_effect = api_exc
            mock_core_cls.return_value = mock_core

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_nodes()

    def test_list_nodes_other_error(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_node.side_effect = Exception("timeout")
            mock_core_cls.return_value = mock_core

            with pytest.raises(ClusterUnreachableError):
                adapter.list_nodes()


class TestListPodUsage:
    def test_list_pod_usage(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with (
            patch("kubernetes.client.CoreV1Api") as mock_core_cls,
            patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls,
        ):
            mock_core = MagicMock()
            pod_list = MagicMock()
            pod_list.items = [
                _make_pod("pod-1", "ns1", "node-1"),
                _make_pod("pod-2", "ns2", "node-2", owner_kind="DaemonSet"),
            ]
            mock_core.list_pod_for_all_namespaces.return_value = pod_list

            mock_custom = MagicMock()
            mock_custom.list_cluster_custom_object.return_value = {
                "items": [
                    {
                        "metadata": {"name": "pod-1", "namespace": "ns1"},
                        "containers": [{"usage": {"cpu": "500m", "memory": "1Gi"}}],
                    },
                    {
                        "metadata": {"name": "pod-2", "namespace": "ns2"},
                        "containers": [{"usage": {"cpu": "250m", "memory": "512Mi"}}],
                    },
                ]
            }
            mock_core_cls.return_value = mock_core
            mock_custom_cls.return_value = mock_custom

            result = adapter.list_pod_usage()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["pod_name"] == "pod-1"
        assert result[0]["node_name"] == "node-1"
        assert result[0]["cpu_usage_cores"] == 0.5  # noqa: PLR2004
        assert result[0]["memory_usage_gb"] == 1.0  # noqa: PLR2004
        assert result[0]["is_daemonset"] is False
        assert result[1]["is_daemonset"] is True

    def test_list_pod_usage_skips_pods_without_node(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with (
            patch("kubernetes.client.CoreV1Api") as mock_core_cls,
            patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls,
        ):
            mock_core = MagicMock()
            pod_list = MagicMock()
            pod_list.items = [
                _make_pod("pod-1", "ns1", "node-1"),
                _make_unscheduled_pod("unscheduled", "ns2"),
            ]
            mock_core.list_pod_for_all_namespaces.return_value = pod_list

            mock_custom = MagicMock()
            mock_custom.list_cluster_custom_object.return_value = {"items": []}
            mock_core_cls.return_value = mock_core
            mock_custom_cls.return_value = mock_custom

            result = adapter.list_pod_usage()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["pod_name"] == "pod-1"

    def test_list_pod_usage_handles_missing_metrics(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with (
            patch("kubernetes.client.CoreV1Api") as mock_core_cls,
            patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls,
        ):
            mock_core = MagicMock()
            pod_list = MagicMock()
            pod_list.items = [_make_pod("pod-1", "ns1", "node-1")]
            mock_core.list_pod_for_all_namespaces.return_value = pod_list

            mock_custom = MagicMock()
            mock_custom.list_cluster_custom_object.side_effect = Exception("metrics down")
            mock_core_cls.return_value = mock_core
            mock_custom_cls.return_value = mock_custom

            result = adapter.list_pod_usage()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["cpu_usage_cores"] == 0.0  # noqa: PLR2004
        assert result[0]["memory_usage_gb"] == 0.0  # noqa: PLR2004

    def test_list_pod_usage_rbac_error(self) -> None:
        adapter = KubernetesNodeAnalysisAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_core.list_pod_for_all_namespaces.side_effect = api_exc
            mock_core_cls.return_value = mock_core

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_pod_usage()
