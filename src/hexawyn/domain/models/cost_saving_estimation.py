from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PodSavingOpportunity:
    pod_name: str
    namespace: str
    current_cpu_request: float | None
    recommended_cpu_request: float | None
    current_memory_request_mi: float | None
    recommended_memory_request_mi: float | None
    delta_cores: float
    delta_memory_mi: float
    monthly_saving_usd: float | None  # None when pricing not configured
    hpa_enabled: bool
    is_bursty: bool
    caveats: list[str]


@dataclass(frozen=True)
class NamespaceSaving:
    namespace: str
    pod_count: int
    total_delta_cores: float
    total_delta_memory_mi: float
    total_monthly_saving_usd: float | None


@dataclass
class CostSavingReport:
    top_opportunities: list[PodSavingOpportunity] = field(default_factory=list)
    namespace_savings: list[NamespaceSaving] = field(default_factory=list)
    total_monthly_saving_usd: float | None = None
    total_delta_cores: float = 0.0
    total_delta_memory_mi: float = 0.0
    pods_analyzed: int = 0
    pods_excluded: int = 0
    pricing_configured: bool = False
