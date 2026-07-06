from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class CrossNamespaceFlowDict(TypedDict):
    source_namespace: str
    destination_namespace: str
    source_service: str
    destination_service: str
    call_count: int
    first_seen: str | None


class CrossNamespaceTrafficPort(ABC):
    """Port for querying cross-namespace traffic data from OTel traces
    or network flow logs. Returns every observed source→destination
    namespace pair with service-level detail so the domain layer can
    classify each flow against the expected communication matrix."""

    @abstractmethod
    def list_cross_namespace_flows(self) -> list[CrossNamespaceFlowDict]:
        """List every observed cross-namespace service-to-service call
        from OTel traces or equivalent flow data."""
