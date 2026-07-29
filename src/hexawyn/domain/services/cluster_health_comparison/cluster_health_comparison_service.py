from __future__ import annotations

from hexawyn.domain.models.cluster_health_comparison import (
    ClusterHealthSnapshot,
    ComparisonReport,
    HealthComparisonResult,
)
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


def to_snapshot(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def compare(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = (
        normalized_a * 2
        + cluster_a.cpu_utilization_pct * 0.01
        + cluster_a.active_incidents * 5
        + cluster_a.nodes_not_ready * 10
    )
    score_b = (
        normalized_b * 2
        + cluster_b.cpu_utilization_pct * 0.01
        + cluster_b.active_incidents * 5
        + cluster_b.nodes_not_ready * 10
    )

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def _failing_per_100(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods / snap.total_pods * 100


def _unreachable_result(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def _maintenance_result(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )
