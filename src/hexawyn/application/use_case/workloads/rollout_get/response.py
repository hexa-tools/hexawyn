from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RolloutGetResponse:
    name: str = ""
    namespace: str = ""
    strategy: str = ""
    phase: str = ""
    desired_replicas: int = 0
    ready_replicas: int = 0
    canary_replicas: int | None = None
    stable_replicas: int | None = None
    current_image: str = ""
    stable_image: str | None = None
    step_index: int | None = None
    total_steps: int | None = None
    current_step_type: str | None = None
    canary_weight: int | None = None
    paused_at: str | None = None
    pause_reason: str | None = None
    message: str | None = None
    analysis_run_name: str | None = None
    error: str | None = None
