from __future__ import annotations

from hexawyn.domain.models.image_drift import ContainerImageDrift, ContainerImageDriftReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
def build_report(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_orig(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_1(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = None
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_2(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) - in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_3(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=None,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_4(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=None,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_5(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=None,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_6(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=None,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_7(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=None,
    )


def x_build_report__mutmut_8(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_9(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_10(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_11(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        summary=_build_summary(drifts, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_12(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        )


def x_build_report__mutmut_13(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(None, in_sync_count, excluded_count),
    )


def x_build_report__mutmut_14(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, None, excluded_count),
    )


def x_build_report__mutmut_15(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, None),
    )


def x_build_report__mutmut_16(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(in_sync_count, excluded_count),
    )


def x_build_report__mutmut_17(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, excluded_count),
    )


def x_build_report__mutmut_18(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> ContainerImageDriftReport:
    total_checked = len(drifts) + in_sync_count
    return ContainerImageDriftReport(
        out_of_sync=drifts,
        in_sync_count=in_sync_count,
        excluded_count=excluded_count,
        total_checked=total_checked,
        summary=_build_summary(drifts, in_sync_count, ),
    )

mutants_x_build_report__mutmut['_mutmut_orig'] = x_build_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_1'] = x_build_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_2'] = x_build_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_3'] = x_build_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_4'] = x_build_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_5'] = x_build_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_6'] = x_build_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_7'] = x_build_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_8'] = x_build_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_9'] = x_build_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_10'] = x_build_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_11'] = x_build_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_12'] = x_build_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_13'] = x_build_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_14'] = x_build_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_15'] = x_build_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_16'] = x_build_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_17'] = x_build_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_18'] = x_build_report__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary += f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_orig(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary += f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_1(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary += f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_2(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = None
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary += f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_3(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = None
    if excluded_count:
        summary += f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_4(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary = f" {excluded_count} container(s) excluded (mutable tag)."
    return summary


def x__build_summary__mutmut_5(
    drifts: list[ContainerImageDrift], in_sync_count: int, excluded_count: int
) -> str:
    if not drifts:
        summary = f"All {in_sync_count} container(s) in sync with the declared image."
    else:
        summary = f"{len(drifts)} container(s) out of sync, {in_sync_count} in sync."
    if excluded_count:
        summary -= f" {excluded_count} container(s) excluded (mutable tag)."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
