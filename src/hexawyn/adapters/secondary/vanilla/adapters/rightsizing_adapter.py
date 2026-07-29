from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesMetricsApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _sum_container_metrics,
    _workload_key_from_pod_name,
    _workload_resource_requests,
)
from hexawyn.application.ports.driven.rightsizing_port import (
    RightsizingPort,
    WorkloadRawData,
)
from hexawyn.domain.errors import ClusterUnreachableError

_K8S_TIMEOUT = 10
_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PODS_PLURAL = "pods"


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaRightsizingAdapter(RightsizingPort):
    def __init__(
        self,
        apps_api: KubernetesAppsApi,
        metrics_api: KubernetesMetricsApi,
    ) -> None:
        self._apps_api = apps_api
        self._metrics_api = metrics_api

    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def _fetch_deployments(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(raw))

    def _fetch_pod_metrics_by_workload(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def _build_workload_raw_data(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }
