from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.resource_search_port import (
    MatchedResourceRaw,
    ResourceSearchPort,
)

if TYPE_CHECKING:
    from kubernetes.client import V1ConfigMap, V1Deployment, V1Pod, V1Service


class KubernetesLabelSearchAdapter(ResourceSearchPort):
    """Secondary adapter — searches pods/deployments/services/configmaps by
    label selector, one `kubernetes` client call per resource kind."""

    def search_pods(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def search_deployments(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def search_services(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def search_configmaps(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]


def _to_pod_raw(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def _pod_ready(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if not statuses:
        return False
    return all(status.ready for status in statuses)


def _to_non_pod_raw(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )
