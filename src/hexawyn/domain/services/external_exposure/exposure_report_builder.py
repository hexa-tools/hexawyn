from __future__ import annotations

from hexawyn.domain.models.external_exposure import (
    ExcludedExposure,
    ExternalExposureFinding,
    ExternalExposureReport,
)


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


def _build_summary(
    findings: list[ExternalExposureFinding],
    excluded_exposures: list[ExcludedExposure],
    total_external_services_checked: int,
) -> str:
    if not findings:
        summary = f"No unintended external exposures found out of {total_external_services_checked} checked."
    else:
        summary = (
            f"{len(findings)} unintended external service(s) found "
            f"out of {total_external_services_checked} checked."
        )
    if excluded_exposures:
        summary += f" {len(excluded_exposures)} service(s) excluded (allowlisted or internal)."
    return summary
