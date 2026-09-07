from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.image_drift_port import (
    ImageDriftPort,
    ResolvedContainerImageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


class KubernetesImageDriftAdapter(ImageDriftPort):
    """Secondary adapter — resolves each running container's actually-pulled
    image digest (`pod.status.containerStatuses[].imageID`, populated by the
    kubelet after every successful pull, no registry auth needed to read it)
    by joining Pods to their owning Deployment via label-selector match."""

    def list_resolved_container_images(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results


def _match_labels(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def _matches_selector(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")
