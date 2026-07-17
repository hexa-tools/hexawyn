from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _node(
    name: str, cpu: str = "4000m", memory: str = "16Gi", unschedulable: bool = False
) -> MagicMock:
    node = MagicMock()
    node.metadata.name = name
    node.status.allocatable = {"cpu": cpu, "memory": memory}
    node.spec.unschedulable = unschedulable
    return node


def _node_list(*nodes: MagicMock) -> MagicMock:
    node_list = MagicMock()
    node_list.items = list(nodes)
    return node_list


def _owner_ref(kind: str) -> MagicMock:
    ref = MagicMock()
    ref.kind = kind
    return ref


def _pod(
    name: str,
    namespace: str = "production",
    node_name: str | None = "worker-1",
    owner_kind: str | None = None,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.metadata.owner_references = [_owner_ref(owner_kind)] if owner_kind else []
    pod.spec.node_name = node_name
    return pod


def _pod_list(*pods: MagicMock) -> MagicMock:
    pod_list = MagicMock()
    pod_list.items = list(pods)
    return pod_list


def _pod_metrics(namespace: str, name: str, cpu: str = "500m", memory: str = "512Mi") -> dict:
    return {
        "metadata": {"namespace": namespace, "name": name},
        "containers": [{"usage": {"cpu": cpu, "memory": memory}}],
    }


class TestKubernetesNodeAnalysisAdapterIsPort:
    def test_is_hot_node_analysis_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        assert isinstance(KubernetesNodeAnalysisAdapter(), HotNodeAnalysisPort)


class TestListNodes:
    def test_returns_allocatable_and_cordoned_status(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node("worker-1", cpu="4000m", memory="16Gi"),
            _node("worker-maintenance", unschedulable=True),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            nodes = adapter.list_nodes()

        by_name = {n["name"]: n for n in nodes}
        assert by_name["worker-1"]["allocatable_cpu_cores"] == pytest.approx(4.0)
        assert by_name["worker-1"]["cordoned"] is False
        assert by_name["worker-maintenance"]["cordoned"] is True

    def test_handles_all_cpu_and_memory_unit_suffixes(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.return_value = _node_list(
            _node("worker-u", cpu="2000000u", memory="1Ki"),
            _node("worker-n", cpu="2000000000n", memory="not-a-number"),
            _node("worker-bare", cpu="2", memory=str(1024**3)),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            nodes = adapter.list_nodes()

        by_name = {n["name"]: n for n in nodes}
        assert by_name["worker-u"]["allocatable_cpu_cores"] == pytest.approx(2.0)
        assert by_name["worker-n"]["allocatable_cpu_cores"] == pytest.approx(2.0)
        assert by_name["worker-n"]["allocatable_memory_gb"] == 0.0
        assert by_name["worker-bare"]["allocatable_cpu_cores"] == pytest.approx(2.0)
        assert by_name["worker-bare"]["allocatable_memory_gb"] == pytest.approx(1.0)

    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_node.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_nodes()

    def test_other_errors_translate_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_node.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_nodes()


class TestListPodUsage:
    def test_joins_pod_to_node_and_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _pod_list(
            _pod("app-xyz", node_name="worker-1")
        )
        custom_api = MagicMock()
        custom_api.list_cluster_custom_object.return_value = {
            "items": [_pod_metrics("production", "app-xyz", cpu="500m", memory="512Mi")]
        }

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=custom_api),
        ):
            adapter = KubernetesNodeAnalysisAdapter()
            usage = adapter.list_pod_usage()

        assert len(usage) == 1
        assert usage[0]["node_name"] == "worker-1"
        assert usage[0]["cpu_usage_cores"] == pytest.approx(0.5)
        assert usage[0]["memory_usage_gb"] == pytest.approx(0.5)
        assert usage[0]["is_daemonset"] is False

    def test_pod_without_owner_references_is_not_daemonset(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        pod = _pod("standalone-pod", node_name="worker-1")
        pod.metadata.owner_references = None
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _pod_list(pod)
        custom_api = MagicMock()
        custom_api.list_cluster_custom_object.return_value = {"items": []}

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=custom_api),
        ):
            adapter = KubernetesNodeAnalysisAdapter()
            usage = adapter.list_pod_usage()

        assert usage[0]["is_daemonset"] is False

    def test_daemonset_owned_pod_is_flagged(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _pod_list(
            _pod("fluentd-abc", node_name="worker-1", owner_kind="DaemonSet")
        )
        custom_api = MagicMock()
        custom_api.list_cluster_custom_object.return_value = {"items": []}

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=custom_api),
        ):
            adapter = KubernetesNodeAnalysisAdapter()
            usage = adapter.list_pod_usage()

        assert usage[0]["is_daemonset"] is True

    def test_unscheduled_pod_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _pod_list(
            _pod("pending-pod", node_name=None)
        )
        custom_api = MagicMock()
        custom_api.list_cluster_custom_object.return_value = {"items": []}

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=custom_api),
        ):
            adapter = KubernetesNodeAnalysisAdapter()
            usage = adapter.list_pod_usage()

        assert usage == []

    def test_pod_missing_from_metrics_response_defaults_to_zero(self) -> None:
        """Edge case: Kubernetes metrics unavailable for a pod (kubelet
        issue) → defaults to 0 usage rather than failing the whole call."""
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _pod_list(
            _pod("no-metrics-pod", node_name="worker-1")
        )
        custom_api = MagicMock()
        custom_api.list_cluster_custom_object.side_effect = Exception("metrics-server unavailable")

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.CustomObjectsApi", return_value=custom_api),
        ):
            adapter = KubernetesNodeAnalysisAdapter()
            usage = adapter.list_pod_usage()

        assert usage[0]["cpu_usage_cores"] == 0.0
        assert usage[0]["memory_usage_gb"] == 0.0

    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_pod_for_all_namespaces.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_pod_usage()

    def test_other_errors_translate_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
            KubernetesNodeAnalysisAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNodeAnalysisAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_pod_usage()
