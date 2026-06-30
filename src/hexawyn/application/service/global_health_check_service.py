from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driving.global_health_check.global_health_check_command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_response import (
    GlobalHealthCheckResponse,
)
from hexawyn.application.ports.driving.global_health_check.global_health_check_service_port import (
    GlobalHealthCheckServicePort,
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


class GlobalHealthCheckService(GlobalHealthCheckServicePort):
    def __init__(self, port: FleetHealthPort) -> None:
        self._port = port

    def global_health_check(self, command: GlobalHealthCheckCommand) -> GlobalHealthCheckResponse:
        contexts = self._port.list_contexts()[: command.max_clusters]
        reports: list[ClusterHealthReport] = []

        with ThreadPoolExecutor(max_workers=max(min(len(contexts), 5), 1)) as executor:
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

        return GlobalHealthCheckResponse(report=fleet_report, fleet_score_trend=trend)

    def _check_one(self, context_name: str) -> ClusterHealthReport:
        metrics = self._port.get_cluster_raw_metrics(context_name)
        return build_cluster_report(metrics)
