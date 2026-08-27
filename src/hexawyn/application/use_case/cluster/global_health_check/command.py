from dataclasses import dataclass


@dataclass(frozen=True)
class GlobalHealthCheckCommand:
    max_clusters: int = 0  # 0 = unlimited (no cap on the kubeconfig contexts)
    timeout_seconds: float = 8.0
    max_workers: int = 5
    page: int = 1
    page_size: int = 0  # 0 = no pagination (scan everything in one call)
    previous_fleet_score: float | None = None
