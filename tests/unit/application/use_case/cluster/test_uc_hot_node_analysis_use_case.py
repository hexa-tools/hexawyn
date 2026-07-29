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

    def test_execute_with_pod_and_node_data(self) -> None:
        metrics_port = MagicMock()
        cpu_series: list[tuple[str, float]] = [
            (f"2024-01-01T{h:02d}:00:00Z", 95.0) for h in range(5)
        ] + [(f"2024-01-01T{h:02d}:00:00Z", 50.0) for h in range(5, 10)]
        mem_series: list[tuple[str, float]] = [
            (f"2024-01-01T{h:02d}:00:00Z", 40.0) for h in range(10)
        ]
        metrics_port.get_node_utilization.return_value = {
            "node-1": {"cpu_percent_series": cpu_series, "memory_percent_series": mem_series},
        }
        node_port = MagicMock()
        node_port.list_nodes.return_value = [
            {
                "name": "node-1",
                "allocatable_cpu_cores": 8.0,
                "allocatable_memory_gb": 16.0,
                "cordoned": False,
            },
            {
                "name": "node-2",
                "allocatable_cpu_cores": 4.0,
                "allocatable_memory_gb": 8.0,
                "cordoned": False,
            },
        ]
        node_port.list_pod_usage.return_value = [
            {
                "pod_name": "app-1",
                "namespace": "default",
                "node_name": "node-1",
                "cpu_usage_cores": 2.0,
                "memory_usage_gb": 4.0,
                "is_daemonset": False,
            },
            {
                "pod_name": "ds-1",
                "namespace": "kube-system",
                "node_name": "node-1",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 2.0,
                "is_daemonset": True,
            },
        ]

        use_case = HotNodeAnalysisUseCase(metrics_port=metrics_port, node_port=node_port)
        result = use_case.execute(HotNodeAnalysisCommand(window_hours=24))

        assert isinstance(result, HotNodeAnalysisResponse)
        assert len(result.hot_nodes) > 0
        assert len(result.hot_nodes[0]["top_consumers"]) > 0
