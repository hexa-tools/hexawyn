from __future__ import annotations

from hexawyn.domain.models.image_drift import ContainerImageDrift, ContainerImageDriftReport


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
