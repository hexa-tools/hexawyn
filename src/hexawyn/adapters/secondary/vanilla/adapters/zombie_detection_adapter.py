from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _compute_pod_resources,
)
from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.domain.errors import ClusterUnreachableError

_K8S_TIMEOUT = 10


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaZombieDetectionAdapter(ZombieDetectionPort):
    def __init__(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache or []

    def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result
