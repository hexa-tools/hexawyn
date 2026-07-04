from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.adaptive_investigation_port import (
    AdaptiveInvestigationPort,
    ResourceInvestigationRawData,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_MAX_EVENTS_PER_RESOURCE = 5
_MAX_LOG_LINES_PER_RESOURCE = 20


class KubernetesAdaptiveInvestigationAdapter(AdaptiveInvestigationPort):
    """Secondary adapter — drills into a single failing resource: events,
    container logs, and restart/termination info (reads
    `last_state.terminated.reason` for OOMKilled detection, which none of the
    shallower overview/events/logs adapters read)."""

    def investigate_resource(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def _investigate_pod(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def _verify_deployment_exists(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def _fetch_events(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def _fetch_logs(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]


def _extract_container_status(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def _translate_error(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")
