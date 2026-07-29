from __future__ import annotations

from collections.abc import Sequence
from datetime import UTC, datetime
from typing import cast

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _container_request,
    _parse_prometheus_vector,
    _pod_containers,
    _pod_namespace,
)
from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceRawData,
    NamespaceWasteAnalysisPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    PrometheusUnavailableError,
)

_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0
_CPU_USAGE_QUERY = (
    "avg_over_time("
    "sum by (namespace) (rate(container_cpu_usage_seconds_total{{container!=''}}[5m]))"
    "[{window}d:1h])"
)
_MEM_USAGE_QUERY = (
    "avg_over_time("
    "sum by (namespace) (container_memory_working_set_bytes{{container!=''}})"
    "[{window}d:1h])"
)


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaNamespaceWasteAdapter(NamespaceWasteAnalysisPort):
    def __init__(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url

    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        namespace_ages = self._fetch_namespace_ages()
        cpu_requests = self._fetch_k8s_resource_requests("cpu")
        mem_requests = self._fetch_k8s_resource_requests("memory")
        cpu_usage = self._fetch_prometheus_usage(_CPU_USAGE_QUERY.format(window=window_days))
        mem_usage = self._fetch_prometheus_usage(_MEM_USAGE_QUERY.format(window=window_days))
        all_namespaces = namespace_ages.keys() | cpu_requests.keys() | mem_requests.keys()
        return [
            self._build_namespace_raw_data(
                ns, namespace_ages, cpu_requests, mem_requests, cpu_usage, mem_usage
            )
            for ns in sorted(all_namespaces)
        ]

    def _build_namespace_raw_data(  # noqa: PLR0913
        self,
        namespace: str,
        ages: dict[str, float],
        cpu_req: dict[str, float],
        mem_req: dict[str, float],
        cpu_usage: dict[str, float],
        mem_usage: dict[str, float],
    ) -> NamespaceRawData:
        cpu_requested = cpu_req.get(namespace)
        mem_requested = mem_req.get(namespace)
        return {
            "namespace": namespace,
            "cpu_requested_cores": cpu_requested,
            "memory_requested_gb": mem_requested,
            "cpu_actual_avg_cores": cpu_usage.get(namespace),
            "memory_actual_avg_gb": mem_usage.get(namespace),
            "age_hours": ages.get(namespace, 999.0),
            "has_resource_requests": cpu_requested is not None or mem_requested is not None,
        }

    def _fetch_namespace_ages(self) -> dict[str, float]:
        try:
            raw = self._api.list_namespace(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        ages: dict[str, float] = {}
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            if meta is None:
                continue
            name = getattr(meta, "name", None) or ""
            creation = getattr(meta, "creation_timestamp", None)
            if name and creation:
                elapsed = (datetime.now(UTC) - creation).total_seconds()
                ages[name] = elapsed / 3600.0
        return ages

    def _fetch_k8s_resource_requests(self, resource: str) -> dict[str, float]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods: {exc}") from exc
        totals: dict[str, float] = {}
        for pod in _items_from(raw):
            namespace = _pod_namespace(pod)
            if not namespace:
                continue
            for container in _pod_containers(pod):
                value = _container_request(container, resource)
                if value is not None:
                    totals[namespace] = totals.get(namespace, 0.0) + value
        return totals

    def _fetch_prometheus_usage(self, query: str) -> dict[str, float]:
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
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._prometheus_url) from exc
        except Exception as exc:
            raise PrometheusUnavailableError(self._prometheus_url) from exc
        return _parse_prometheus_vector(resp.json())
