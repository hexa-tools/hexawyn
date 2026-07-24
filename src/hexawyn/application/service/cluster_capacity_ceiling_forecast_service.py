from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
    ResourceForecastDict,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_service_port import (
    ClusterCapacityCeilingForecastServicePort,
)
from hexawyn.domain.errors import InsufficientDataError
from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastReport,
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
    ResourceForecast,
)
from hexawyn.domain.services.cluster_capacity_forecast.forecast_builder import (
    build_cluster_capacity_forecast,
)

_QUERY_TIMEOUT_SECONDS = 15.0


class ClusterCapacityCeilingForecastService(ClusterCapacityCeilingForecastServicePort):
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, capacity_port: CapacityForecastPort
    ) -> None:
        self._metrics_port = metrics_port
        self._capacity_port = capacity_port

    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)


def _to_response(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def _to_resource_dict(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )
