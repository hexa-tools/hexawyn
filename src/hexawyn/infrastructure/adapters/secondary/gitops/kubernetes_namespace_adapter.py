from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    HpaStatusRaw,
    NamespaceOverviewPort,
    NamespaceOverviewRawData,
    PodStatusRaw,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import V1Deployment, V1HorizontalPodAutoscaler, V1Pod

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


class KubernetesNamespaceAdapter(NamespaceOverviewPort):
    """Secondary adapter — one bulk fetch of pods/deployments/services/HPAs
    for a namespace, used to build a compact, conservative health overview."""

    def get_namespace_overview_data(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )


def _to_pod_status(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, status=_pod_status(pod))


def _pod_status(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "Unknown")


def _waiting_reason(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def _to_deployment_status(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def _to_hpa_status(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def _translate_namespace_error(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")
