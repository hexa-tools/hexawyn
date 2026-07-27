from dataclasses import dataclass


@dataclass(frozen=True)
class DeploymentLatencyCommand:
    service_name: str
    regression_threshold_pct: float = 20.0
