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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _Series(Protocol):
    scope: str
    pointlist: Sequence[Sequence[float | None]]


class _QueryResponse(Protocol):
    series: Sequence[_Series] | None


class MetricsApi(Protocol):
    """Minimal contract for the Datadog v1 MetricsApi used here."""

    def query_metrics(self, *, _from: int, to: int, query: str) -> _QueryResponse: ...
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut: MutantDict = {}  # type: ignore


class DatadogClusterResourceMetricsAdapter(ClusterResourceMetricsPort):
    """ClusterResourceMetricsPort backed by the Datadog Metrics API.

    Datadog uses its own metric query language (not PromQL), so it implements
    the typed resource-metrics port rather than MetricsQueryPort. Read-only:
    only the metrics_read scope is required.
    """

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut)
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

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_orig(
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

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_1(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "XXXX",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_2(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "XXXX",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_3(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "XXdatadoghq.comXX",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_4(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "DATADOGHQ.COM",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_5(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = None
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_6(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = None
        self._app_key = app_key
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_7(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = None
        self._site = site

    def xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_8(
        self,
        metrics_api: MetricsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._metrics_api = metrics_api
        self._key = key
        self._app_key = app_key
        self._site = None

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut)
    def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_orig(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_1(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = None
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_2(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(None)
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_3(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = None
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_4(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end + _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_5(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = None
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_6(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(None, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_7(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, None, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_8(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, None)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_9(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_10(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_11(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, )
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_12(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = None
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_13(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(None, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_14(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, None, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_15(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, None)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_16(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_17(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_18(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, )
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_19(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "XXcpu_coresXX": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_20(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "CPU_CORES": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_21(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) * _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_22(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(None) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_23(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "XXmemory_gbXX": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_24(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "MEMORY_GB": _latest_value(memory_series) / _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_25(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(memory_series) * _BYTES_PER_GIB,
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_26(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        end = int(time.time())
        start = end - _INSTANT_WINDOW_SECONDS
        cpu_series = self._query(_CPU_CORES_QUERY, start, end)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start, end)
        return {
            "cpu_cores": _latest_value(cpu_series) / _NANOCORES_PER_CORE,
            "memory_gb": _latest_value(None) / _BYTES_PER_GIB,
        }

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut)
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_orig(
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_1(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = None
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_2(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(None)
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_3(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = None
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_4(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(None)
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_5(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = None
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_6(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(None, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_7(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, None, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_8(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, None)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_9(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_10(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_11(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, )
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_12(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = None
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_13(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(None, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_14(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, None, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_15(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, None)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_16(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_17(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_18(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, )
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_19(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "XXcpu_daily_coresXX": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_20(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "CPU_DAILY_CORES": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_21(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v * _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_22(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(None)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_23(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "XXmemory_daily_gbXX": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_24(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "MEMORY_DAILY_GB": [v / _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_25(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v * _BYTES_PER_GIB for v in _values(memory_series)],
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_26(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_series = self._query(_CPU_CORES_QUERY, start_ts, end_ts)
        memory_series = self._query(_MEMORY_BYTES_QUERY, start_ts, end_ts)
        return {
            "cpu_daily_cores": [v / _NANOCORES_PER_CORE for v in _values(cpu_series)],
            "memory_daily_gb": [v / _BYTES_PER_GIB for v in _values(None)],
        }

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut)
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_orig(
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_1(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = None
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_2(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(None)
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_3(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = None
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_4(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(None)
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

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_5(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = None
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_6(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(None)
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_7(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(None, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_8(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, None, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_9(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, None))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_10(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_11(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_12(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, ))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_13(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = None
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_14(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(None)
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_15(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(None, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_16(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, None, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_17(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, None))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_18(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_19(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_20(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, ))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_21(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = None
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_22(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) & set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_23(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(None) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_24(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(None)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_25(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "XXcpu_percent_seriesXX": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_26(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "CPU_PERCENT_SERIES": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_27(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(None, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_28(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, None),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_29(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get([]),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_30(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        start_ts = int(start.timestamp())
        end_ts = int(end.timestamp())
        cpu_by_node = _series_by_host(self._query(_CPU_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        memory_by_node = _series_by_host(self._query(_MEMORY_UTIL_BY_NODE_QUERY, start_ts, end_ts))
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, ),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_31(
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
                "XXmemory_percent_seriesXX": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_32(
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
                "MEMORY_PERCENT_SERIES": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_33(
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
                "memory_percent_series": memory_by_node.get(None, []),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_34(
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
                "memory_percent_series": memory_by_node.get(node, None),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_35(
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
                "memory_percent_series": memory_by_node.get([]),
            }
            for node in node_names
        }

    def xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_36(
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
                "memory_percent_series": memory_by_node.get(node, ),
            }
            for node in node_names
        }

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut)
    def _query(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_orig(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_1(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = None
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_2(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=None, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_3(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=None, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_4(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=None)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_5(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_6(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_7(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, )
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_8(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(None) from exc
        return list(response.series or [])

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_9(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(None)

    def xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_10(self, query: str, start: int, end: int) -> list[_Series]:
        from datadog_api_client.exceptions import ApiException

        try:
            response = self._api().query_metrics(_from=start, to=end, query=query)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.series and [])

    @_mutmut_mutated(mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut)
    def _api(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_orig(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_1(self) -> MetricsApi:
        if self._metrics_api is not None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_2(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = None
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_3(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(None, self._app_key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_4(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, None, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_5(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, None)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_6(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._app_key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_7(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._site)
        return self._metrics_api

    def xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_8(self) -> MetricsApi:
        if self._metrics_api is None:
            self._metrics_api = _build_metrics_api(self._key, self._app_key, )
        return self._metrics_api

mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut['xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_9'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_10'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_11'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_12'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_13'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_14'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_15'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_16'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_17'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_18'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_19'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_20'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_21'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_22'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_23'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_24'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_25'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_26'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_current_usage__mutmut_26 # type: ignore # mutmut generated

mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_9'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_10'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_11'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_12'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_13'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_14'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_15'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_16'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_17'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_18'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_19'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_20'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_21'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_22'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_23'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_24'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_25'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_26'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_daily_usage__mutmut_26 # type: ignore # mutmut generated

mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_9'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_10'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_11'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_12'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_13'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_14'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_15'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_16'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_17'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_18'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_19'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_20'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_21'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_22'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_23'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_24'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_25'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_26'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_27'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_28'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_29'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_30'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_31'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_32'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_33'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_34'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_35'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut['xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_36'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁget_node_utilization__mutmut_36 # type: ignore # mutmut generated

mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_9'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_10'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_query__mutmut_10 # type: ignore # mutmut generated

mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['_mutmut_orig'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_1'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_2'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_3'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_4'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_5'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_6'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_7'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut['xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_8'] = DatadogClusterResourceMetricsAdapter.xǁDatadogClusterResourceMetricsAdapterǁ_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
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


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
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


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
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


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
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


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
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


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
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


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
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


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
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


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
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


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(None, context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context=None)
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", )
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("XXDatadog rate limit reached.XX", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_15(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_16(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("DATADOG RATE LIMIT REACHED.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_17(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"XXstatusXX": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_18(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"STATUS": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_19(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(None)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_20(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status not in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_21(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            None,
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_22(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context=None,
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_23(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_24(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_25(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"XXstatusXX": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_26(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"STATUS": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_27(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(None)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_28(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        None, context={"status": str(status)}
    )


def x__translate_error__mutmut_29(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context=None
    )


def x__translate_error__mutmut_30(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        context={"status": str(status)}
    )


def x__translate_error__mutmut_31(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", )


def x__translate_error__mutmut_32(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "XXDatadog Metrics API request failed.XX", context={"status": str(status)}
    )


def x__translate_error__mutmut_33(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "datadog metrics api request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_34(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "DATADOG METRICS API REQUEST FAILED.", context={"status": str(status)}
    )


def x__translate_error__mutmut_35(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"XXstatusXX": str(status)}
    )


def x__translate_error__mutmut_36(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"STATUS": str(status)}
    )


def x__translate_error__mutmut_37(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            f"Datadog API rejected the credentials. {_CREDENTIALS_HINT}",
            context={"status": str(status)},
        )
    return MetricsUnavailableError(
        "Datadog Metrics API request failed.", context={"status": str(None)}
    )

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_24'] = x__translate_error__mutmut_24 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_25'] = x__translate_error__mutmut_25 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_26'] = x__translate_error__mutmut_26 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_27'] = x__translate_error__mutmut_27 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_28'] = x__translate_error__mutmut_28 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_29'] = x__translate_error__mutmut_29 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_30'] = x__translate_error__mutmut_30 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_31'] = x__translate_error__mutmut_31 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_32'] = x__translate_error__mutmut_32 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_33'] = x__translate_error__mutmut_33 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_34'] = x__translate_error__mutmut_34 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_35'] = x__translate_error__mutmut_35 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_36'] = x__translate_error__mutmut_36 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_37'] = x__translate_error__mutmut_37 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__latest_value__mutmut)
def _latest_value(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_orig(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_1(series: list[_Series]) -> float:
    if series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_2(series: list[_Series]) -> float:
    if not series:
        return 1.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_3(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = None
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_4(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[+1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_5(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-2] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_6(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[1].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_7(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point or point[-1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_8(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[+1] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_9(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-2] is not None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_10(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is None]
    return float(values[-1]) if values else 0.0


def x__latest_value__mutmut_11(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(None) if values else 0.0


def x__latest_value__mutmut_12(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[+1]) if values else 0.0


def x__latest_value__mutmut_13(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-2]) if values else 0.0


def x__latest_value__mutmut_14(series: list[_Series]) -> float:
    if not series:
        return 0.0
    values = [point[-1] for point in series[0].pointlist if point and point[-1] is not None]
    return float(values[-1]) if values else 1.0

mutants_x__latest_value__mutmut['_mutmut_orig'] = x__latest_value__mutmut_orig # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_1'] = x__latest_value__mutmut_1 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_2'] = x__latest_value__mutmut_2 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_3'] = x__latest_value__mutmut_3 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_4'] = x__latest_value__mutmut_4 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_5'] = x__latest_value__mutmut_5 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_6'] = x__latest_value__mutmut_6 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_7'] = x__latest_value__mutmut_7 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_8'] = x__latest_value__mutmut_8 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_9'] = x__latest_value__mutmut_9 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_10'] = x__latest_value__mutmut_10 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_11'] = x__latest_value__mutmut_11 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_12'] = x__latest_value__mutmut_12 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_13'] = x__latest_value__mutmut_13 # type: ignore # mutmut generated
mutants_x__latest_value__mutmut['x__latest_value__mutmut_14'] = x__latest_value__mutmut_14 # type: ignore # mutmut generated
mutants_x__values__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__values__mutmut)
def _values(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_orig(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_1(series: list[_Series]) -> list[float]:
    if series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_2(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(None) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_3(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[+1]) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_4(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-2]) for point in series[0].pointlist if point and point[-1] is not None]


def x__values__mutmut_5(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[1].pointlist if point and point[-1] is not None]


def x__values__mutmut_6(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point or point[-1] is not None]


def x__values__mutmut_7(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[+1] is not None]


def x__values__mutmut_8(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-2] is not None]


def x__values__mutmut_9(series: list[_Series]) -> list[float]:
    if not series:
        return []
    return [float(point[-1]) for point in series[0].pointlist if point and point[-1] is None]

mutants_x__values__mutmut['_mutmut_orig'] = x__values__mutmut_orig # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_1'] = x__values__mutmut_1 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_2'] = x__values__mutmut_2 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_3'] = x__values__mutmut_3 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_4'] = x__values__mutmut_4 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_5'] = x__values__mutmut_5 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_6'] = x__values__mutmut_6 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_7'] = x__values__mutmut_7 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_8'] = x__values__mutmut_8 # type: ignore # mutmut generated
mutants_x__values__mutmut['x__values__mutmut_9'] = x__values__mutmut_9 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__series_by_host__mutmut)
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


def x__series_by_host__mutmut_orig(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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


def x__series_by_host__mutmut_1(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = None
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


def x__series_by_host__mutmut_2(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = None
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


def x__series_by_host__mutmut_3(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(None)
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


def x__series_by_host__mutmut_4(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = None
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


def x__series_by_host__mutmut_5(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if point:
                continue
            timestamp = point[0]
            value = point[-1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_6(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                break
            timestamp = point[0]
            value = point[-1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_7(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = None
            value = point[-1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_8(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[1]
            value = point[-1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_9(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = None
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_10(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[+1]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_11(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[-2]
            if timestamp is None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_12(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[-1]
            if timestamp is None and value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_13(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[-1]
            if timestamp is not None or value is None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_14(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for one in series:
        host = _host_from_scope(one.scope)
        points: list[tuple[str, float]] = []
        for point in one.pointlist:
            if not point:
                continue
            timestamp = point[0]
            value = point[-1]
            if timestamp is None or value is not None:
                continue
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_15(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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
                break
            points.append((_ts_to_iso(timestamp), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_16(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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
            points.append(None)
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_17(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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
            points.append((_ts_to_iso(None), float(value)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_18(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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
            points.append((_ts_to_iso(timestamp), float(None)))
        grouped[host] = points
    return grouped


def x__series_by_host__mutmut_19(series: list[_Series]) -> dict[str, list[tuple[str, float]]]:
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
        grouped[host] = None
    return grouped

mutants_x__series_by_host__mutmut['_mutmut_orig'] = x__series_by_host__mutmut_orig # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_1'] = x__series_by_host__mutmut_1 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_2'] = x__series_by_host__mutmut_2 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_3'] = x__series_by_host__mutmut_3 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_4'] = x__series_by_host__mutmut_4 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_5'] = x__series_by_host__mutmut_5 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_6'] = x__series_by_host__mutmut_6 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_7'] = x__series_by_host__mutmut_7 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_8'] = x__series_by_host__mutmut_8 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_9'] = x__series_by_host__mutmut_9 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_10'] = x__series_by_host__mutmut_10 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_11'] = x__series_by_host__mutmut_11 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_12'] = x__series_by_host__mutmut_12 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_13'] = x__series_by_host__mutmut_13 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_14'] = x__series_by_host__mutmut_14 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_15'] = x__series_by_host__mutmut_15 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_16'] = x__series_by_host__mutmut_16 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_17'] = x__series_by_host__mutmut_17 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_18'] = x__series_by_host__mutmut_18 # type: ignore # mutmut generated
mutants_x__series_by_host__mutmut['x__series_by_host__mutmut_19'] = x__series_by_host__mutmut_19 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__host_from_scope__mutmut)
def _host_from_scope(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_orig(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_1(scope: str) -> str:
    for tag in str(scope).split(None):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_2(scope: str) -> str:
    for tag in str(None).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_3(scope: str) -> str:
    for tag in str(scope).split("XX,XX"):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_4(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = None
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_5(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith(None):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_6(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("XXhost:XX"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_7(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("HOST:"):
            return cleaned[len("host:") :]
    return "unknown"


def x__host_from_scope__mutmut_8(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "XXunknownXX"


def x__host_from_scope__mutmut_9(scope: str) -> str:
    for tag in str(scope).split(","):
        cleaned = tag.strip()
        if cleaned.startswith("host:"):
            return cleaned[len("host:") :]
    return "UNKNOWN"

mutants_x__host_from_scope__mutmut['_mutmut_orig'] = x__host_from_scope__mutmut_orig # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_1'] = x__host_from_scope__mutmut_1 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_2'] = x__host_from_scope__mutmut_2 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_3'] = x__host_from_scope__mutmut_3 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_4'] = x__host_from_scope__mutmut_4 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_5'] = x__host_from_scope__mutmut_5 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_6'] = x__host_from_scope__mutmut_6 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_7'] = x__host_from_scope__mutmut_7 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_8'] = x__host_from_scope__mutmut_8 # type: ignore # mutmut generated
mutants_x__host_from_scope__mutmut['x__host_from_scope__mutmut_9'] = x__host_from_scope__mutmut_9 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__ts_to_iso__mutmut)
def _ts_to_iso(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_orig(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_1(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace(None, "Z")


def x__ts_to_iso__mutmut_2(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", None)


def x__ts_to_iso__mutmut_3(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("Z")


def x__ts_to_iso__mutmut_4(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", )


def x__ts_to_iso__mutmut_5(epoch_millis: float) -> str:
    return datetime.fromtimestamp(None, tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_6(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=None).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_7(epoch_millis: float) -> str:
    return datetime.fromtimestamp(tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_8(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, ).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_9(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis * 1000, tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_10(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1001, tz=UTC).isoformat().replace("+00:00", "Z")


def x__ts_to_iso__mutmut_11(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("XX+00:00XX", "Z")


def x__ts_to_iso__mutmut_12(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", "XXZXX")


def x__ts_to_iso__mutmut_13(epoch_millis: float) -> str:
    return datetime.fromtimestamp(epoch_millis / 1000, tz=UTC).isoformat().replace("+00:00", "z")

mutants_x__ts_to_iso__mutmut['_mutmut_orig'] = x__ts_to_iso__mutmut_orig # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_1'] = x__ts_to_iso__mutmut_1 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_2'] = x__ts_to_iso__mutmut_2 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_3'] = x__ts_to_iso__mutmut_3 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_4'] = x__ts_to_iso__mutmut_4 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_5'] = x__ts_to_iso__mutmut_5 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_6'] = x__ts_to_iso__mutmut_6 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_7'] = x__ts_to_iso__mutmut_7 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_8'] = x__ts_to_iso__mutmut_8 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_9'] = x__ts_to_iso__mutmut_9 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_10'] = x__ts_to_iso__mutmut_10 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_11'] = x__ts_to_iso__mutmut_11 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_12'] = x__ts_to_iso__mutmut_12 # type: ignore # mutmut generated
mutants_x__ts_to_iso__mutmut['x__ts_to_iso__mutmut_13'] = x__ts_to_iso__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_metrics_api__mutmut)
def _build_metrics_api(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_orig(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_1(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = None
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_2(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = None
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_3(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["XXapiKeyAuthXX"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_4(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apikeyauth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_5(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["APIKEYAUTH"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_6(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = None
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_7(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["XXappKeyAuthXX"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_8(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appkeyauth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_9(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["APPKEYAUTH"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_10(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = None
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_11(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["XXsiteXX"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_12(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["SITE"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_13(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(None, DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_14(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, None)


def x__build_metrics_api__mutmut_15(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(DatadogMetricsApi(ApiClient(configuration)))


def x__build_metrics_api__mutmut_16(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, )


def x__build_metrics_api__mutmut_17(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(None))


def x__build_metrics_api__mutmut_18(key: str, app_key: str, site: str) -> MetricsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.metrics_api import MetricsApi as DatadogMetricsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MetricsApi, DatadogMetricsApi(ApiClient(None)))

mutants_x__build_metrics_api__mutmut['_mutmut_orig'] = x__build_metrics_api__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_1'] = x__build_metrics_api__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_2'] = x__build_metrics_api__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_3'] = x__build_metrics_api__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_4'] = x__build_metrics_api__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_5'] = x__build_metrics_api__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_6'] = x__build_metrics_api__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_7'] = x__build_metrics_api__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_8'] = x__build_metrics_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_9'] = x__build_metrics_api__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_10'] = x__build_metrics_api__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_11'] = x__build_metrics_api__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_12'] = x__build_metrics_api__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_13'] = x__build_metrics_api__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_14'] = x__build_metrics_api__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_15'] = x__build_metrics_api__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_16'] = x__build_metrics_api__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_17'] = x__build_metrics_api__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_metrics_api__mutmut['x__build_metrics_api__mutmut_18'] = x__build_metrics_api__mutmut_18 # type: ignore # mutmut generated
