from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.use_case.cluster.global_health_check.command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.use_case.cluster.global_health_check.response import (
    GlobalHealthCheckResponse,
)
from hexawyn.domain.models.fleet_health import ClusterHealthReport
from hexawyn.domain.services.fleet_health.fleet_health_score_service import (
    aggregate_fleet,
    build_cluster_report,
    make_unreachable_report,
)

_SIGNIFICANT_TREND_PCT = 0.10


def _compute_fleet_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def paginate_clusters(
    contexts: list[str], page: int, page_size: int, max_clusters: int
) -> tuple[list[str], int]:
    """Limit (``max_clusters``) and page (``page``/``page_size``) the contexts.

    ``max_clusters <= 0`` means unlimited. ``page_size <= 0`` means no
    pagination. Returns the page items and the total number of (limited)
    contexts.
    """
    if max_clusters > 0:
        contexts = contexts[:max_clusters]
    total = len(contexts)
    if page_size <= 0:
        return contexts, total
    start = (page - 1) * page_size
    return contexts[start : start + page_size], total


class GlobalHealthCheckUseCase:
    def __init__(self, port: FleetHealthPort) -> None:
        self._port = port

    def execute(self, command: GlobalHealthCheckCommand) -> GlobalHealthCheckResponse:
        contexts, total = paginate_clusters(
            self._port.list_contexts(), command.page, command.page_size, command.max_clusters
        )
        reports: list[ClusterHealthReport] = []

        with ThreadPoolExecutor(
            max_workers=max(min(len(contexts), command.max_workers), 1)
        ) as executor:
            future_to_ctx = {executor.submit(self._check_one, ctx): ctx for ctx in contexts}
            done_futures = as_completed(future_to_ctx, timeout=command.timeout_seconds)
            try:
                for future in done_futures:
                    ctx = future_to_ctx[future]
                    try:
                        report = future.result()
                    except Exception as exc:
                        report = make_unreachable_report(ctx, str(exc))
                    reports.append(report)
            except TimeoutError:
                for future, ctx in future_to_ctx.items():
                    if not future.done():
                        reports.append(make_unreachable_report(ctx, "timeout"))

        fleet_report = aggregate_fleet(reports)

        current_score: float | None = fleet_report.fleet_score
        trend = _compute_fleet_trend(command.previous_fleet_score, current_score)

        has_more = command.page_size > 0 and command.page * command.page_size < total

        return GlobalHealthCheckResponse(
            report=fleet_report,
            fleet_score_trend=trend,
            total_contexts=total,
            page=command.page,
            page_size=command.page_size,
            has_more=has_more,
        )

    def _check_one(self, context_name: str) -> ClusterHealthReport:
        metrics = self._port.get_cluster_raw_metrics(context_name)
        return build_cluster_report(metrics)
