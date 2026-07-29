from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestHotNodeAnalysisMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        mock_metrics = MagicMock()
        mock_metrics.get_node_utilization.return_value = {}
        mock_node = MagicMock()
        mock_node.list_nodes.return_value = []
        mock_node.list_pod_usage.return_value = []

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=mock_metrics,
            ),
            patch(
                "hexawyn.mcp.server.build_node_analysis_adapter",
                return_value=mock_node,
            ),
        ):
            result = hot_node_analysis()

        assert isinstance(result, dict)
        assert result["error"] is None

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        with patch(
            "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
            side_effect=RuntimeError("metrics overloaded"),
        ):
            result = hot_node_analysis()

        assert isinstance(result, dict)
        assert "metrics overloaded" in str(result["error"])
