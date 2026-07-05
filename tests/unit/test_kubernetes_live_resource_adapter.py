from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _deployment(
    name: str = "payment-service",
    namespace: str = "production",
    labels: dict | None = None,
    annotations: dict | None = None,
) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.metadata.labels = labels or {}
    dep.metadata.annotations = annotations or {}
    dep.to_dict.return_value = {
        "metadata": {"name": name, "namespace": namespace, "labels": labels or {}},
        "spec": {"replicas": 3, "template": {"spec": {"containers": [{"image": "payment:v1.2"}]}}},
    }
    return dep


def _configmap(name: str = "app-config", namespace: str = "production") -> MagicMock:
    cm = MagicMock()
    cm.metadata.name = name
    cm.metadata.namespace = namespace
    cm.metadata.labels = {}
    cm.metadata.annotations = {"meta.helm.sh/release-name": "app-chart"}
    cm.to_dict.return_value = {
        "metadata": {"name": name, "namespace": namespace},
        "data": {"log_level": "info"},
    }
    return cm


def _list(*items: MagicMock) -> MagicMock:
    result = MagicMock()
    result.items = list(items)
    return result


class TestKubernetesLiveResourceAdapterIsPort:
    def test_is_live_resource_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        assert isinstance(KubernetesLiveResourceAdapter(), LiveResourcePort)


class TestListLiveResources:
    def test_returns_deployments_and_configmaps_with_labels_and_annotations(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list(
            _deployment(
                labels={"app": "payment"},
                annotations={"meta.helm.sh/release-name": "payment-chart"},
            )
        )
        core_api = MagicMock()
        core_api.list_namespaced_config_map.return_value = _list(_configmap())

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesLiveResourceAdapter()
            resources = adapter.list_live_resources("production")

        assert len(resources) == 2
        by_kind = {r["kind"]: r for r in resources}
        assert by_kind["Deployment"]["name"] == "payment-service"
        assert by_kind["Deployment"]["labels"] == {"app": "payment"}
        assert by_kind["Deployment"]["annotations"] == {
            "meta.helm.sh/release-name": "payment-chart"
        }
        assert by_kind["Deployment"]["data"]["spec"]["replicas"] == 3
        assert by_kind["ConfigMap"]["name"] == "app-config"
        assert by_kind["ConfigMap"]["annotations"] == {"meta.helm.sh/release-name": "app-chart"}

    def test_empty_namespace_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list()
        core_api = MagicMock()
        core_api.list_namespaced_config_map.return_value = _list()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesLiveResourceAdapter()
            resources = adapter.list_live_resources("empty-namespace")

        assert resources == []

    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        apps_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        apps_api.list_namespaced_deployment.side_effect = forbidden

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            adapter = KubernetesLiveResourceAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_live_resources("production")

    def test_other_errors_translate_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.side_effect = Exception("connection reset")

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            adapter = KubernetesLiveResourceAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_live_resources("production")

    def test_configmap_forbidden_also_translates(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
            KubernetesLiveResourceAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list()
        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_namespaced_config_map.side_effect = forbidden

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesLiveResourceAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_live_resources("production")
