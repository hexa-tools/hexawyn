from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeBudgetIntelligenceCommand:
    period: str
