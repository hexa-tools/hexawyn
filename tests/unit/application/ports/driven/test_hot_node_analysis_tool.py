from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)


class TestHotNodeAnalysisTool:
    def test_returns_analysis(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        with (
            patch("hexawyn.mcp.server.build_cluster_resource_metrics_adapter") as build_metrics,
            patch("hexawyn.mcp.server.build_node_analysis_adapter") as build_node,
        ):
            metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
            metrics_port.get_node_utilization.return_value = {}
            build_metrics.return_value = metrics_port

            node_port = MagicMock()
            node_port.list_nodes.return_value = []
            node_port.list_pod_usage.return_value = []
            build_node.return_value = node_port

            result = hot_node_analysis()

        assert result["error"] is None
        assert result["hot_nodes"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        with patch(
            "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
            side_effect=RuntimeError("Prometheus unavailable"),
        ):
            result = hot_node_analysis()

        assert "Prometheus unavailable" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.hot_node_analysis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
