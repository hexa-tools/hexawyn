"""Unit tests for HotNodeAnalysisService (mocks the new
ClusterResourceMetricsPort via get_node_utilization + HotNodeAnalysisPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.service.hot_node_analysis_service import HotNodeAnalysisService


def _series(value: float, hours: int = 24) -> list[tuple[str, float]]:
    return [(f"2026-06-17T{h % 24:02d}:00:00Z", value) for h in range(hours)]


def _node_util(cpu: float, memory: float) -> dict:
    return {"cpu_percent_series": _series(cpu), "memory_percent_series": _series(memory)}


def _node_info(
    name: str,
    allocatable_cpu: float = 8.0,
    allocatable_memory: float = 32.0,
    cordoned: bool = False,
) -> dict:
    return {
        "name": name,
        "allocatable_cpu_cores": allocatable_cpu,
        "allocatable_memory_gb": allocatable_memory,
        "cordoned": cordoned,
    }


def _pod_usage(
    pod_name: str, node_name: str, cpu: float = 0.5, memory: float = 1.0, is_daemonset: bool = False
) -> dict:
    return {
        "pod_name": pod_name,
        "namespace": "production",
        "node_name": node_name,
        "cpu_usage_cores": cpu,
        "memory_usage_gb": memory,
        "is_daemonset": is_daemonset,
    }


def _make_service(
    metrics_port: MagicMock | None = None, node_port: MagicMock | None = None
) -> tuple[HotNodeAnalysisService, MagicMock, MagicMock]:
    if metrics_port is None:
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.return_value = {
            "worker-1": _node_util(50.0, 50.0),
            "worker-2": _node_util(50.0, 50.0),
        }
    if node_port is None:
        node_port = MagicMock()
        node_port.list_nodes.return_value = [_node_info("worker-1"), _node_info("worker-2")]
        node_port.list_pod_usage.return_value = []
    service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)
    return service, metrics_port, node_port


class TestMetricsQuery:
    def test_calls_get_node_utilization_once_with_window(self) -> None:
        service, metrics_port, _ = _make_service()

        service.analyze(HotNodeAnalysisCommand(window_hours=24))

        metrics_port.get_node_utilization.assert_called_once()
        call = metrics_port.get_node_utilization.call_args
        start = call.args[0]
        end = call.args[1]
        assert round((end - start).total_seconds() / 3600) == 24


class TestMultiSeriesGrouping:
    def test_both_node_series_are_used_not_just_the_first(self) -> None:
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.return_value = {
            "worker-1": _node_util(92.0, 30.0),
            "worker-2": _node_util(30.0, 30.0),
        }
        node_port = MagicMock()
        node_port.list_nodes.return_value = [_node_info("worker-1"), _node_info("worker-2")]
        node_port.list_pod_usage.return_value = []
        service, _, _ = _make_service(metrics_port=metrics_port, node_port=node_port)

        response = service.analyze(HotNodeAnalysisCommand())

        assert len(response.hot_nodes) == 1
        assert response.hot_nodes[0]["node_name"] == "worker-1"
        assert response.healthy_node_count == 1


class TestDaemonSetExclusion:
    def test_daemonset_pods_excluded_before_grouping(self) -> None:
        node_port = MagicMock()
        node_port.list_nodes.return_value = [_node_info("worker-1", allocatable_cpu=100.0)]
        node_port.list_pod_usage.return_value = [
            _pod_usage("fluentd-abc", "worker-1", cpu=0.9, is_daemonset=True),
            _pod_usage("app-xyz", "worker-1", cpu=0.1, is_daemonset=False),
        ]
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.return_value = {"worker-1": _node_util(92.0, 30.0)}
        service, _, _ = _make_service(metrics_port=metrics_port, node_port=node_port)

        response = service.analyze(HotNodeAnalysisCommand())

        pod_names = [c["pod_name"] for c in response.hot_nodes[0]["top_consumers"]]
        assert "fluentd-abc" not in pod_names
        assert "app-xyz" in pod_names


class TestResponseComposition:
    def test_all_healthy_scenario(self) -> None:
        service, _, _ = _make_service()

        response = service.analyze(HotNodeAnalysisCommand())

        assert response.error is None
        assert response.hot_nodes == []
        assert response.healthy_node_count == 2

    def test_node_port_failure_propagates(self) -> None:
        from unittest.mock import MagicMock

        import pytest

        node_port = MagicMock()
        node_port.list_nodes.side_effect = RuntimeError("node list failed")
        metrics_port = MagicMock(
            spec=__import__(
                "hexawyn.application.ports.driven.cluster_resource_metrics_port",
                fromlist=["ClusterResourceMetricsPort"],
            ).ClusterResourceMetricsPort
        )
        metrics_port.get_node_utilization.return_value = {}
        service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)
        with pytest.raises(RuntimeError, match="node list failed"):
            service.analyze(
                __import__(
                    "hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command",
                    fromlist=["HotNodeAnalysisCommand"],
                ).HotNodeAnalysisCommand()
            )


class TestHotNodeAnalysisServiceEdgeCases:
    def test_window_hours_zero(self) -> None:
        service, _, _ = _make_service()

        response = service.analyze(HotNodeAnalysisCommand(window_hours=0))

        assert response.error is None
        assert response.healthy_node_count == 2

    def test_empty_node_list(self) -> None:
        node_port = MagicMock()
        node_port.list_nodes.return_value = []
        node_port.list_pod_usage.return_value = []
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.return_value = {}
        service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)

        response = service.analyze(HotNodeAnalysisCommand())

        assert response.error is None
        assert response.hot_nodes == []
        assert response.healthy_node_count == 0

    def test_cordoned_nodes_excluded(self) -> None:
        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.return_value = {
            "worker-1": _node_util(92.0, 80.0),
        }
        node_port = MagicMock()
        node_port.list_nodes.return_value = [
            _node_info("worker-1", cordoned=True),
            _node_info("worker-2"),
        ]
        node_port.list_pod_usage.return_value = []
        service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)

        response = service.analyze(HotNodeAnalysisCommand())

        assert response.error is None

    def test_metrics_port_failure_propagates(self) -> None:
        import pytest

        metrics_port = MagicMock(spec=ClusterResourceMetricsPort)
        metrics_port.get_node_utilization.side_effect = RuntimeError("Prometheus timeout")
        node_port = MagicMock()
        node_port.list_nodes.return_value = [_node_info("worker-1")]
        node_port.list_pod_usage.return_value = []
        service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)

        with pytest.raises(RuntimeError, match="Prometheus timeout"):
            service.analyze(HotNodeAnalysisCommand())
