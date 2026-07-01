from abc import ABC, abstractmethod
from typing import TypedDict


class HistoricalPodInfo(TypedDict, total=False):
    name: str
    namespace: str
    phase: str
    restart_count: int
    queried_timestamp: str
    currently_exists: bool
    status_changed_since: bool


class KubeArchiveQuery(TypedDict, total=False):
    namespace: str
    resource_type: str
    timestamp: str
    compare_with_current: bool


class KubeArchiveResponse(TypedDict):
    namespace: str
    resource_type: str
    queried_timestamp: str
    total_resources: int
    pods: list[HistoricalPodInfo]
    kubearchive_available: bool
    error: str | None


class HistoricalComparisonResult(TypedDict):
    historical_count: int
    current_count: int
    pods_added: int
    pods_removed: int
    added_pod_names: list[str]
    removed_pod_names: list[str]
    delta_message: str


class KubeArchivePort(ABC):
    """Port for querying KubeArchive for historical Kubernetes resource state."""

    @abstractmethod
    def query_historical_state(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        """Query KubeArchive for the historical state of resources at a given timestamp."""
