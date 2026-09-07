"""KubernetesPodResourceAdapter — combines pod spec limits with Metrics API usage."""

from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import (
    ContainerMetricsRecord,
    PodResourceMetricsPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)

_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PLURAL = "pods"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


class KubernetesPodResourceAdapter(PodResourceMetricsPort):
    """Secondary adapter — reads pod resource limits and live usage from K8s."""

    def list_container_resources(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def _fetch_pod_limits(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def _fetch_metrics(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage


# ── Helpers ────────────────────────────────────────────────────────────────


def _parse_cpu(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


def _parse_memory(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def _merge(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records
