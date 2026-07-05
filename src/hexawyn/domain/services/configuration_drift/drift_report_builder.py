from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.configuration_drift import ConfigurationDriftReport, DriftResult


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
