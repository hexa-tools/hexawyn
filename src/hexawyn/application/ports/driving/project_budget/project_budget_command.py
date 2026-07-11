from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProjectBudgetCommand:
    horizon_months: int = 6
    history_months: int = 6
    budget_threshold_usd: float | None = None
    exclude_months: list[str] = field(default_factory=list)
