from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_MAX_TAIL_LINES = 5000


class KubernetesPodLogSearchAdapter(LogSearchPort):
    """Secondary adapter — reads every container's logs for one pod, tail-
    truncated server-side (`tail_lines`) since this feature scans every pod
    in the cluster, unlike the single-pod `analyze_pod_logs` adapter."""

    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def _read_container_log(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )


def _translate_pod_error(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")
