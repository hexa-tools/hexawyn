from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusRangeSample,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_response import (
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

_CPU_USAGE_PROMQL = 'sum(rate(container_cpu_usage_seconds_total{container!=""}[5m]))'
_MEMORY_USAGE_PROMQL = 'sum(container_memory_working_set_bytes{container!=""}) / (1024*1024*1024)'
_QUERY_TIMEOUT_SECONDS = 15.0
_RANGE_STEP = "1d"


class ClusterCapacityCeilingForecastService(ClusterCapacityCeilingForecastServicePort):
    def __init__(self, metrics_port: MetricsQueryPort, capacity_port: CapacityForecastPort) -> None:
        self._metrics_port = metrics_port
        self._capacity_port = capacity_port

    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        cpu_values = self._fetch_daily_series(_CPU_USAGE_PROMQL, start, end)
        memory_values = self._fetch_daily_series(_MEMORY_USAGE_PROMQL, start, end)
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

    def _fetch_daily_series(self, promql: str, start: datetime, end: datetime) -> list[float]:
        samples = self._metrics_port.range_query(
            promql,
            start=start.isoformat(),
            end=end.isoformat(),
            step=_RANGE_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return _extract_series(samples)


def _extract_series(samples: list[PrometheusRangeSample]) -> list[float]:
    if not samples:
        return []
    return [value for _, value in samples[0]["values"]]


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
