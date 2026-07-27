from dataclasses import dataclass


@dataclass(frozen=True)
class GlobalHealthCheckCommand:
    max_clusters: int = 10
    timeout_seconds: float = 8.0
    previous_fleet_score: float | None = None
