from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypedDict


class ClusterUsageSnapshot(TypedDict):
    cpu_cores: float
    memory_gb: float


class ClusterDailyUsage(TypedDict):
    cpu_daily_cores: list[float]
    memory_daily_gb: list[float]


class NodeUtilizationSeries(TypedDict):
    cpu_percent_series: list[tuple[str, float]]
    memory_percent_series: list[tuple[str, float]]


class ClusterResourceMetricsPort(ABC):
    """Driven port: provider-agnostic cluster resource-usage metrics.

    Implemented by Prometheus (PromQL) and AWS CloudWatch Container Insights.
    Unlike MetricsQueryPort, this port never exposes a query language — it
    speaks in domain terms (cores, GiB, utilization %) so any observability
    backend can satisfy it.
    """

    @abstractmethod
    def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        """Return the current total cluster CPU (cores) and memory (GiB) usage.

        Raises MetricsUnavailableError when the backend is unreachable.
        """

    @abstractmethod
    def get_daily_usage(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        """Return the daily cluster CPU (cores) and memory (GiB) usage series.

        Raises MetricsUnavailableError when the backend is unreachable.
        """

    @abstractmethod
    def get_node_utilization(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        """Return per-node CPU and memory utilization (%) time series.

        Keyed by node name. Raises MetricsUnavailableError when unreachable.
        """
