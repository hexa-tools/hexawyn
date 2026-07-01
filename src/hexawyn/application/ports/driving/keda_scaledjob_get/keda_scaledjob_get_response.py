from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KedaScaledJobGetResponse:
    name: str = ""
    namespace: str = ""
    phase: str = "unknown"
    successful_jobs: int = 0
    failed_jobs: int = 0
    last_execution_time: str | None = None
    job_target_ref: str = ""
    cooldown_period_seconds: int = 0
    max_replica_count: int = 0
    message: str | None = None
    error: str | None = None
