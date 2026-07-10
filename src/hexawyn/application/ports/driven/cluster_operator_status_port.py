from abc import ABC, abstractmethod
from typing import TypedDict


class ClusterOperatorRawData(TypedDict):
    name: str
    available: bool
    progressing: bool
    degraded: bool
    available_unknown: bool
    message: str
    degraded_since: str | None


class ClusterOperatorStatusPort(ABC):
    """Driven port — reads ClusterOperator status from an OpenShift cluster.

    ClusterOperators live in the config.openshift.io/v1 API group and expose
    Available / Progressing / Degraded conditions.
    """

    @abstractmethod
    def list_cluster_operators(self) -> list[ClusterOperatorRawData]:
        """Return every ClusterOperator with its parsed conditions.

        Raises ClusterOperatorCRDNotFoundError when the CRD is absent (404,
        e.g. vanilla Kubernetes).
        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """
