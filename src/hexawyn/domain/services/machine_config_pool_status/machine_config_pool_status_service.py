from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolRawData,
)
from hexawyn.domain.models.machine_config_pool_health import (
    STATE_DEGRADED,
    STATE_DEGRADED_UPDATING,
    STATE_PAUSED,
    STATE_READY,
    STATE_UPDATING,
    MachineConfigPoolHealthReport,
    MachineConfigPoolStatus,
)

_STUCK_THRESHOLD_MINUTES = 30
_STATE_ORDER = {
    STATE_DEGRADED: 0,
    STATE_DEGRADED_UPDATING: 1,
    STATE_UPDATING: 2,
    STATE_PAUSED: 3,
    STATE_READY: 4,
}


class MachineConfigPoolStatusService:
    """Domain service — classifies MachineConfigPool health from raw status.

    State precedence: a paused pool is reported as paused (an intentional
    operator action, never degraded). Otherwise degraded wins over updating,
    and a pool that is both degraded and updating gets a combined state. A pool
    updating for more than 30 minutes is flagged as stuck.
    """

    def __init__(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def evaluate(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def _to_status(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def _classify(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def _updating_duration_minutes(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))


_DEGRADED_STATES = frozenset({STATE_DEGRADED, STATE_DEGRADED_UPDATING})
_UPDATING_STATES = frozenset({STATE_UPDATING, STATE_DEGRADED_UPDATING})


def _utc_now() -> datetime:
    return datetime.now(UTC)
