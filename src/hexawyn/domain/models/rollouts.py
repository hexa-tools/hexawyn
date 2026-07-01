from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RolloutPhase(Enum):
    HEALTHY = "healthy"
    PROGRESSING = "progressing"
    DEGRADED = "degraded"
    PAUSED = "paused"
    ABORTED = "aborted"
    UNKNOWN = "unknown"


class RolloutStrategy(Enum):
    CANARY = "canary"
    BLUE_GREEN = "blue_green"


class AnalysisRunPhase(Enum):
    RUNNING = "running"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    ERROR = "error"
    INCONCLUSIVE = "inconclusive"


@dataclass(frozen=True)
class RolloutStepStatus:
    step_index: int
    total_steps: int
    current_step_type: str
    canary_weight: int | None
    paused_at: str | None
    pause_reason: str | None


@dataclass(frozen=True)
class Rollout:
    name: str
    namespace: str
    strategy: RolloutStrategy
    phase: RolloutPhase
    desired_replicas: int
    ready_replicas: int
    current_image: str
    canary_replicas: int | None = None
    stable_replicas: int | None = None
    current_step: RolloutStepStatus | None = None
    stable_image: str | None = None
    message: str | None = None
    analysis_run_name: str | None = None


@dataclass(frozen=True)
class AnalysisRun:
    name: str
    namespace: str
    rollout_name: str
    phase: AnalysisRunPhase
    metrics_count: int
    failed_metrics: list[str]
    message: str | None
    started_at: str
    completed_at: str | None


@dataclass(frozen=True)
class RolloutsDetectionResult:
    installed: bool
    version: str | None
    namespace: str | None
    total_rollouts: int
    healthy: int
    progressing: int
    degraded: int
    paused: int
