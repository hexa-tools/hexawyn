from abc import ABC, abstractmethod
from typing import TypedDict


class RawContainerLog(TypedDict):
    container: str
    lines: list[str]
    truncated: bool


class RawPodLogData(TypedDict):
    pod_name: str
    namespace: str
    containers: list[RawContainerLog]


class LogSearchPort(ABC):
    """Driven port: fetches raw log lines for every container in one pod."""

    @abstractmethod
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        """Fetches recent log lines for every container in the given pod.

        Raises ResourceNotFoundError when the pod no longer exists.
        Raises InsufficientPermissionsError when RBAC denies log access.
        Raises ClusterUnreachableError on other cluster/API failures.
        Returns [] when the pod exists but has no accessible logs (e.g.
        evicted/completed) — not an error.
        """
