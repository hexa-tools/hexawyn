from __future__ import annotations

from hexawyn.domain.models.network_policy import (
    ExcludedNamespace,
    NamespaceNetworkFinding,
    NetworkSegmentationReport,
)


def build_report(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def _build_summary(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary
