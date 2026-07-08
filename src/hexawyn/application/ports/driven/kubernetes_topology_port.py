from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class ServiceRecordData(TypedDict):
    name: str
    namespace: str
    replicas: int
    is_external: bool


class EdgeRecordData(TypedDict):
    caller: str
    callee: str


class KubernetesTopologyPort(ABC):
    @abstractmethod
    def list_services(self, namespace: str | None) -> list[ServiceRecordData]:
        """Return all discovered services, optionally scoped to a namespace."""

    @abstractmethod
    def get_network_policy_edges(self, namespace: str | None) -> list[EdgeRecordData]:
        """Return caller→callee edges inferred from NetworkPolicy ingress/egress rules."""
