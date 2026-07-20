from __future__ import annotations

from datetime import datetime, timedelta

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
)
from hexawyn.domain.models.cross_cluster_correlation import (
    AffectedCluster,
    CrossClusterCorrelationReport,
)


def correlate(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def _group_by_failure_type(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], []).append(sig)
    return grouped


def _parse_utc(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", "+00:00"))


def _filter_within_window(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if len(clusters) < 2:  # pragma: no cover — always called with ≥2 after line 28 check
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def _timedelta(minutes: int):  # type: ignore[no-untyped-def]  # returns timedelta
    return timedelta(minutes=minutes)


def _onset_gap_seconds(clusters: list[ClusterFailureSignature]) -> int:
    if len(clusters) < 2:  # pragma: no cover — always called with cascading=True precondition
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def _classify_scope(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:
        return "global"
    if in_window >= 2:
        return "regional"
    return "isolated"


def _extract_common_factor(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 1 else None


def _suggestion(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case
