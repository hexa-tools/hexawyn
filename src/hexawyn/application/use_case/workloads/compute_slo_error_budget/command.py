from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeSLOErrorBudgetCommand:
    service_name: str = ""
    slo_target: float = 99.9
    rolling_window_days: int = 30
