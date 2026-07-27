from __future__ import annotations

from hexawyn.domain.models.fleet_health import (
    CategoryReport,
    ClusterHealthReport,
    ClusterRawMetrics,
    FleetHealthReport,
)

_STATUS_ORDER = {"OK": 0, "WARNING": 1, "CRITICAL": 2, "UNKNOWN": -1}


def compute_health_score(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def _health_status_from_score(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def _node_category(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def _pod_category(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    crash_ratio = crash / max(total, 1)
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash_ratio < 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def _cpu_category(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def _memory_category(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def _cert_category(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def _pipeline_category(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def _security_category(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def build_categories(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def build_cluster_report(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def make_unreachable_report(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


_SIGNIFICANT_TREND_PCT = 0.10


def compute_fleet_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def aggregate_fleet(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        statuses = [r.health_status for r in reachable]
        worst = max(statuses, key=lambda s: {"healthy": 0, "degraded": 1, "critical": 2}.get(s, -1))
        fleet_status = worst
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )
