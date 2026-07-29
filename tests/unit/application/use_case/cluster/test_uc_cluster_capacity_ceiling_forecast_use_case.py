from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (  # noqa: E501
    ClusterCapacityCeilingForecastUseCase,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
)


class TestClusterCapacityCeilingForecastUseCase:
    def test_forecast_returns_response_type(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": [10.0, 12.0, 15.0],
            "memory_daily_gb": [16.0, 18.0, 20.0],
        }
        capacity_port = MagicMock()
        capacity_port.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "autoscaler_enabled": True,
        }

        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=metrics_port, capacity_port=capacity_port
        )
        result = use_case.forecast(ClusterCapacityCeilingForecastCommand())

        assert isinstance(result, ClusterCapacityCeilingForecastResponse)
        assert result.error is None

    def test_forecast_includes_all_response_fields(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": [10.0],
            "memory_daily_gb": [16.0],
        }
        capacity_port = MagicMock()
        capacity_port.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "autoscaler_enabled": False,
        }

        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=metrics_port, capacity_port=capacity_port
        )
        result = use_case.forecast(ClusterCapacityCeilingForecastCommand())

        assert result.cpu is not None
        assert result.memory is not None
        assert result.critical_resource is not None
        assert result.recommendation is not None
        assert result.window_days_used > 0

    def test_forecast_uses_window_days_from_command(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": [10.0] * 30,
            "memory_daily_gb": [16.0] * 30,
        }
        capacity_port = MagicMock()
        capacity_port.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "autoscaler_enabled": False,
        }

        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=metrics_port, capacity_port=capacity_port
        )
        result = use_case.forecast(ClusterCapacityCeilingForecastCommand(window_days=30))

        assert result.window_days_used == 30  # noqa: PLR2004

    def test_forecast_empty_usage_raises(self) -> None:
        import pytest
        from hexawyn.domain.errors import InsufficientDataError

        metrics_port = MagicMock()
        metrics_port.get_daily_usage.return_value = {
            "cpu_daily_cores": [],
            "memory_daily_gb": [],
        }
        capacity_port = MagicMock()
        capacity_port.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "autoscaler_enabled": False,
        }

        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=metrics_port, capacity_port=capacity_port
        )

        with pytest.raises(InsufficientDataError):
            use_case.forecast(ClusterCapacityCeilingForecastCommand())
