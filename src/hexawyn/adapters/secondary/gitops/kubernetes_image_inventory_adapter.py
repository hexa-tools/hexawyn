from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.image_inventory_port import (
    ImageInventoryPort,
    RunningImageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


class KubernetesImageInventoryAdapter(ImageInventoryPort):
    """Secondary adapter — enumerates every unique container image currently
    running in the cluster, covering init, regular, and ephemeral containers."""

    def list_running_images(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images


def _to_running_images(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")
