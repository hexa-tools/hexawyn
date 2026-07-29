from dataclasses import dataclass


@dataclass(frozen=True)
class EstimateCostSavingCommand:
    top_n: int = 10
    cpu_per_core_per_hour_usd: float | None = None
    memory_per_gb_per_hour_usd: float | None = None
