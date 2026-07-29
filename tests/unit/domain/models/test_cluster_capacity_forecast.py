"""Unit tests for the Cluster Capacity Ceiling Forecast domain models — pure
dataclasses, no I/O."""

from __future__ import annotations

from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastReport,
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
    ResourceForecast,
)


class TestClusterCapacityRawData:
    def test_defaults(self) -> None:
        raw = ClusterCapacityRawData()

        assert raw.cpu_daily_usage_cores == []
        assert raw.memory_daily_usage_gb == []
        assert raw.total_allocatable_cpu_cores == 0.0
        assert raw.autoscaler_enabled is False

    def test_custom_values(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[40.0, 67.2],
            memory_daily_usage_gb=[200.0, 307.2],
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
            autoscaler_enabled=True,
        )

        assert raw.cpu_daily_usage_cores == [40.0, 67.2]
        assert raw.autoscaler_enabled is True


class TestResourceForecast:
    def test_fields(self) -> None:
        forecast = ResourceForecast(
            resource_type="cpu",
            current_value=67.2,
            ceiling=96.0,
            current_utilization_percent=70.0,
            growth_rate_per_day=1.92,
            days_to_saturation=15,
            saturation_date="2026-07-01",
            capacity_jump_detected=False,
            spike_caveat=False,
            capped_horizon=False,
        )

        assert forecast.resource_type == "cpu"
        assert forecast.days_to_saturation == 15  # noqa: PLR2004
        assert forecast.saturation_date == "2026-07-01"


class TestClusterCapacityForecastRequest:
    def test_default_window(self) -> None:
        request = ClusterCapacityForecastRequest()

        assert request.window_days == 14  # noqa: PLR2004

    def test_custom_window(self) -> None:
        request = ClusterCapacityForecastRequest(window_days=7)

        assert request.window_days == 7  # noqa: PLR2004


class TestClusterCapacityForecastReport:
    def test_fields(self) -> None:
        cpu = ResourceForecast(
            resource_type="cpu",
            current_value=67.2,
            ceiling=96.0,
            current_utilization_percent=70.0,
            growth_rate_per_day=1.92,
            days_to_saturation=15,
            saturation_date="2026-07-01",
            capacity_jump_detected=False,
            spike_caveat=False,
            capped_horizon=False,
        )
        memory = ResourceForecast(
            resource_type="memory",
            current_value=307.2,
            ceiling=384.0,
            current_utilization_percent=80.0,
            growth_rate_per_day=1.92,
            days_to_saturation=40,
            saturation_date="2026-07-26",
            capacity_jump_detected=False,
            spike_caveat=False,
            capped_horizon=False,
        )

        report = ClusterCapacityForecastReport(
            cpu=cpu,
            memory=memory,
            critical_resource="CPU",
            autoscaler_enabled=False,
            recommendation="Add 2+ worker nodes within the next 10 days",
            confidence="high",
            window_days_used=14,
        )

        assert report.critical_resource == "CPU"
        assert report.confidence == "high"
        assert report.window_days_used == 14  # noqa: PLR2004
