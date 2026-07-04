from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class NamespaceCountsDict(TypedDict):
    pods_total: int
    pods_running: int
    pods_failed: int
    deployments_total: int
    deployments_ready: int
    services_total: int


class UnhealthyResourceDict(TypedDict):
    name: str
    kind: str
    reason: str


@dataclass
class ConservativeNamespaceOverviewResponse:
    namespace: str = ""
    namespace_status: str = ""
    counts: NamespaceCountsDict | None = None
    health_status: str = ""
    root_cause: str = ""
    unhealthy_resources: list[UnhealthyResourceDict] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    has_more_unhealthy: bool = False
    remaining_unhealthy_count: int = 0
    estimated_tokens: int = 0
    is_empty: bool = False
    summary: str = ""
    error: str | None = None
