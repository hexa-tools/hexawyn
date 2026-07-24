from __future__ import annotations

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.use_case.global_health_check.command import GlobalHealthCheckCommand
from hexawyn.application.use_case.global_health_check.response import GlobalHealthCheckResponse
from hexawyn.domain.models.fleet_health import ClusterRawMetrics
from hexawyn.domain.services.fleet_health.fleet_health_score_service import (
    aggregate_fleet,
    build_cluster_report,
    make_unreachable_report,
)


class GlobalHealthCheckUseCase:
    def __init__(self, port: FleetHealthPort) -> None:
        self._port = port

    def execute(self, command: GlobalHealthCheckCommand) -> GlobalHealthCheckResponse:
        contexts = self._port.list_contexts()
        limited = contexts[: command.max_clusters]

        cluster_reports = []
        for ctx in limited:
            try:
                metrics: ClusterRawMetrics = self._port.get_cluster_raw_metrics(ctx)
                cluster_reports.append(build_cluster_report(metrics))
            except Exception as exc:
                cluster_reports.append(make_unreachable_report(ctx, str(exc)))

        report = aggregate_fleet(cluster_reports)

        trend: str | None = None
        if command.previous_fleet_score is not None and report.fleet_score is not None:
            if report.fleet_score > command.previous_fleet_score:
                trend = "improving"
            elif report.fleet_score < command.previous_fleet_score:
                trend = "degrading"
            else:
                trend = "stable"

        return GlobalHealthCheckResponse(report=report, fleet_score_trend=trend)
