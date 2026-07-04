from __future__ import annotations

from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomCapacityInfoRaw,
    HeadroomSimulationPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUTOSCALER_NAME_HINT = "cluster-autoscaler"
_BYTES_PER_GB = 1024.0**3
_KUBE_SYSTEM_NAMESPACE = "kube-system"


class KubernetesHeadroomSimulationAdapter(HeadroomSimulationPort):
    """Secondary adapter — node-allocatable totals, node count, largest
    single node's capacity, and cluster-autoscaler presence. Narrower than
    (and independent of) `KubernetesCapacityForecastAdapter` (ECA-74), which
    only exposes summed totals — this feature additionally needs per-node
    granularity, so the quantity parsing is reimplemented locally rather than
    imported cross-adapter (no shared quantity-parser module in this
    codebase, confirmed twice already)."""

    def get_node_capacity_info(self) -> HeadroomCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        per_node_cpu = [_node_allocatable_cpu(node) for node in node_list.items]
        per_node_memory_gb = [_node_allocatable_memory_gb(node) for node in node_list.items]

        return HeadroomCapacityInfoRaw(
            total_allocatable_cpu_cores=sum(per_node_cpu),
            total_allocatable_memory_gb=sum(per_node_memory_gb),
            node_count=len(node_list.items),
            largest_node_cpu_cores=max(per_node_cpu, default=0.0),
            largest_node_memory_gb=max(per_node_memory_gb, default=0.0),
            autoscaler_enabled=_detect_autoscaler(k8s),
        )


def _detect_autoscaler(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


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
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")
