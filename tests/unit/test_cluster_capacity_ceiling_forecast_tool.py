from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)


class TestClusterCapacityCeilingForecastTool:
    def test_returns_forecast(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with (
            patch("hexawyn.mcp.server.build_cluster_resource_metrics_adapter") as build_metrics,
            patch("hexawyn.mcp.server.build_capacity_forecast_adapter") as build_capacity,
        ):
            metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
            metrics_port.get_daily_usage.return_value = {
                "cpu_daily_cores": [50.0] * 14,
                "memory_daily_gb": [50.0] * 14,
            }
            build_metrics.return_value = metrics_port

            capacity_port = MagicMock()
            capacity_port.get_cluster_capacity_info.return_value = {
                "total_allocatable_cpu_cores": 96.0,
                "total_allocatable_memory_gb": 384.0,
                "autoscaler_enabled": False,
            }
            build_capacity.return_value = capacity_port

            result = cluster_capacity_ceiling_forecast()

        assert result["error"] is None
        assert result["confidence"] == "high"

    def test_insufficient_data_surfaces_as_error(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with (
            patch("hexawyn.mcp.server.build_cluster_resource_metrics_adapter") as build_metrics,
            patch("hexawyn.mcp.server.build_capacity_forecast_adapter") as build_capacity,
        ):
            metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
            metrics_port.get_daily_usage.return_value = {
                "cpu_daily_cores": [],
                "memory_daily_gb": [],
            }
            build_metrics.return_value = metrics_port

            capacity_port = MagicMock()
            capacity_port.get_cluster_capacity_info.return_value = {
                "total_allocatable_cpu_cores": 96.0,
                "total_allocatable_memory_gb": 384.0,
                "autoscaler_enabled": False,
            }
            build_capacity.return_value = capacity_port

            result = cluster_capacity_ceiling_forecast()

        assert result["error"] is not None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
            side_effect=RuntimeError("Prometheus unavailable"),
        ):
            result = cluster_capacity_ceiling_forecast()

        assert "Prometheus unavailable" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cluster_capacity_ceiling_forecast")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
