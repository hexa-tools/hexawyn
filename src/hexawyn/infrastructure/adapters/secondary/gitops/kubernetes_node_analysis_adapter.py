from __future__ import annotations

from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
    NodeInfoRaw,
    PodUsageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_BYTES_PER_GB = 1024.0**3
_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PLURAL = "pods"


class KubernetesNodeAnalysisAdapter(HotNodeAnalysisPort):
    """Secondary adapter — node allocatable/cordon status and cluster-wide
    pod usage joined to node assignment + DaemonSet ownership. Per-node
    utilization history comes from the existing MetricsQueryPort (ECA-31),
    not this adapter."""

    def list_nodes(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def list_pod_usage(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results


def _fetch_pod_metrics(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def _is_daemonset(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def _node_allocatable(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def _node_allocatable_cpu(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", "0")))


def _node_allocatable_memory_gb(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", "0"))) / _BYTES_PER_GB


def _cpu_to_cores(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def _memory_to_bytes(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def _float_prefix(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def _safe_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")
