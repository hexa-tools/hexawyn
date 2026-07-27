from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestClusterCapacityCeilingForecastMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        mock_metrics = MagicMock()
        mock_metrics.get_daily_usage.return_value = {
            "cpu_daily_cores": [10.0, 12.0, 15.0],
            "memory_daily_gb": [16.0, 18.0, 20.0],
        }
        mock_capacity = MagicMock()
        mock_capacity.get_cluster_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "autoscaler_enabled": True,
        }

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=mock_metrics,
            ),
            patch(
                "hexawyn.mcp.server.build_capacity_forecast_adapter",
                return_value=mock_capacity,
            ),
        ):
            result = cluster_capacity_ceiling_forecast()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["window_days_used"] > 0

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
            side_effect=RuntimeError("prometheus unreachable"),
        ):
            result = cluster_capacity_ceiling_forecast()

        assert isinstance(result, dict)
        assert "prometheus unreachable" in str(result["error"])
