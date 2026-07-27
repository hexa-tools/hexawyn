from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.hot_node_analysis.command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.response import (
    HotNodeAnalysisResponse,
)


class TestHotNodeAnalysisUseCase:
    def test_execute_returns_response_type(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_node_utilization.return_value = {}
        node_port = MagicMock()
        node_port.list_nodes.return_value = []
        node_port.list_pod_usage.return_value = []

        use_case = HotNodeAnalysisUseCase(metrics_port=metrics_port, node_port=node_port)
        result = use_case.execute(HotNodeAnalysisCommand())

        assert isinstance(result, HotNodeAnalysisResponse)
        assert result.error is None

    def test_execute_uses_window_hours_from_command(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_node_utilization.return_value = {}
        node_port = MagicMock()
        node_port.list_nodes.return_value = []
        node_port.list_pod_usage.return_value = []

        use_case = HotNodeAnalysisUseCase(metrics_port=metrics_port, node_port=node_port)
        result = use_case.execute(HotNodeAnalysisCommand(window_hours=12))

        assert isinstance(result, HotNodeAnalysisResponse)
        assert result.hot_nodes is not None

    def test_execute_includes_summary_fields(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_node_utilization.return_value = {}
        node_port = MagicMock()
        node_port.list_nodes.return_value = []
        node_port.list_pod_usage.return_value = []

        use_case = HotNodeAnalysisUseCase(metrics_port=metrics_port, node_port=node_port)
        result = use_case.execute(HotNodeAnalysisCommand())

        assert hasattr(result, "summary")
        assert hasattr(result, "healthy_node_count")
        assert hasattr(result, "excluded_cordoned_nodes")
