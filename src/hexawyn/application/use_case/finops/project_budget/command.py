from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProjectBudgetCommand:
    history_months: int = 6
    horizon_months: int = 3
    budget_threshold_usd: float = 1000.0
    exclude_months: list[str] = field(default_factory=list)
