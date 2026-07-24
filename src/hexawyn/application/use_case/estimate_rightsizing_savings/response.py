from dataclasses import dataclass, field


@dataclass
class RightsizingRecommendation:
    pod_name: str = ""
    namespace: str = ""
    current_cpu: float = 0.0
    recommended_cpu: float = 0.0
    current_memory_gb: float = 0.0
    recommended_memory_gb: float = 0.0
    monthly_saving_eur: float = 0.0


@dataclass
class RightsizingReport:
    total_monthly_saving_eur: float = 0.0
    recommendations: list[RightsizingRecommendation] = field(default_factory=list)


@dataclass
class EstimateRightsizingSavingsResponse:
    result: RightsizingReport
    error: str | None = None
