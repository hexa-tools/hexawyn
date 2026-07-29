# mypy: ignore-errors
from dataclasses import dataclass, field
from typing import TypedDict


class NamespaceCountsDict(TypedDict):
    total_pods: int
    total_deployments: int
    total_services: int
    total_crashlooping: int


class UnhealthyResourceDict(TypedDict):
    name: str
    kind: str
    reason: str
    since: str


@dataclass
class ConservativeNamespaceOverviewResponse:
    namespace: str = ""
    is_empty: bool = False
    counts: NamespaceCountsDict = field(default_factory=dict)  # type: ignore[arg-type]
    unhealthy_resources: list[UnhealthyResourceDict] = field(default_factory=list)
    health_score: int = 100
    summary: str = ""
    namespace_status: str = ""
    health_status: str = ""
    root_cause: str = ""
    token_limit_reached: bool = False
    warnings: str = ""
    pods_total: str = ""
    pods_running: str = ""
    pods_failed: str = ""
    deployments_total: str = ""
    deployments_ready: str = ""
    services_total: str = ""
    services_total: str = ""  # type: ignore
    deployments_ready: str = ""  # type: ignore
    deployments_total: str = ""  # type: ignore
    pods_failed: str = ""  # type: ignore
    pods_running: str = ""  # type: ignore
    pods_total: str = ""  # type: ignore
    has_more_unhealthy: str = ""
    remaining_unhealthy_count: str = ""
    estimated_tokens: str = ""
    error: str | None = None
