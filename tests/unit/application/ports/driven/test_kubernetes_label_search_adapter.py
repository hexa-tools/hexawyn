"""Unit tests for KubernetesLabelSearchAdapter (mocks kubernetes.client)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort

_DEFAULT_LABELS = {"app": "payment"}


def _pod(
    name: str = "payment-pod-abc12",
    namespace: str = "production",
    node: str = "worker-1",
    phase: str = "Running",
    container_ready: list[bool] | None = None,
    labels: dict[str, str] | None = _DEFAULT_LABELS,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.labels = labels
    item.spec.node_name = node
    item.status.phase = phase
    ready_flags = [True] if container_ready is None else container_ready
    item.status.container_statuses = (
        [MagicMock(ready=flag) for flag in ready_flags] if ready_flags else []
    )
    return item


def _non_pod(name: str, namespace: str = "production") -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.labels = {"app": "payment"}
    return item


class TestImplementsPort:
    def test_implements_resource_search_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        assert isinstance(KubernetesLabelSearchAdapter(), ResourceSearchPort)


class TestSearchPods:
    def test_all_namespaces_call_when_namespace_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        pod_list = MagicMock()
        pod_list.items = [_pod()]
        core_api.list_pod_for_all_namespaces.return_value = pod_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_pods(
                label_selector="app=payment", namespace=None
            )

        core_api.list_pod_for_all_namespaces.assert_called_once_with(label_selector="app=payment")
        core_api.list_namespaced_pod.assert_not_called()
        assert results[0]["name"] == "payment-pod-abc12"
        assert results[0]["node"] == "worker-1"
        assert results[0]["phase"] == "Running"
        assert results[0]["ready"] is True
        assert results[0]["kind"] == "pod"

    def test_namespaced_call_when_namespace_given(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        pod_list = MagicMock()
        pod_list.items = []
        core_api.list_namespaced_pod.return_value = pod_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            KubernetesLabelSearchAdapter().search_pods(
                label_selector="app=payment", namespace="production"
            )

        core_api.list_namespaced_pod.assert_called_once_with(
            namespace="production", label_selector="app=payment"
        )
        core_api.list_pod_for_all_namespaces.assert_not_called()

    def test_ready_false_when_any_container_not_ready(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        pod_list = MagicMock()
        pod_list.items = [
            _pod(
                name="payment-pod-def34",
                namespace="staging",
                phase="CrashLoopBackOff",
                container_ready=[False],
            )
        ]
        core_api.list_pod_for_all_namespaces.return_value = pod_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_pods(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["ready"] is False
        assert results[0]["phase"] == "CrashLoopBackOff"

    def test_ready_false_when_no_container_statuses(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        pod_list = MagicMock()
        pod_list.items = [_pod(container_ready=[])]
        core_api.list_pod_for_all_namespaces.return_value = pod_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_pods(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["ready"] is False

    def test_missing_labels_defaults_to_empty_dict(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        pod_list = MagicMock()
        pod_list.items = [_pod(labels=None)]
        core_api.list_pod_for_all_namespaces.return_value = pod_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_pods(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["labels"] == {}


class TestSearchDeployments:
    def test_returns_deployment_kind_with_no_pod_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        apps_api = MagicMock()
        dep_list = MagicMock()
        dep_list.items = [_non_pod("payment-deployment")]
        apps_api.list_deployment_for_all_namespaces.return_value = dep_list

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            results = KubernetesLabelSearchAdapter().search_deployments(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["kind"] == "deployment"
        assert results[0]["node"] is None
        assert results[0]["phase"] is None
        assert results[0]["ready"] is None

    def test_namespaced_call_when_namespace_given(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        apps_api = MagicMock()
        dep_list = MagicMock()
        dep_list.items = []
        apps_api.list_namespaced_deployment.return_value = dep_list

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            KubernetesLabelSearchAdapter().search_deployments(
                label_selector="app=payment", namespace="production"
            )

        apps_api.list_namespaced_deployment.assert_called_once_with(
            namespace="production", label_selector="app=payment"
        )
        apps_api.list_deployment_for_all_namespaces.assert_not_called()


class TestSearchServices:
    def test_returns_service_kind_with_no_pod_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        svc_list = MagicMock()
        svc_list.items = [_non_pod("payment-service")]
        core_api.list_service_for_all_namespaces.return_value = svc_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_services(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["kind"] == "service"
        assert results[0]["node"] is None

    def test_namespaced_call_when_namespace_given(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        svc_list = MagicMock()
        svc_list.items = []
        core_api.list_namespaced_service.return_value = svc_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            KubernetesLabelSearchAdapter().search_services(
                label_selector="app=payment", namespace="production"
            )

        core_api.list_namespaced_service.assert_called_once_with(
            namespace="production", label_selector="app=payment"
        )
        core_api.list_service_for_all_namespaces.assert_not_called()


class TestSearchConfigmaps:
    def test_returns_configmap_kind_with_no_pod_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        cm_list = MagicMock()
        cm_list.items = [_non_pod("payment-config")]
        core_api.list_config_map_for_all_namespaces.return_value = cm_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesLabelSearchAdapter().search_configmaps(
                label_selector="app=payment", namespace=None
            )

        assert results[0]["kind"] == "configmap"
        assert results[0]["phase"] is None

    def test_namespaced_call_when_namespace_given(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
            KubernetesLabelSearchAdapter,
        )

        core_api = MagicMock()
        cm_list = MagicMock()
        cm_list.items = []
        core_api.list_namespaced_config_map.return_value = cm_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            KubernetesLabelSearchAdapter().search_configmaps(
                label_selector="app=payment", namespace="production"
            )

        core_api.list_namespaced_config_map.assert_called_once_with(
            namespace="production", label_selector="app=payment"
        )
        core_api.list_config_map_for_all_namespaces.assert_not_called()
