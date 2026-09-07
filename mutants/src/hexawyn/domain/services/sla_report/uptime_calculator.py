from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.sla_report_port import ServiceSlaRaw

_MINUTES_PER_DAY = 1440


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ServiceUptimeResult:
    actual_uptime_pct: float
    met: bool
    exceeded: bool
    prorated: bool
    coverage_days: int
mutants_x_evaluate_service__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_evaluate_service__mutmut)
def evaluate_service(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_orig(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_1(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = None
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_2(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(None)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_3(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = None
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_4(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["XXsla_target_pctXX"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_5(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["SLA_TARGET_PCT"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_6(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=None,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_7(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=None,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_8(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=None,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_9(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=None,
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_10(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=None,
    )


def x_evaluate_service__mutmut_11(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_12(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_13(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_14(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_15(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        )


def x_evaluate_service__mutmut_16(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime > target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_17(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime >= target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_18(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["XXcoverage_daysXX"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_19(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["COVERAGE_DAYS"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_20(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] <= raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_21(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["XXquarter_daysXX"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_22(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["QUARTER_DAYS"],
        coverage_days=raw["coverage_days"],
    )


def x_evaluate_service__mutmut_23(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["XXcoverage_daysXX"],
    )


def x_evaluate_service__mutmut_24(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["COVERAGE_DAYS"],
    )

mutants_x_evaluate_service__mutmut['_mutmut_orig'] = x_evaluate_service__mutmut_orig # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_1'] = x_evaluate_service__mutmut_1 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_2'] = x_evaluate_service__mutmut_2 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_3'] = x_evaluate_service__mutmut_3 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_4'] = x_evaluate_service__mutmut_4 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_5'] = x_evaluate_service__mutmut_5 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_6'] = x_evaluate_service__mutmut_6 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_7'] = x_evaluate_service__mutmut_7 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_8'] = x_evaluate_service__mutmut_8 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_9'] = x_evaluate_service__mutmut_9 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_10'] = x_evaluate_service__mutmut_10 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_11'] = x_evaluate_service__mutmut_11 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_12'] = x_evaluate_service__mutmut_12 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_13'] = x_evaluate_service__mutmut_13 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_14'] = x_evaluate_service__mutmut_14 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_15'] = x_evaluate_service__mutmut_15 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_16'] = x_evaluate_service__mutmut_16 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_17'] = x_evaluate_service__mutmut_17 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_18'] = x_evaluate_service__mutmut_18 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_19'] = x_evaluate_service__mutmut_19 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_20'] = x_evaluate_service__mutmut_20 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_21'] = x_evaluate_service__mutmut_21 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_22'] = x_evaluate_service__mutmut_22 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_23'] = x_evaluate_service__mutmut_23 # type: ignore # mutmut generated
mutants_x_evaluate_service__mutmut['x_evaluate_service__mutmut_24'] = x_evaluate_service__mutmut_24 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__effective_uptime__mutmut)
def _effective_uptime(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_orig(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_1(raw: ServiceSlaRaw) -> float:
    covered_minutes = None
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_2(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] / _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_3(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["XXcoverage_daysXX"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_4(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["COVERAGE_DAYS"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_5(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes < 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_6(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 1:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_7(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(None, 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_8(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], None)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_9(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_10(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], )

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_11(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["XXuptime_pctXX"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_12(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["UPTIME_PCT"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_13(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 4)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_14(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = None
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_15(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 / covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_16(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) * 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_17(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 + raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_18(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (101.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_19(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["XXuptime_pctXX"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_20(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["UPTIME_PCT"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_21(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 101.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_22(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = None
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_23(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(None, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_24(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, None)
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_25(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_26(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, )
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_27(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(1.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_28(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime + raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_29(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["XXmaintenance_minutesXX"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_30(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["MAINTENANCE_MINUTES"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_31(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = None
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_32(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 + effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_33(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 101.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_34(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes / 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_35(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime * covered_minutes * 100.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_36(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 101.0
    return round(effective_uptime, 3)


def x__effective_uptime__mutmut_37(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(None, 3)


def x__effective_uptime__mutmut_38(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, None)


def x__effective_uptime__mutmut_39(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(3)


def x__effective_uptime__mutmut_40(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, )


def x__effective_uptime__mutmut_41(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 4)

mutants_x__effective_uptime__mutmut['_mutmut_orig'] = x__effective_uptime__mutmut_orig # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_1'] = x__effective_uptime__mutmut_1 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_2'] = x__effective_uptime__mutmut_2 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_3'] = x__effective_uptime__mutmut_3 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_4'] = x__effective_uptime__mutmut_4 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_5'] = x__effective_uptime__mutmut_5 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_6'] = x__effective_uptime__mutmut_6 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_7'] = x__effective_uptime__mutmut_7 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_8'] = x__effective_uptime__mutmut_8 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_9'] = x__effective_uptime__mutmut_9 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_10'] = x__effective_uptime__mutmut_10 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_11'] = x__effective_uptime__mutmut_11 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_12'] = x__effective_uptime__mutmut_12 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_13'] = x__effective_uptime__mutmut_13 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_14'] = x__effective_uptime__mutmut_14 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_15'] = x__effective_uptime__mutmut_15 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_16'] = x__effective_uptime__mutmut_16 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_17'] = x__effective_uptime__mutmut_17 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_18'] = x__effective_uptime__mutmut_18 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_19'] = x__effective_uptime__mutmut_19 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_20'] = x__effective_uptime__mutmut_20 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_21'] = x__effective_uptime__mutmut_21 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_22'] = x__effective_uptime__mutmut_22 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_23'] = x__effective_uptime__mutmut_23 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_24'] = x__effective_uptime__mutmut_24 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_25'] = x__effective_uptime__mutmut_25 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_26'] = x__effective_uptime__mutmut_26 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_27'] = x__effective_uptime__mutmut_27 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_28'] = x__effective_uptime__mutmut_28 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_29'] = x__effective_uptime__mutmut_29 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_30'] = x__effective_uptime__mutmut_30 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_31'] = x__effective_uptime__mutmut_31 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_32'] = x__effective_uptime__mutmut_32 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_33'] = x__effective_uptime__mutmut_33 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_34'] = x__effective_uptime__mutmut_34 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_35'] = x__effective_uptime__mutmut_35 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_36'] = x__effective_uptime__mutmut_36 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_37'] = x__effective_uptime__mutmut_37 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_38'] = x__effective_uptime__mutmut_38 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_39'] = x__effective_uptime__mutmut_39 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_40'] = x__effective_uptime__mutmut_40 # type: ignore # mutmut generated
mutants_x__effective_uptime__mutmut['x__effective_uptime__mutmut_41'] = x__effective_uptime__mutmut_41 # type: ignore # mutmut generated
