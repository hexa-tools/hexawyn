from __future__ import annotations

from dataclasses import dataclass, field

ScopeClassification = str  # "none" | "isolated" | "regional" | "global"


@dataclass(frozen=True)
class AffectedCluster:
    cluster_name: str
    onset_utc: str
    pod_count: int
    failure_type: str


@dataclass
class CrossClusterCorrelationReport:
    scope: str = "none"
    affected_clusters: list[AffectedCluster] = field(default_factory=list)
    common_failure_type: str = ""
    common_factor: str = ""
    suggestion: str = ""
    cascading: bool = False
    has_data: bool = True
    warning: str = ""
