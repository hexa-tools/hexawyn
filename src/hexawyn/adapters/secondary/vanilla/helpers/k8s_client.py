from __future__ import annotations

from typing import Protocol


class KubernetesCoreApi(Protocol):
    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List pods across all namespaces."""

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> object:
        """List pods in a namespace."""

    def list_node(self, timeout_seconds: int) -> object:
        """List cluster nodes."""

    def list_namespace(self, timeout_seconds: int) -> object:
        """List all namespaces."""


class KubernetesAppsApi(Protocol):
    def list_deployment_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all deployments across namespaces."""

    def list_stateful_set_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all stateful sets across namespaces."""


class KubernetesMetricsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""


class KubernetesCRDApi(Protocol):
    def list_namespaced_custom_object(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> object:
        """List namespace-scoped custom objects."""
