from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class ServiceRaw(TypedDict):
    name: str
    namespace: str
    service_type: str
    ports: list[int]
    node_port: int | None
    external_ip: str | None
    external_hostname: str | None
    has_source_ranges: bool
    annotations: dict[str, str]


class ExternalExposureAuditPort(ABC):
    """Port for enumerating every Service across the cluster — unfiltered.
    The LoadBalancer/NodePort type filter is applied in the application
    service via a domain function, keeping that decision testable in the
    domain layer."""

    @abstractmethod
    def list_external_services(self) -> list[ServiceRaw]:
        """List every Service across all namespaces, with its type, ports,
        LoadBalancer status, source-range restriction, and annotations."""
