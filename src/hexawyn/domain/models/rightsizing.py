from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class RightsizingType(Enum):
    OVER_PROVISIONED = "over_provisioned"
    UNDER_PROVISIONED = "under_provisioned"
    OPTIMAL = "optimal"


@dataclass(frozen=True)
class RightsizingRecommendation:
    resource_name: str
    namespace: str
    kind: str  # "Deployment" | "StatefulSet"
    rightsizing_type: RightsizingType
    current_cpu_cores: float
    recommended_cpu_cores: float
    current_memory_mi: float
    recommended_memory_mi: float
    monthly_savings_usd: float  # positive = over-provisioned, negative = under
    waste_percentage: float
    reason: str
    priority: str  # "high" | "medium" | "low"


@dataclass
class RightsizingReport:
    recommendations: list[RightsizingRecommendation] = field(default_factory=list)
    skipped_count: int = 0
    total_monthly_savings_usd: float = 0.0
