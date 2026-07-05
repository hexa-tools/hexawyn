from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

NetworkStatus = Literal["open", "partially_restricted", "restricted"]
RiskLevel = Literal["critical", "medium", "low"]


@dataclass(frozen=True)
class NamespaceNetworkFinding:
    namespace: str
    ingress_policies: int
    egress_policies: int
    pod_count: int
    network_status: NetworkStatus
    risk_level: RiskLevel
    recommendation: str | None
    note: str | None


@dataclass(frozen=True)
class ExcludedNamespace:
    namespace: str
    reason: str


@dataclass(frozen=True)
class NetworkSegmentationReport:
    findings: list[NamespaceNetworkFinding]
    excluded_namespaces: list[ExcludedNamespace]
    total_namespaces_checked: int
    fully_open_count: int
    partially_restricted_count: int
    restricted_count: int
    summary: str
