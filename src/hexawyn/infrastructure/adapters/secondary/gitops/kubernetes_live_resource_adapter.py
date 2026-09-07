from __future__ import annotations

from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort, LiveResourceRaw
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


class KubernetesLiveResourceAdapter(LiveResourcePort):
    """Secondary adapter — lists live Deployments and ConfigMaps, extracting
    labels and annotations. `to_dict()`'s output is directly compatible
    with field_comparison.py's extractors — none of the specific paths this
    feature reads (image/env/replicas/limits/labels/data) differ between
    raw K8s YAML and the client's snake_case conversion."""

    def list_live_resources(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]


def _to_live_resource(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")
