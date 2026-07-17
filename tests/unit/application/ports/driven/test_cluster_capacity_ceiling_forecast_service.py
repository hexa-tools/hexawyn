"""Unit tests for ClusterCapacityCeilingForecastService (mocks the new
ClusterResourceMetricsPort + CapacityForecastPort)."""

from __future__ import annotations

import re
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.service.cluster_capacity_ceiling_forecast_service import (
    ClusterCapacityCeilingForecastService,
)
from hexawyn.domain.errors import InsufficientDataError


def _cpu_series_matching_ticket() -> list[float]:
    return [67.2 - 1.92 * (13 - i) for i in range(14)]


def _memory_series_matching_ticket() -> list[float]:
    return [307.2 - 1.92 * (13 - i) for i in range(14)]


def _make_service(
    metrics_port: MagicMock | None = None, capacity_port: MagicMock | None = None
) -> tuple[ClusterCapacityCeilingForecastService, MagicMock, MagicMock]:
    if metrics_port is None:
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": _cpu_series_matching_ticket(),
            "memory_daily_gb": _memory_series_matching_ticket(),
        }
    if capacity_port is None:
        capacity_port = MagicMock()
        capacity_port.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 96.0,
            "total_allocatable_memory_gb": 384.0,
            "autoscaler_enabled": False,
        }
    service = ClusterCapacityCeilingForecastService(
        metrics_port=metrics_port, capacity_port=capacity_port
    )
    return service, metrics_port, capacity_port


class TestMetricsQuery:
    def test_calls_get_daily_usage_once(self) -> None:
        service, metrics_port, _ = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand())

        metrics_port.get_daily_usage.assert_called_once()

    def test_window_days_affects_query_window(self) -> None:
        service, metrics_port, _ = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand(window_days=7))

        call = metrics_port.get_daily_usage.call_args
        start = call.args[0]
        end = call.args[1]
        assert (end - start).days == 7


class TestCapacityPort:
    def test_calls_capacity_port_once(self) -> None:
        service, _, capacity_port = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand())

        capacity_port.get_cluster_capacity_info.assert_called_once()


class TestInsufficientData:
    def test_raises_when_both_series_empty(self) -> None:
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": [],
            "memory_daily_gb": [],
        }
        service, _, _ = _make_service(metrics_port=metrics_port)

        with pytest.raises(InsufficientDataError):
            service.forecast(ClusterCapacityCeilingForecastCommand())


class TestResponseComposition:
    def test_response_populated_with_forecast_fields(self) -> None:
        service, _, _ = _make_service()

        response = service.forecast(ClusterCapacityCeilingForecastCommand())

        assert response.error is None
        assert response.cpu is not None
        assert response.cpu["days_to_saturation"] == 15
        assert response.memory is not None
        assert response.memory["days_to_saturation"] == 40
        assert response.critical_resource == "CPU"
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", response.cpu["saturation_date"] or "")
