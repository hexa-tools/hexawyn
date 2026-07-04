"""Unit tests for ClusterCapacityCeilingForecastService (mocks the existing
MetricsQueryPort [ECA-31, reused] + the new CapacityForecastPort)."""

from __future__ import annotations

import re
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.service.cluster_capacity_ceiling_forecast_service import (
    ClusterCapacityCeilingForecastService,
)
from hexawyn.domain.errors import InsufficientDataError


def _range_sample(values: list[float]) -> dict:
    now = datetime.now(UTC)
    return {"metric": {}, "values": [(now.isoformat(), v) for v in values]}


def _cpu_series_matching_ticket() -> list[float]:
    return [67.2 - 1.92 * (13 - i) for i in range(14)]


def _memory_series_matching_ticket() -> list[float]:
    return [307.2 - 1.92 * (13 - i) for i in range(14)]


def _make_service(
    metrics_port: MagicMock | None = None, capacity_port: MagicMock | None = None
) -> tuple[ClusterCapacityCeilingForecastService, MagicMock, MagicMock]:
    if metrics_port is None:
        metrics_port = MagicMock()
        metrics_port.range_query.side_effect = [
            [_range_sample(_cpu_series_matching_ticket())],
            [_range_sample(_memory_series_matching_ticket())],
        ]
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


class TestPrometheusQueries:
    def test_calls_range_query_twice_with_daily_step(self) -> None:
        service, metrics_port, _ = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand())

        assert metrics_port.range_query.call_count == 2
        for call in metrics_port.range_query.call_args_list:
            assert call.kwargs.get("step", call.args[3] if len(call.args) > 3 else None) == "1d"

    def test_window_days_affects_query_start(self) -> None:
        service, metrics_port, _ = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand(window_days=7))

        first_call = metrics_port.range_query.call_args_list[0]
        start_str = first_call.kwargs.get(
            "start", first_call.args[1] if len(first_call.args) > 1 else None
        )
        end_str = first_call.kwargs.get(
            "end", first_call.args[2] if len(first_call.args) > 2 else None
        )
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        assert (end - start).days == 7


class TestCapacityPort:
    def test_calls_capacity_port_once(self) -> None:
        service, _, capacity_port = _make_service()

        service.forecast(ClusterCapacityCeilingForecastCommand())

        capacity_port.get_cluster_capacity_info.assert_called_once()


class TestInsufficientData:
    def test_raises_when_both_series_empty(self) -> None:
        metrics_port = MagicMock()
        metrics_port.range_query.side_effect = [[], []]
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
