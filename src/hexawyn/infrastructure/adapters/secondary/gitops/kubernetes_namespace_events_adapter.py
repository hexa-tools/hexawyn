from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


class KubernetesNamespaceEventsAdapter(NamespaceEventsPort):
    """Secondary adapter — reads namespace-wide events from the Kubernetes API
    (core_v1.list_namespaced_event)."""

    def list_events(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def _to_namespace_event(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )


def _object_exists(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def _translate_error(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")
