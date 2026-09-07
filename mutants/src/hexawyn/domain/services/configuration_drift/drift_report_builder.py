from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.configuration_drift import ConfigurationDriftReport, DriftResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_drift_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_drift_report__mutmut)
def build_drift_report(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_orig(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_1(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = None
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_2(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields and result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_3(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = None

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_4(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) + len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_5(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = None
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_6(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(None)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_7(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(None)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_8(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=None,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_9(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=None,
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_10(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=None,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_11(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=None,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_12(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=None,
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_13(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=None,
    )


def x_build_drift_report__mutmut_14(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_15(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_16(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_17(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_18(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_19(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        )


def x_build_drift_report__mutmut_20(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(None),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_21(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(None, in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_22(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, None, excluded),
    )


def x_build_drift_report__mutmut_23(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, None),
    )


def x_build_drift_report__mutmut_24(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(in_sync_count, excluded),
    )


def x_build_drift_report__mutmut_25(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, excluded),
    )


def x_build_drift_report__mutmut_26(results: list[DriftResult], excluded: list[str]) -> ConfigurationDriftReport:
    drifted = [result for result in results if result.drifted_fields or result.is_orphaned]
    in_sync_count = len(results) - len(drifted)

    drifted_by_namespace: dict[str, list[DriftResult]] = defaultdict(list)
    for result in drifted:
        drifted_by_namespace[result.namespace].append(result)

    return ConfigurationDriftReport(
        drifted_resources=drifted,
        drifted_by_namespace=dict(drifted_by_namespace),
        in_sync_count=in_sync_count,
        excluded_resources=excluded,
        total_checked=len(results),
        summary=_build_summary(drifted, in_sync_count, ),
    )

mutants_x_build_drift_report__mutmut['_mutmut_orig'] = x_build_drift_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_1'] = x_build_drift_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_2'] = x_build_drift_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_3'] = x_build_drift_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_4'] = x_build_drift_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_5'] = x_build_drift_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_6'] = x_build_drift_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_7'] = x_build_drift_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_8'] = x_build_drift_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_9'] = x_build_drift_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_10'] = x_build_drift_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_11'] = x_build_drift_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_12'] = x_build_drift_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_13'] = x_build_drift_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_14'] = x_build_drift_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_15'] = x_build_drift_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_16'] = x_build_drift_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_17'] = x_build_drift_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_18'] = x_build_drift_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_19'] = x_build_drift_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_20'] = x_build_drift_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_21'] = x_build_drift_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_22'] = x_build_drift_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_23'] = x_build_drift_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_24'] = x_build_drift_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_25'] = x_build_drift_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_drift_report__mutmut['x_build_drift_report__mutmut_26'] = x_build_drift_report__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_orig(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_1(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_2(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = None
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_3(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = None
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_4(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(None)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_5(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(2 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_6(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = None
    if excluded:
        summary += f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_7(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary = f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary


def x__build_summary__mutmut_8(drifted: list[DriftResult], in_sync_count: int, excluded: list[str]) -> str:
    if not drifted:
        summary = f"All {in_sync_count} resource(s) in sync with desired state."
    else:
        critical_count = sum(1 for result in drifted if result.has_critical_drift)
        summary = (
            f"{len(drifted)} drifted resource(s) found ({critical_count} critical), "
            f"{in_sync_count} in sync."
        )
    if excluded:
        summary -= f" {len(excluded)} resource(s) excluded (not managed by Helm or Kustomize)."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_6'] = x__build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_7'] = x__build_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_8'] = x__build_summary__mutmut_8 # type: ignore # mutmut generated
