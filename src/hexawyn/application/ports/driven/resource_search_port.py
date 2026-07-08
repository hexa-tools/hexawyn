from abc import ABC, abstractmethod
from typing import TypedDict


class MatchedResourceRaw(TypedDict):
    """One raw K8s resource matched by a label selector — node/phase/ready
    are populated for pods only, None for every other resource kind."""

    name: str
    namespace: str
    kind: str
    node: str | None
    phase: str | None
    ready: bool | None
    labels: dict[str, str]


class ResourceSearchPort(ABC):
    """Driven port: searches K8s resources by label selector, one method per
    API group (mirrors the kubernetes client's distinct list-by-kind calls)."""

    @abstractmethod
    def search_pods(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]: ...

    @abstractmethod
    def search_deployments(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]: ...

    @abstractmethod
    def search_services(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]: ...

    @abstractmethod
    def search_configmaps(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]: ...
