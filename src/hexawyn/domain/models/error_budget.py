from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SLOErrorBudgetRequest:
    service_name: str
    slo_target: float
    rolling_window_days: int


@dataclass
class SLOErrorBudgetResult:
    service_name: str = ""
    slo_target: float = 0.999
    rolling_window_days: int = 30
    total_budget_minutes: float = 0.0
    current_success_rate: float = 0.0
    error_rate: float = 0.0
    budget_consumed_minutes: float = 0.0
    budget_remaining_pct: float = 0.0
    burn_rate: float = 0.0
    time_to_exhaustion_days: float | None = None
    verdict: str = "budget_safe"
    recommendation: str = ""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
