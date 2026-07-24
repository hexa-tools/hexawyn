from dataclasses import dataclass, field


@dataclass
class NamespaceSaving:
    namespace: str = ""
    monthly_saving_eur: float = 0.0
    recommendation: str = ""


@dataclass
class SavingOpportunity:
    name: str = ""
    category: str = ""
    saving_eur: float = 0.0
    description: str = ""


@dataclass
class CostSavingReport:
    total_saving_eur: float = 0.0
    savings: list[SavingOpportunity] = field(default_factory=list)


@dataclass
class EstimateCostSavingResponse:
    result: CostSavingReport
    error: str | None = None
