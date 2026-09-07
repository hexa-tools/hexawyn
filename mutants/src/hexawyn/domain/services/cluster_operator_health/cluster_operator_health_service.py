from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
)
from hexawyn.domain.models.cluster_operator_health import (
    HEALTH_DEGRADED,
    HEALTH_HEALTHY,
    HEALTH_PROGRESSING,
    HEALTH_UNKNOWN,
    ClusterOperatorHealthReport,
    ClusterOperatorStatus,
)

_CHRONIC_THRESHOLD_MINUTES = 15
_HEALTH_ORDER = {
    HEALTH_DEGRADED: 0,
    HEALTH_UNKNOWN: 1,
    HEALTH_PROGRESSING: 2,
    HEALTH_HEALTHY: 3,
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁClusterOperatorHealthServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut: MutantDict = {}  # type: ignore


class ClusterOperatorHealthService:
    """Domain service — classifies ClusterOperator health from raw conditions.

    Health precedence: an operator is degraded before progressing; an operator
    whose Available condition is Unknown is never healthy. Operators degraded
    for more than 15 minutes are chronic (vs transient).
    """

    @_mutmut_mutated(mutants_xǁClusterOperatorHealthServiceǁ__init____mutmut)
    def __init__(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def xǁClusterOperatorHealthServiceǁ__init____mutmut_orig(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def xǁClusterOperatorHealthServiceǁ__init____mutmut_1(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = None

    def xǁClusterOperatorHealthServiceǁ__init____mutmut_2(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock and _utc_now

    @_mutmut_mutated(mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut)
    def evaluate(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_orig(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_1(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = None
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_2(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(None) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_3(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=None)

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_4(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: None)

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_5(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(None, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_6(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, None))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_7(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_8(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, ))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_9(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 100))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_10(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = None
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_11(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(None)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_12(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(2 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_13(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health != HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_14(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = None
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_15(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(None)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_16(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(2 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_17(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health != HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_18(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = None

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_19(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(None)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_20(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(2 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_21(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health != HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_22(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=None,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_23(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=None,
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_24(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=None,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_25(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=None,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_26(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=None,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_27(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=None,
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_28(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_29(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_30(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_31(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_32(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            all_healthy=healthy == len(statuses),
        )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_33(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            )

    def xǁClusterOperatorHealthServiceǁevaluate__mutmut_34(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy != len(statuses),
        )

    @_mutmut_mutated(mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut)
    def _to_status(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_orig(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_1(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = None
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_2(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(None)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_3(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = None
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_4(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(None)
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_5(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get(None))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_6(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("XXdegraded_sinceXX"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_7(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("DEGRADED_SINCE"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_8(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=None,
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_9(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=None,
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_10(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=None,
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_11(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=None,
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_12(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=None,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_13(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=None,
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_14(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=None,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_15(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=None,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_16(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_17(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_18(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_19(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_20(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_21(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_22(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_23(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_24(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["XXnameXX"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_25(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["NAME"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_26(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["XXavailableXX"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_27(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["AVAILABLE"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_28(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["XXprogressingXX"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_29(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["PROGRESSING"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_30(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["XXdegradedXX"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_31(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["DEGRADED"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_32(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get(None, ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_33(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", None),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_34(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get(""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_35(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_36(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("XXmessageXX", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_37(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("MESSAGE", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_38(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", "XXXX"),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def xǁClusterOperatorHealthServiceǁ_to_status__mutmut_39(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes >= _CHRONIC_THRESHOLD_MINUTES,
        )

    @_mutmut_mutated(mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut)
    def _classify(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_orig(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_1(self, operator: ClusterOperatorRawData) -> str:
        if operator.get(None):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_2(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("XXavailable_unknownXX"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_3(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("AVAILABLE_UNKNOWN"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_4(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["XXdegradedXX"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_5(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["DEGRADED"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_6(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["XXprogressingXX"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_7(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["PROGRESSING"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_8(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["XXavailableXX"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def xǁClusterOperatorHealthServiceǁ_classify__mutmut_9(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["AVAILABLE"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    @_mutmut_mutated(mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut)
    def _degraded_duration_minutes(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_orig(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_1(self, degraded_since: str | None) -> int:
        if degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_2(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 1
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_3(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = None
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_4(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(None)
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_5(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace(None, "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_6(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", None))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_7(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_8(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", ))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_9(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("XXZXX", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_10(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_11(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "XX+00:00XX"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_12(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 1
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_13(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = None
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_14(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() + started
        return max(0, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_15(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(None, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_16(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, None)

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_17(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_18(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, )

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_19(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(1, int(elapsed.total_seconds() // 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_20(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(None))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_21(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() / 60))

    def xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_22(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 61))

mutants_xǁClusterOperatorHealthServiceǁ__init____mutmut['_mutmut_orig'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ__init____mutmut['xǁClusterOperatorHealthServiceǁ__init____mutmut_1'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ__init____mutmut['xǁClusterOperatorHealthServiceǁ__init____mutmut_2'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['_mutmut_orig'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_1'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_2'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_3'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_4'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_5'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_6'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_7'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_8'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_9'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_10'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_11'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_12'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_13'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_14'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_15'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_16'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_17'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_18'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_19'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_20'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_21'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_22'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_23'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_24'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_25'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_26'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_27'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_28'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_29'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_30'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_31'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_32'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_33'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁevaluate__mutmut['xǁClusterOperatorHealthServiceǁevaluate__mutmut_34'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁevaluate__mutmut_34 # type: ignore # mutmut generated

mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['_mutmut_orig'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_1'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_2'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_3'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_4'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_5'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_6'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_7'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_8'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_9'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_10'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_11'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_12'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_13'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_14'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_15'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_16'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_17'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_18'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_19'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_20'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_21'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_22'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_23'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_24'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_25'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_26'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_27'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_28'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_29'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_30'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_31'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_32'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_33'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_34'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_35'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_36'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_37'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_38'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_to_status__mutmut['xǁClusterOperatorHealthServiceǁ_to_status__mutmut_39'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_to_status__mutmut_39 # type: ignore # mutmut generated

mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['_mutmut_orig'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_1'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_2'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_3'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_4'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_5'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_6'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_7'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_8'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_classify__mutmut['xǁClusterOperatorHealthServiceǁ_classify__mutmut_9'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_classify__mutmut_9 # type: ignore # mutmut generated

mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['_mutmut_orig'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_1'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_2'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_3'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_4'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_5'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_6'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_7'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_8'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_9'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_10'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_11'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_12'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_13'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_14'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_15'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_16'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_17'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_18'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_19'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_20'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_21'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut['xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_22'] = ClusterOperatorHealthService.xǁClusterOperatorHealthServiceǁ_degraded_duration_minutes__mutmut_22 # type: ignore # mutmut generated
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
