from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)

_TREND_TOLERANCE_PCT = 2.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ResolutionResult:
    avg_resolution_minutes: int
    resolution_delta_pct: float
    resolution_trend: str
mutants_x_compute_resolution__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_resolution__mutmut)
def compute_resolution(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_orig(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_1(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = None
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_2(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(None)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_3(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = None
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_4(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(None, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_5(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, None)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_6(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_7(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, )
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_8(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=None,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_9(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=None,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_10(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=None,
    )


def x_compute_resolution__mutmut_11(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_12(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def x_compute_resolution__mutmut_13(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        )


def x_compute_resolution__mutmut_14(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(None, previous_avg),
    )


def x_compute_resolution__mutmut_15(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, None),
    )


def x_compute_resolution__mutmut_16(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(previous_avg),
    )


def x_compute_resolution__mutmut_17(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, ),
    )

mutants_x_compute_resolution__mutmut['_mutmut_orig'] = x_compute_resolution__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_1'] = x_compute_resolution__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_2'] = x_compute_resolution__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_3'] = x_compute_resolution__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_4'] = x_compute_resolution__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_5'] = x_compute_resolution__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_6'] = x_compute_resolution__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_7'] = x_compute_resolution__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_8'] = x_compute_resolution__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_9'] = x_compute_resolution__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_10'] = x_compute_resolution__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_11'] = x_compute_resolution__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_12'] = x_compute_resolution__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_13'] = x_compute_resolution__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_14'] = x_compute_resolution__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_15'] = x_compute_resolution__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_16'] = x_compute_resolution__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_resolution__mutmut['x_compute_resolution__mutmut_17'] = x_compute_resolution__mutmut_17 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__average_resolution__mutmut)
def _average_resolution(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_orig(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_1(incidents: list[ReliabilityIncidentRaw]) -> int:
    if incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_2(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 1
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_3(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = None
    return round(total / len(incidents))


def x__average_resolution__mutmut_4(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(None)
    return round(total / len(incidents))


def x__average_resolution__mutmut_5(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["XXresolution_minutesXX"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_6(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["RESOLUTION_MINUTES"] for incident in incidents)
    return round(total / len(incidents))


def x__average_resolution__mutmut_7(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(None)


def x__average_resolution__mutmut_8(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total * len(incidents))

mutants_x__average_resolution__mutmut['_mutmut_orig'] = x__average_resolution__mutmut_orig # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_1'] = x__average_resolution__mutmut_1 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_2'] = x__average_resolution__mutmut_2 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_3'] = x__average_resolution__mutmut_3 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_4'] = x__average_resolution__mutmut_4 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_5'] = x__average_resolution__mutmut_5 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_6'] = x__average_resolution__mutmut_6 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_7'] = x__average_resolution__mutmut_7 # type: ignore # mutmut generated
mutants_x__average_resolution__mutmut['x__average_resolution__mutmut_8'] = x__average_resolution__mutmut_8 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__delta_pct__mutmut)
def _delta_pct(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_orig(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_1(current: int, previous: int | None) -> float:
    if previous is None and previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_2(current: int, previous: int | None) -> float:
    if previous is not None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_3(current: int, previous: int | None) -> float:
    if previous is None or previous < 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_4(current: int, previous: int | None) -> float:
    if previous is None or previous <= 1:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_5(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 1.0
    return round((current - previous) / previous * 100, 1)


def x__delta_pct__mutmut_6(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round(None, 1)


def x__delta_pct__mutmut_7(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, None)


def x__delta_pct__mutmut_8(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round(1)


def x__delta_pct__mutmut_9(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, )


def x__delta_pct__mutmut_10(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous / 100, 1)


def x__delta_pct__mutmut_11(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) * previous * 100, 1)


def x__delta_pct__mutmut_12(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current + previous) / previous * 100, 1)


def x__delta_pct__mutmut_13(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 101, 1)


def x__delta_pct__mutmut_14(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 2)

mutants_x__delta_pct__mutmut['_mutmut_orig'] = x__delta_pct__mutmut_orig # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_1'] = x__delta_pct__mutmut_1 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_2'] = x__delta_pct__mutmut_2 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_3'] = x__delta_pct__mutmut_3 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_4'] = x__delta_pct__mutmut_4 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_5'] = x__delta_pct__mutmut_5 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_6'] = x__delta_pct__mutmut_6 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_7'] = x__delta_pct__mutmut_7 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_8'] = x__delta_pct__mutmut_8 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_9'] = x__delta_pct__mutmut_9 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_10'] = x__delta_pct__mutmut_10 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_11'] = x__delta_pct__mutmut_11 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_12'] = x__delta_pct__mutmut_12 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_13'] = x__delta_pct__mutmut_13 # type: ignore # mutmut generated
mutants_x__delta_pct__mutmut['x__delta_pct__mutmut_14'] = x__delta_pct__mutmut_14 # type: ignore # mutmut generated
mutants_x__trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__trend__mutmut)
def _trend(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_orig(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_1(delta_pct: float, previous: int | None) -> str:
    if previous is not None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_2(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "XXstableXX"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_3(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "STABLE"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_4(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct <= -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_5(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < +_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_6(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "XXimprovingXX"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_7(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "IMPROVING"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_8(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct >= _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x__trend__mutmut_9(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "XXdegradingXX"
    return "stable"


def x__trend__mutmut_10(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "DEGRADING"
    return "stable"


def x__trend__mutmut_11(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "XXstableXX"


def x__trend__mutmut_12(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "STABLE"

mutants_x__trend__mutmut['_mutmut_orig'] = x__trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_1'] = x__trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_2'] = x__trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_3'] = x__trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_4'] = x__trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_5'] = x__trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_6'] = x__trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_7'] = x__trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_8'] = x__trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_9'] = x__trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_10'] = x__trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_11'] = x__trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__trend__mutmut['x__trend__mutmut_12'] = x__trend__mutmut_12 # type: ignore # mutmut generated
