from abc import ABC, abstractmethod
from typing import TypedDict


class ResourceInvestigationRawData(TypedDict):
    events: list[str]
    logs: list[str]
    restart_count: int
    last_termination_reason: str | None


class AdaptiveInvestigationPort(ABC):
    """Driven port: drills into a single failing resource (events, container
    logs, restart/termination info) for the adaptive investigation flow."""

    @abstractmethod
    def investigate_resource(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        """Fetches events/logs/restart info for one resource.

        Raises ResourceNotFoundError if the resource no longer exists (it may
        have disappeared between the overview and the drill-down).
        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
