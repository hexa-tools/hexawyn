from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class TopConsumerDict(TypedDict):
    pod_name: str
    namespace: str
    cpu_usage_cores: float
    memory_usage_gb: float


class HotNodeResultDict(TypedDict):
    node_name: str
    cpu_avg_percent: float
    memory_avg_percent: float
    cpu_hot: bool
    memory_hot: bool
    hot_hours: int
    top_consumers: list[TopConsumerDict]
    feasible_redistribution: bool
    target_node: str | None
    recommendation: str
    business_hours_pattern: bool


@dataclass
class HotNodeAnalysisResponse:
    hot_nodes: list[HotNodeResultDict] = field(default_factory=list)
    healthy_node_count: int = 0
    excluded_cordoned_nodes: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    summary: str = ""
    error: str | None = None
