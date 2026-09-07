from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class LiveResourceRaw(TypedDict):
    kind: str
    name: str
    namespace: str
    labels: dict[str, str]
    annotations: dict[str, str]
    data: dict[str, object]


class LiveResourcePort(ABC):
    """Driven port: lists live Kubernetes resources (currently Deployment
    and ConfigMap) with their labels and annotations — the annotations are
    read only to identify a resource's owning Helm release
    (meta.helm.sh/release-name), never as a drift-comparison target."""

    @abstractmethod
    def list_live_resources(self, namespace: str) -> list[LiveResourceRaw]:
        """Fetches every Deployment/ConfigMap in the namespace.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
