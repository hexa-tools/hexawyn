from __future__ import annotations

import time
from collections.abc import Sequence
from datetime import UTC, datetime
from typing import Protocol, cast

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterDailyUsage,
    ClusterResourceMetricsPort,
    ClusterUsageSnapshot,
    NodeUtilizationSeries,
)
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)

_NANOCORES_PER_CORE = 1_000_000_000.0
_BYTES_PER_GIB = float(1024**3)
_INSTANT_WINDOW_SECONDS = 300
_RATE_LIMIT_STATUS = 429
_UNAUTHORIZED_STATUSES = (401, 403)
_CREDENTIALS_HINT = "Check the Datadog API/application keys and required read scopes."

# Datadog metric queries mapped to hexawyn's provider-agnostic domain.
_CPU_CORES_QUERY = "sum:kubernetes.cpu.usage.total{*}"
_MEMORY_BYTES_QUERY = "sum:kubernetes.memory.usage{*}"
_CPU_UTIL_BY_NODE_QUERY = (
    "(sum:kubernetes.cpu.usage.total{*} by {host} / 1000000000 "
    "/ avg:kubernetes.cpu.capacity{*} by {host}) * 100"
)
_MEMORY_UTIL_BY_NODE_QUERY = (
    "(avg:kubernetes.memory.usage{*} by {host} / avg:kubernetes.memory.capacity{*} by {host}) * 100"
)


class _Series(Protocol):
    scope: str
    pointlist: Sequence[Sequence[float | None]]


class _QueryResponse(Protocol):
    series: Sequence[_Series] | None


class MetricsApi(Protocol):
    """Minimal contract for the Datadog v1 MetricsApi used here."""

    def query_metrics(self, *, _from: int, to: int, query: str) -> _QueryResponse: ...


class DatadogClusterResourceMetricsAdapter(ClusterResourceMetricsPort):
    """ClusterResourceMetricsPort backed by the Datadog Metrics API.

    Datadog uses its own metric query language (not PromQL), so it implements
    the typed resource-metrics port rather than MetricsQueryPort. Read-only:
    only the metrics_read scope is required.
    """

    def __init__(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def get_daily_usage(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def get_node_utilization(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def _query(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def _api(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, self._site)
        return self._metrics_api


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def _latest_value(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def _values(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-1] is not None]


def _series_by_host(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[-1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def _host_from_scope(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def _ts_to_iso(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", "Z")


def _build_metrics_api(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))
