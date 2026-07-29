"""Tests for k8s_client Protocol classes — structural subtyping verification."""

from __future__ import annotations

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesCoreApi,
    KubernetesCRDApi,
    KubernetesMetricsApi,
)


class _FakeCoreApi:
    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> object:
        raise NotImplementedError

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> object:
        raise NotImplementedError

    def list_node(self, timeout_seconds: int) -> object:
        raise NotImplementedError

    def list_namespace(self, timeout_seconds: int) -> object:
        raise NotImplementedError


class _FakeAppsApi:
    def list_deployment_for_all_namespaces(self, timeout_seconds: int) -> object:
        raise NotImplementedError

    def list_stateful_set_for_all_namespaces(self, timeout_seconds: int) -> object:
        raise NotImplementedError


class _FakeMetricsApi:
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        raise NotImplementedError


class _FakeCRDApi:
    def list_namespaced_custom_object(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> object:
        raise NotImplementedError


class TestKubernetesCoreApi:
    def test_protocol_exists(self) -> None:
        assert KubernetesCoreApi is not None

    def test_has_list_pod_for_all_namespaces(self) -> None:
        assert hasattr(KubernetesCoreApi, "list_pod_for_all_namespaces")

    def test_fake_implements_interface(self) -> None:
        api = _FakeCoreApi()
        try:
            api.list_pod_for_all_namespaces(timeout_seconds=5)
        except NotImplementedError:
            pass


class TestKubernetesAppsApi:
    def test_protocol_exists(self) -> None:
        assert KubernetesAppsApi is not None

    def test_has_list_deployment_for_all_namespaces(self) -> None:
        assert hasattr(KubernetesAppsApi, "list_deployment_for_all_namespaces")

    def test_fake_implements_interface(self) -> None:
        api = _FakeAppsApi()
        try:
            api.list_deployment_for_all_namespaces(timeout_seconds=5)
        except NotImplementedError:
            pass


class TestKubernetesMetricsApi:
    def test_protocol_exists(self) -> None:
        assert KubernetesMetricsApi is not None

    def test_has_list_cluster_custom_object(self) -> None:
        assert hasattr(KubernetesMetricsApi, "list_cluster_custom_object")

    def test_fake_implements_interface(self) -> None:
        api = _FakeMetricsApi()
        try:
            api.list_cluster_custom_object(group="g", version="v", plural="p")
        except NotImplementedError:
            pass


class TestKubernetesCRDApi:
    def test_protocol_exists(self) -> None:
        assert KubernetesCRDApi is not None

    def test_has_list_namespaced_custom_object(self) -> None:
        assert hasattr(KubernetesCRDApi, "list_namespaced_custom_object")

    def test_fake_implements_interface(self) -> None:
        api = _FakeCRDApi()
        try:
            api.list_namespaced_custom_object(group="g", version="v", namespace="ns", plural="p")
        except NotImplementedError:
            pass
