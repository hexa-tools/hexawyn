from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class NamespaceNetworkFindingDict(TypedDict):
    namespace: str
    ingress_policies: int
    egress_policies: int
    pod_count: int
    network_status: Literal["open", "partially_restricted", "restricted"]
    risk_level: Literal["critical", "medium", "low"]
    recommendation: str | None
    note: str | None


class ExcludedNamespaceDict(TypedDict):
    namespace: str
    reason: str


@dataclass
class DetectNetworkSegmentationGapsResponse:
    findings: list[NamespaceNetworkFindingDict] = field(default_factory=list)
    excluded_namespaces: list[ExcludedNamespaceDict] = field(default_factory=list)
    total_namespaces_checked: int = 0
    fully_open_count: int = 0
    partially_restricted_count: int = 0
    restricted_count: int = 0
    summary: str = ""
    error: str | None = None
