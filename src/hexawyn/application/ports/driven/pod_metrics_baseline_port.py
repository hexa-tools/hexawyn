from abc import ABC, abstractmethod
from typing import TypedDict


class PodMetricsRawData(TypedDict):
    """Raw per-pod CPU/memory/error-rate baseline + current usage — one entry
    per pod, already assembled from K8s (pod age) and Prometheus (metrics)."""

    pod_name: str
    namespace: str
    pod_age_hours: float
    hours_since_last_restart: float | None
    baseline_window_hours: float
    cpu_baseline_millicores: list[float]
    cpu_current_millicores: float
    memory_baseline_bytes: list[float]
    memory_current_bytes: float
    error_rate_baseline_pct: list[float]
    error_rate_current_pct: float
    is_scheduled_batch_job: bool


class PodMetricsBaselinePort(ABC):
    """Driven port: provides current + 7-day-baseline CPU/memory/error-rate
    usage for every pod in a namespace."""

    @abstractmethod
    def get_all_pod_metrics_data(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        """Fetch baseline + current metrics for all pods in the namespace.

        Returns an entry per currently-existing pod.
        Raises PrometheusUnavailableError when Prometheus is unreachable.
        Raises PrometheusQueryError when a metrics query is rejected.
        Raises AdapterTimeoutError when a metrics query exceeds its timeout.
        Raises ClusterUnreachableError when the K8s API cannot be reached.
        """
