from __future__ import annotations

from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    SecretRotationReport,
    StaleSecretFinding,
)


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
