from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class ContainerMetricsRecord(TypedDict):
    container_name: str
    pod_name: str
    namespace: str
    cpu_usage_millicores: int
    cpu_limit_millicores: int | None
    memory_usage_bytes: int
    memory_limit_bytes: int | None
    is_init_container: bool


class PodResourceMetricsPort(ABC):
    """Outbound port — fetches pod resource usage and limits from the cluster."""

    @abstractmethod
    def list_container_resources(self, namespace: str) -> list[ContainerMetricsRecord]:
        """Return per-container CPU/memory usage and limits for *namespace*.

        Raises InsufficientPermissionsError on RBAC 403.
        Raises MetricsUnavailableError when the metrics-server is absent (404).
        Raises ClusterUnreachableError on other API failures.
        """
