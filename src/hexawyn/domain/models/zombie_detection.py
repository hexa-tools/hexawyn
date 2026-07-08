from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ZombieCandidate:
    pod_name: str
    namespace: str
    age_days: int
    traffic_rps: float
    cpu_cores: float
    memory_gb: float
    risk: str  # "safe_to_remove" | "review_needed"
    reason: str


@dataclass
class ZombieDetectionResult:
    analysis_window_hours: int = 24
    zombie_candidates: list[ZombieCandidate] = field(default_factory=list)
    total_wasted_cores: float = 0.0
    total_wasted_gb: float = 0.0
    prometheus_available: bool = False
    data_source: str = "estimated"  # "prometheus" | "otel_fallback" | "estimated"
