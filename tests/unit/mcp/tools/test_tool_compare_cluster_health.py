"""Unit tests for MCP tool: compare_cluster_health."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCompareClusterHealthTool:
    def test_compare_cluster_health_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

        with patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()):
            result = compare_cluster_health()

        assert isinstance(result, dict)
        assert "error" in result

    def test_compare_cluster_health_handles_error(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compare_cluster_health()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_compare_cluster_health_success_path(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

        mock_comparison = MagicMock()
        mock_comparison.worse_cluster = "cluster-a"
        mock_comparison.reason = "higher failures"
        mock_comparison.delta_failing_pods = 2
        mock_comparison.delta_cpu_pct = 5.0
        mock_comparison.delta_active_incidents = 1
        mock_comparison.normalized_a_failing_per_100 = 1.0
        mock_comparison.normalized_b_failing_per_100 = 3.0
        mock_result = MagicMock()
        mock_result.comparison = mock_comparison
        mock_result.cluster_a = MagicMock()
        mock_result.cluster_a.cluster_name = "cluster-a"
        mock_result.cluster_a.failing_pods = 1
        mock_result.cluster_a.total_pods = 100
        mock_result.cluster_a.cpu_utilization_pct = 50.0
        mock_result.cluster_a.memory_utilization_pct = 60.0
        mock_result.cluster_a.node_count = 5
        mock_result.cluster_a.nodes_not_ready = 0
        mock_result.cluster_a.active_incidents = 0
        mock_result.cluster_a.health_status = "Healthy"
        mock_result.cluster_a.in_maintenance = False
        mock_result.cluster_a.reachable = True
        mock_result.cluster_b = MagicMock()
        mock_result.cluster_b.cluster_name = "cluster-b"
        mock_result.cluster_b.failing_pods = 3
        mock_result.cluster_b.total_pods = 100
        mock_result.cluster_b.cpu_utilization_pct = 55.0
        mock_result.cluster_b.memory_utilization_pct = 65.0
        mock_result.cluster_b.node_count = 5
        mock_result.cluster_b.nodes_not_ready = 0
        mock_result.cluster_b.active_incidents = 1
        mock_result.cluster_b.health_status = "Healthy"
        mock_result.cluster_b.in_maintenance = False
        mock_result.cluster_b.reachable = True
        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_fleet_health_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.compare_cluster_health.CompareClusterHealthUseCase",
                return_value=mock_uc,
            ),
        ):
            result = compare_cluster_health()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compare_cluster_health")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
