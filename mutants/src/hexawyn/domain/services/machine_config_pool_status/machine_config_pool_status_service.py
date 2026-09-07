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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMachineConfigPoolStatusServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut: MutantDict = {}  # type: ignore


class MachineConfigPoolStatusService:
    """Domain service — classifies MachineConfigPool health from raw status.

    State precedence: a paused pool is reported as paused (an intentional
    operator action, never degraded). Otherwise degraded wins over updating,
    and a pool that is both degraded and updating gets a combined state. A pool
    updating for more than 30 minutes is flagged as stuck.
    """

    @_mutmut_mutated(mutants_xǁMachineConfigPoolStatusServiceǁ__init____mutmut)
    def __init__(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def xǁMachineConfigPoolStatusServiceǁ__init____mutmut_orig(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def xǁMachineConfigPoolStatusServiceǁ__init____mutmut_1(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = None

    def xǁMachineConfigPoolStatusServiceǁ__init____mutmut_2(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock and _utc_now

    @_mutmut_mutated(mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_orig(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_1(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = None
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_2(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(None) for pool in pools]
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_3(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=None)

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_4(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: None)

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_5(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(None, 99))

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_6(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, None))

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_7(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(99))

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_8(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, ))

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_9(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 100))

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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_10(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = None
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_11(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(None)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_12(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(2 for status in statuses if status.state in _DEGRADED_STATES)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_13(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state not in _DEGRADED_STATES)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_14(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = None
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_15(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(None)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_16(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(2 for status in statuses if status.state == STATE_UPDATING)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_17(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state != STATE_UPDATING)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_18(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = None
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_19(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(None)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_20(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(2 for status in statuses if status.state == STATE_PAUSED)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_21(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state != STATE_PAUSED)
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

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_22(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = None

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_23(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(None)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_24(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(2 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_25(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state != STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_26(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=None,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_27(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=None,
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_28(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            healthy=None,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_29(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            degraded=None,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_30(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            updating=None,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_31(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            paused=None,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_32(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            all_healthy=None,
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_33(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_34(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            healthy=healthy,
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_35(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
        statuses = [self._to_status(pool) for pool in pools]
        statuses.sort(key=lambda status: _STATE_ORDER.get(status.state, 99))

        degraded = sum(1 for status in statuses if status.state in _DEGRADED_STATES)
        updating = sum(1 for status in statuses if status.state == STATE_UPDATING)
        paused = sum(1 for status in statuses if status.state == STATE_PAUSED)
        healthy = sum(1 for status in statuses if status.state == STATE_READY)

        return MachineConfigPoolHealthReport(
            pools=statuses,
            total=len(statuses),
            degraded=degraded,
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_36(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            updating=updating,
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_37(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            paused=paused,
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_38(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            all_healthy=healthy == len(statuses),
        )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_39(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            )

    def xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_40(self, pools: list[MachineConfigPoolRawData]) -> MachineConfigPoolHealthReport:
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
            all_healthy=healthy != len(statuses),
        )

    @_mutmut_mutated(mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut)
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_orig(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_1(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = None
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_2(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(None)
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_3(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = None
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_4(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(None, state)
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_5(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, None)
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_6(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(state)
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_7(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, )
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_8(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=None,
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_9(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=None,
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_10(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=None,
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_11(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=None,
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_12(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=None,
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_13(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=None,
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_14(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=None,
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_15(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            desired_config=None,
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_16(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=None,
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_17(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            paused=None,
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_18(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=None,
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_19(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            updating_duration_minutes=None,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_20(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            is_stuck=None,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_21(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_22(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_23(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_24(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_25(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_26(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_27(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_28(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_29(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_30(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_31(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_32(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_33(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_34(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["XXnameXX"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_35(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["NAME"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_36(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["XXmachine_countXX"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_37(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["MACHINE_COUNT"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_38(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["XXready_machine_countXX"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_39(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["READY_MACHINE_COUNT"],
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

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_40(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["XXupdated_machine_countXX"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_41(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["UPDATED_MACHINE_COUNT"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_42(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["XXdegraded_machine_countXX"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_43(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["DEGRADED_MACHINE_COUNT"],
            current_config=pool["current_config"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_44(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["XXcurrent_configXX"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_45(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
        state = self._classify(pool)
        duration_minutes = self._updating_duration_minutes(pool, state)
        return MachineConfigPoolStatus(
            name=pool["name"],
            state=state,
            machine_count=pool["machine_count"],
            ready_machine_count=pool["ready_machine_count"],
            updated_machine_count=pool["updated_machine_count"],
            degraded_machine_count=pool["degraded_machine_count"],
            current_config=pool["CURRENT_CONFIG"],
            desired_config=pool["desired_config"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_46(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            desired_config=pool["XXdesired_configXX"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_47(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            desired_config=pool["DESIRED_CONFIG"],
            config_mismatch=pool["current_config"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_48(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["XXcurrent_configXX"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_49(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["CURRENT_CONFIG"] != pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_50(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["current_config"] == pool["desired_config"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_51(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["current_config"] != pool["XXdesired_configXX"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_52(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            config_mismatch=pool["current_config"] != pool["DESIRED_CONFIG"],
            paused=pool["paused"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_53(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            paused=pool["XXpausedXX"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_54(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            paused=pool["PAUSED"],
            reason=pool.get("reason", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_55(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get(None, ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_56(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("reason", None),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_57(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get(""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_58(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("reason", ),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_59(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("XXreasonXX", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_60(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("REASON", ""),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_61(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            reason=pool.get("reason", "XXXX"),
            updating_duration_minutes=duration_minutes,
            is_stuck=duration_minutes > _STUCK_THRESHOLD_MINUTES,
        )

    def xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_62(self, pool: MachineConfigPoolRawData) -> MachineConfigPoolStatus:
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
            is_stuck=duration_minutes >= _STUCK_THRESHOLD_MINUTES,
        )

    @_mutmut_mutated(mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut)
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

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_orig(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_1(self, pool: MachineConfigPoolRawData) -> str:
        if pool["XXpausedXX"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_2(self, pool: MachineConfigPoolRawData) -> str:
        if pool["PAUSED"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_3(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] or pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_4(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["XXdegradedXX"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_5(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["DEGRADED"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_6(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["XXupdatingXX"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_7(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["UPDATING"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_8(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["XXdegradedXX"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_9(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["DEGRADED"]:
            return STATE_DEGRADED
        if pool["updating"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_10(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["XXupdatingXX"]:
            return STATE_UPDATING
        return STATE_READY

    def xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_11(self, pool: MachineConfigPoolRawData) -> str:
        if pool["paused"]:
            return STATE_PAUSED
        if pool["degraded"] and pool["updating"]:
            return STATE_DEGRADED_UPDATING
        if pool["degraded"]:
            return STATE_DEGRADED
        if pool["UPDATING"]:
            return STATE_UPDATING
        return STATE_READY

    @_mutmut_mutated(mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut)
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

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_orig(self, pool: MachineConfigPoolRawData, state: str) -> int:
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

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_1(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state in _UPDATING_STATES:
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

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_2(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 1
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_3(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = None
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_4(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get(None)
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_5(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("XXupdating_sinceXX")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_6(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("UPDATING_SINCE")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_7(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_8(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 1
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_9(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = None
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_10(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(None)
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_11(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace(None, "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_12(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", None))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_13(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_14(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", ))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_15(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("XXZXX", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_16(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_17(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "XX+00:00XX"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_18(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 1
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_19(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = None
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_20(self, pool: MachineConfigPoolRawData, state: str) -> int:
        if state not in _UPDATING_STATES:
            return 0
        updating_since = pool.get("updating_since")
        if not updating_since:
            return 0
        try:
            started = datetime.fromisoformat(updating_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() + started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_21(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(None, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_22(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(0, None)

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_23(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_24(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(0, )

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_25(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(1, int(elapsed.total_seconds() // 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_26(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(0, int(None))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_27(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(0, int(elapsed.total_seconds() / 60))

    def xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_28(self, pool: MachineConfigPoolRawData, state: str) -> int:
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
        return max(0, int(elapsed.total_seconds() // 61))

mutants_xǁMachineConfigPoolStatusServiceǁ__init____mutmut['_mutmut_orig'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ__init____mutmut['xǁMachineConfigPoolStatusServiceǁ__init____mutmut_1'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ__init____mutmut['xǁMachineConfigPoolStatusServiceǁ__init____mutmut_2'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['_mutmut_orig'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_1'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_2'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_3'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_4'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_5'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_6'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_7'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_8'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_9'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_10'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_11'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_12'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_13'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_14'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_15'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_16'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_17'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_18'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_19'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_20'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_21'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_22'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_23'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_24'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_25'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_26'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_27'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_28'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_29'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_30'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_31'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_32'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_33'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_34'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_35'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_36'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_37'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_38'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_39'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁevaluate__mutmut['xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_40'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁevaluate__mutmut_40 # type: ignore # mutmut generated

mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['_mutmut_orig'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_1'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_2'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_3'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_4'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_5'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_6'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_7'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_8'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_9'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_10'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_11'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_12'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_13'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_14'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_15'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_16'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_17'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_18'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_19'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_20'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_21'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_22'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_23'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_24'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_25'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_26'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_27'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_28'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_29'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_30'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_31'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_32'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_33'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_34'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_35'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_36'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_37'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_38'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_39'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_40'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_41'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_42'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_43'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_44'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_45'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_46'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_47'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_48'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_49'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_50'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_51'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_52'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_53'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_54'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_55'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_56'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_57'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_58'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_58 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_59'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_59 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_60'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_60 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_61'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_61 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut['xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_62'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_to_status__mutmut_62 # type: ignore # mutmut generated

mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['_mutmut_orig'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_1'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_2'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_3'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_4'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_5'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_6'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_7'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_8'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_9'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_10'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_classify__mutmut['xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_11'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_classify__mutmut_11 # type: ignore # mutmut generated

mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['_mutmut_orig'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_1'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_2'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_3'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_4'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_5'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_6'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_7'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_8'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_9'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_10'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_11'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_12'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_13'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_14'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_15'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_16'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_17'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_18'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_19'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_20'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_21'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_22'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_23'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_24'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_25'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_26'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_27'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut['xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_28'] = MachineConfigPoolStatusService.xǁMachineConfigPoolStatusServiceǁ_updating_duration_minutes__mutmut_28 # type: ignore # mutmut generated


_DEGRADED_STATES = frozenset({STATE_DEGRADED, STATE_DEGRADED_UPDATING})
_UPDATING_STATES = frozenset({STATE_UPDATING, STATE_DEGRADED_UPDATING})
mutants_x__utc_now__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__utc_now__mutmut)
def _utc_now() -> datetime:
    return datetime.now(UTC)


def x__utc_now__mutmut_orig() -> datetime:
    return datetime.now(UTC)


def x__utc_now__mutmut_1() -> datetime:
    return datetime.now(None)

mutants_x__utc_now__mutmut['_mutmut_orig'] = x__utc_now__mutmut_orig # type: ignore # mutmut generated
mutants_x__utc_now__mutmut['x__utc_now__mutmut_1'] = x__utc_now__mutmut_1 # type: ignore # mutmut generated
