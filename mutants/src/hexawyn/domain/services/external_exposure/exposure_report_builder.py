from __future__ import annotations

from hexawyn.domain.models.external_exposure import (
    ExcludedExposure,
    ExternalExposureFinding,
    ExternalExposureReport,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
def build_report(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_orig(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_1(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=None,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_2(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=None,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_3(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=None,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_4(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=None,
    )


def x_build_report__mutmut_5(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_6(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_7(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        summary=_build_summary(findings, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_8(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        )


def x_build_report__mutmut_9(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(None, excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_10(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, None, total_external_services_checked),
    )


def x_build_report__mutmut_11(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, None),
    )


def x_build_report__mutmut_12(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(excluded_exposures, total_external_services_checked),
    )


def x_build_report__mutmut_13(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, total_external_services_checked),
    )


def x_build_report__mutmut_14(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> ExternalExposureReport:
    return ExternalExposureReport(
        findings=findings,
        excluded_exposures=excluded_exposures,
        total_external_services_checked=total_external_services_checked,
        summary=_build_summary(findings, excluded_exposures, ),
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
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_orig(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_1(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_2(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = None  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_3(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = None
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_4(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary = f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary


def x__build_summary__mutmut_5(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary -= f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
