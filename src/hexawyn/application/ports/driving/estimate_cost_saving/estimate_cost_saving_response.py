from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.cost_saving_estimation import CostSavingReport


@dataclass
class EstimateCostSavingResponse:
    report: CostSavingReport = field(default_factory=CostSavingReport)
    previous_total_saving_usd: float | None = None
    saving_trend: str | None = None  # "increasing" | "decreasing" | "stable" | None
