from dataclasses import dataclass


@dataclass(frozen=True)
class PlanSpikeProvisioningCommand:
    event_date: str
    traffic_multiplier: float | None = None
    provider_lead_time_hours: int = 24
    safety_margin_days: int = 3
    safe_threshold_pct: float = 85.0
    unpredictable: bool = False
