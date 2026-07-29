from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
    KubernetesLabelSearchAdapter,
    _pod_ready,
    _to_non_pod_raw,
    _to_pod_raw,
)


class TestKubernetesLabelSearchAdapter:
    def test_search_pods_namespaced(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_pod = MagicMock()
        mock_pod.metadata.name = "resource-1"
        mock_pod.metadata.namespace = "default"
        mock_pod.metadata.labels = {"app": "my-app"}
        mock_pod.spec.node_name = "node-1"
        mock_pod.status.phase = "Running"
        mock_pod.status.container_statuses = []

        mock_core = MagicMock()
        mock_core.list_namespaced_pod.return_value = MagicMock(items=[mock_pod])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_pods("app=my-app", "default")

            assert len(result) == 1
            assert result[0]["name"] == "resource-1"
            assert result[0]["kind"] == "pod"

    def test_search_pods_all_namespaces(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_pod = MagicMock()
        mock_pod.metadata.name = "resource-1"
        mock_pod.metadata.namespace = "default"
        mock_pod.metadata.labels = {}
        mock_pod.spec.node_name = "node-1"
        mock_pod.status.phase = "Running"
        mock_pod.status.container_statuses = []

        mock_core = MagicMock()
        mock_core.list_pod_for_all_namespaces.return_value = MagicMock(items=[mock_pod])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_pods("app=my-app", None)

            assert len(result) == 1

    def test_search_deployments_namespaced(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_deploy = MagicMock()
        mock_deploy.metadata.name = "resource-1"
        mock_deploy.metadata.namespace = "default"
        mock_deploy.metadata.labels = {"app": "my-app"}

        mock_apps = MagicMock()
        mock_apps.list_namespaced_deployment.return_value = MagicMock(items=[mock_deploy])

        with patch("kubernetes.client.AppsV1Api", return_value=mock_apps):
            result = adapter.search_deployments("app=my-app", "default")

            assert len(result) == 1
            assert result[0]["kind"] == "deployment"

    def test_search_deployments_all_namespaces(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_deploy = MagicMock()
        mock_deploy.metadata.name = "resource-1"
        mock_deploy.metadata.namespace = "default"
        mock_deploy.metadata.labels = {}

        mock_apps = MagicMock()
        mock_apps.list_deployment_for_all_namespaces.return_value = MagicMock(items=[mock_deploy])

        with patch("kubernetes.client.AppsV1Api", return_value=mock_apps):
            result = adapter.search_deployments("app=my-app", None)

            assert len(result) == 1

    def test_search_services_namespaced(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_svc = MagicMock()
        mock_svc.metadata.name = "resource-1"
        mock_svc.metadata.namespace = "default"
        mock_svc.metadata.labels = {}

        mock_core = MagicMock()
        mock_core.list_namespaced_service.return_value = MagicMock(items=[mock_svc])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_services("app=my-app", "default")

            assert len(result) == 1
            assert result[0]["kind"] == "service"

    def test_search_services_all_namespaces(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_svc = MagicMock()
        mock_svc.metadata.name = "resource-1"
        mock_svc.metadata.namespace = "default"
        mock_svc.metadata.labels = {}

        mock_core = MagicMock()
        mock_core.list_service_for_all_namespaces.return_value = MagicMock(items=[mock_svc])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_services("app=my-app", None)

            assert len(result) == 1

    def test_search_configmaps_namespaced(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_cm = MagicMock()
        mock_cm.metadata.name = "resource-1"
        mock_cm.metadata.namespace = "default"
        mock_cm.metadata.labels = {}

        mock_core = MagicMock()
        mock_core.list_namespaced_config_map.return_value = MagicMock(items=[mock_cm])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_configmaps("app=my-app", "default")

            assert len(result) == 1
            assert result[0]["kind"] == "configmap"

    def test_search_configmaps_all_namespaces(self) -> None:
        adapter = KubernetesLabelSearchAdapter()
        mock_cm = MagicMock()
        mock_cm.metadata.name = "resource-1"
        mock_cm.metadata.namespace = "default"
        mock_cm.metadata.labels = {}

        mock_core = MagicMock()
        mock_core.list_config_map_for_all_namespaces.return_value = MagicMock(items=[mock_cm])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.search_configmaps("app=my-app", None)

            assert len(result) == 1


class TestToPodRaw:
    def test_converts_pod_correctly(self) -> None:
        mock_pod = MagicMock()
        mock_pod.metadata.name = "my-pod"
        mock_pod.metadata.namespace = "default"
        mock_pod.metadata.labels = {"app": "x"}
        mock_pod.spec.node_name = "node-1"
        mock_pod.status.phase = "Running"
        mock_pod.status.container_statuses = []

        result = _to_pod_raw(mock_pod)

        assert result["name"] == "my-pod"
        assert result["node"] == "node-1"
        assert result["phase"] == "Running"
        assert result["kind"] == "pod"

    def test_converts_pod_with_unknown_phase(self) -> None:
        mock_pod = MagicMock()
        mock_pod.metadata.name = "my-pod"
        mock_pod.metadata.namespace = "default"
        mock_pod.metadata.labels = {}
        mock_pod.spec.node_name = "node-1"
        mock_pod.status.phase = None
        mock_pod.status.container_statuses = []

        result = _to_pod_raw(mock_pod)

        assert result["phase"] == "Unknown"


class TestPodReady:
    def test_all_containers_ready_returns_true(self) -> None:
        mock_pod = MagicMock()
        mock_cs1 = MagicMock()
        mock_cs1.ready = True
        mock_cs2 = MagicMock()
        mock_cs2.ready = True
        mock_pod.status.container_statuses = [mock_cs1, mock_cs2]

        assert _pod_ready(mock_pod) is True

    def test_one_not_ready_returns_false(self) -> None:
        mock_pod = MagicMock()
        mock_cs1 = MagicMock()
        mock_cs1.ready = True
        mock_cs2 = MagicMock()
        mock_cs2.ready = False
        mock_pod.status.container_statuses = [mock_cs1, mock_cs2]

        assert _pod_ready(mock_pod) is False

    def test_no_statuses_returns_false(self) -> None:
        mock_pod = MagicMock()
        mock_pod.status.container_statuses = None

        assert _pod_ready(mock_pod) is False

    def test_empty_statuses_returns_false(self) -> None:
        mock_pod = MagicMock()
        mock_pod.status.container_statuses = []

        assert _pod_ready(mock_pod) is False


class TestToNonPodRaw:
    def test_converts_deployment_correctly(self) -> None:
        mock_item = MagicMock()
        mock_item.metadata.name = "my-deploy"
        mock_item.metadata.namespace = "default"
        mock_item.metadata.labels = {"app": "x"}

        result = _to_non_pod_raw(mock_item, "deployment")

        assert result["name"] == "my-deploy"
        assert result["kind"] == "deployment"
        assert result["node"] is None
        assert result["phase"] is None
        assert result["ready"] is None
        assert result["labels"] == {"app": "x"}
