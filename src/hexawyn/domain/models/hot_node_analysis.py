from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Recommendation = Literal["redistribute", "scale_vertically", "add_node"]


@dataclass(frozen=True)
class TopConsumer:
    pod_name: str
    namespace: str
    cpu_usage_cores: float
    memory_usage_gb: float


@dataclass(frozen=True)
class ClusterNodeSnapshot:
    node_name: str
    cordoned: bool
    allocatable_cpu_cores: float
    allocatable_memory_gb: float
    cpu_percent_series: list[tuple[str, float]] = field(default_factory=list)
    memory_percent_series: list[tuple[str, float]] = field(default_factory=list)
    pods: list[TopConsumer] = field(default_factory=list)


@dataclass(frozen=True)
class HotNodeAnalysisRequest:
    window_hours: int = 24


@dataclass(frozen=True)
class HotNodeResult:
    node_name: str
    cpu_avg_percent: float
    memory_avg_percent: float
    cpu_hot: bool
    memory_hot: bool
    hot_hours: int
    top_consumers: list[TopConsumer]
    feasible_redistribution: bool
    target_node: str | None
    recommendation: Recommendation
    business_hours_pattern: bool


@dataclass(frozen=True)
class HotNodeAnalysisReport:
    hot_nodes: list[HotNodeResult]
    healthy_node_count: int
    excluded_cordoned_nodes: list[str]
    warnings: list[str]
    summary: str
