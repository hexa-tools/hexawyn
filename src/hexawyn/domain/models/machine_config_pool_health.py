from __future__ import annotations

from dataclasses import dataclass, field

STATE_READY = "ready"
STATE_UPDATING = "updating"
STATE_DEGRADED = "degraded"
STATE_DEGRADED_UPDATING = "degraded+updating"
STATE_PAUSED = "paused"


@dataclass(frozen=True)
class MachineConfigPoolStatus:
    name: str
    state: str
    machine_count: int
    ready_machine_count: int
    updated_machine_count: int
    degraded_machine_count: int
    current_config: str
    desired_config: str
    config_mismatch: bool
    paused: bool
    reason: str
    updating_duration_minutes: int
    is_stuck: bool


@dataclass
class MachineConfigPoolHealthReport:
    pools: list[MachineConfigPoolStatus] = field(default_factory=list)
    total: int = 0
    healthy: int = 0
    degraded: int = 0
    updating: int = 0
    paused: int = 0
    all_healthy: bool = True
