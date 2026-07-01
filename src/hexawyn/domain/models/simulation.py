from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class RiskLevel(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3


@dataclass(frozen=True)
class ScenarioInput:
    target_service: str
    namespace: str
    current_replicas: int
    proposed_replicas: int
    current_cpu_utilization: float


@dataclass
class ServiceImpact:
    name: str
    calls_per_second: float
    estimated_latency_delta_percent: float = 0


@dataclass
class ImpactReport:
    target_service: str
    namespace: str
    current_replicas: int
    proposed_replicas: int
    risk: RiskLevel
    affected_services: list[ServiceImpact] = field(default_factory=list)
    estimated_latency_increase_percent: float = 0.0
    error_risk: str = ""
    pdb_violation: bool = False
    hpa_detected: bool = False
    circular_dependency: bool = False
    recommendation: str = ""
