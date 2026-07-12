from abc import ABC, abstractmethod
from typing import TypedDict


class ClusterFailureSignature(TypedDict):
    cluster_name: str
    failure_type: str
    pod_count: int
    onset_utc: str
    affected_service: str
    shared_dependency: str | None


class CrossClusterIncidentPort(ABC):
    """Driven port — returns failure signatures from all configured clusters.

    Each signature describes a failure pattern (e.g. ImagePullBackOff) with its
    onset time, affected service, and an optional shared dependency (e.g. image
    registry, ConfigMap). The domain correlates these across clusters to detect
    whether the same problem is happening simultaneously.
    """

    @abstractmethod
    def list_all_cluster_failures(self) -> list[ClusterFailureSignature]: ...
