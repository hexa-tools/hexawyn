from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from kubernetes import client

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _deployment_key_from_pod,
    _parse_prometheus_pod_vector,
    _pod_requests_and_limits,
)
from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
    PodResourceData,
)
from hexawyn.domain.errors import ClusterUnreachableError

_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0
_POD_CPU_P95_QUERY = (
    "quantile_over_time(0.95,"
    " sum by (pod, namespace) (rate(container_cpu_usage_seconds_total{container!=''}[5m]))"
    "[7d:1h])"
)
_POD_MEM_P95_QUERY = (
    "quantile_over_time(0.95,"
    " sum by (pod, namespace) (container_memory_working_set_bytes{container!=''})"
    "[7d:1h]) / (1024 * 1024)"
)
_POD_CPU_MAX_QUERY = (
    "max_over_time("
    " sum by (pod, namespace) (rate(container_cpu_usage_seconds_total{container!=''}[5m]))"
    "[7d:1h])"
)


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaCostSavingAdapter(CostSavingEstimationPort):
    def __init__(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url

    def get_pod_resource_data(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def _fetch_hpa_map(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def _fetch_pod_prometheus_map(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def get_previous_total_saving(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def store_total_saving(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass
