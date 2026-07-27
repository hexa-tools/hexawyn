from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestClusterHeadroomSimulationMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import (
            cluster_headroom_simulation,
        )

        mock_metrics = MagicMock()
        mock_metrics.get_current_usage.return_value = {
            "cpu_cores": 8.0,
            "memory_gb": 16.0,
        }
        mock_headroom = MagicMock()
        mock_headroom.get_node_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "node_count": 4,
            "largest_node_cpu_cores": 8.0,
            "largest_node_memory_gb": 16.0,
            "autoscaler_enabled": True,
        }

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=mock_metrics,
            ),
            patch(
                "hexawyn.mcp.server.build_headroom_simulation_adapter",
                return_value=mock_headroom,
            ),
        ):
            result = cluster_headroom_simulation()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["verdict"] is not None

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import (
            cluster_headroom_simulation,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
            side_effect=RuntimeError("metrics unavailable"),
        ):
            result = cluster_headroom_simulation()

        assert isinstance(result, dict)
        assert "metrics unavailable" in str(result["error"])
