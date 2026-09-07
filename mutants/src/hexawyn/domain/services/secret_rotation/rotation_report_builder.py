from __future__ import annotations

from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    SecretRotationReport,
    StaleSecretFinding,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
def build_report(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_orig(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_1(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=None,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_2(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=None,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_3(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=None,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_4(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=None,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_5(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=None,
    )


def x_build_report__mutmut_6(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_7(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_8(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_9(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_10(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        )


def x_build_report__mutmut_11(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            None, excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_12(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, None, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_13(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, None, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_14(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, None
        ),
    )


def x_build_report__mutmut_15(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            excluded_secrets, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_16(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, total_secrets_checked, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_17(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, rotation_threshold_days
        ),
    )


def x_build_report__mutmut_18(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> SecretRotationReport:
    return SecretRotationReport(
        findings=findings,
        excluded_secrets=excluded_secrets,
        total_secrets_checked=total_secrets_checked,
        rotation_threshold_days=rotation_threshold_days,
        summary=_build_summary(
            findings, excluded_secrets, total_secrets_checked, ),
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
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary += f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_orig(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary += f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_1(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary += f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_2(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = None  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary += f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_3(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = None
    if excluded_secrets:
        summary += f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_4(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary = f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary


def x__build_summary__mutmut_5(
    findings: list[StaleSecretFinding],
    excluded_secrets: list[ExcludedSecret],
    total_secrets_checked: int,
    rotation_threshold_days: int,
) -> str:
    if not findings:
        summary = f"No secrets stale (>{rotation_threshold_days} days) out of {total_secrets_checked} checked."  # noqa: E501
    else:
        summary = (
            f"{len(findings)} secret(s) stale (>{rotation_threshold_days} days) "
            f"out of {total_secrets_checked} checked."
        )
    if excluded_secrets:
        summary -= f" {len(excluded_secrets)} secret(s) excluded from rotation policy."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
