from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestClusterHeadroomSimulationTool:
    def test_returns_simulation(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import cluster_headroom_simulation

        with (
            patch("hexawyn.mcp.server.build_metrics_query_adapter") as build_metrics,
            patch("hexawyn.mcp.server.build_headroom_simulation_adapter") as build_headroom,
        ):
            metrics_port = MagicMock()
            metrics_port.instant_query.side_effect = [
                [{"metric": {}, "value": 48.0}],
                [{"metric": {}, "value": 192.0}],
            ]
            build_metrics.return_value = metrics_port

            headroom_port = MagicMock()
            headroom_port.get_node_capacity_info.return_value = {
                "total_allocatable_cpu_cores": 80.0,
                "total_allocatable_memory_gb": 320.0,
                "node_count": 10,
                "largest_node_cpu_cores": 8.0,
                "largest_node_memory_gb": 32.0,
                "autoscaler_enabled": False,
            }
            build_headroom.return_value = headroom_port

            result = cluster_headroom_simulation(
                proposed_workloads=[
                    {
                        "name": "analytics-service",
                        "cpu_request_per_pod": "500m",
                        "memory_request_per_pod": "512Mi",
                    }
                ]
            )

        assert result["error"] is None
        assert result["verdict"] == "fits"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import cluster_headroom_simulation

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            side_effect=RuntimeError("Prometheus unavailable"),
        ):
            result = cluster_headroom_simulation()

        assert "Prometheus unavailable" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cluster_headroom_simulation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
