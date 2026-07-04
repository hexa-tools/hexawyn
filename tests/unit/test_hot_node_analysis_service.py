"""Unit tests for HotNodeAnalysisService (mocks the existing MetricsQueryPort
[ECA-31, reused via range_query] + the new HotNodeAnalysisPort). This service
is the first caller in the codebase to walk multiple returned Prometheus
series instead of indexing samples[0]."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.service.hot_node_analysis_service import HotNodeAnalysisService


def _series(value: float, hours: int = 24) -> list[tuple[str, float]]:
    return [(f"2026-06-17T{h % 24:02d}:00:00Z", value) for h in range(hours)]


def _range_sample(node_label: str, values: list[tuple[str, float]]) -> dict:
    return {"metric": {"instance": node_label}, "values": values}


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
        metrics_port = MagicMock()
        metrics_port.range_query.side_effect = [
            [_range_sample("worker-1", _series(50.0)), _range_sample("worker-2", _series(50.0))],
            [_range_sample("worker-1", _series(50.0)), _range_sample("worker-2", _series(50.0))],
        ]
    if node_port is None:
        node_port = MagicMock()
        node_port.list_nodes.return_value = [_node_info("worker-1"), _node_info("worker-2")]
        node_port.list_pod_usage.return_value = []
    service = HotNodeAnalysisService(metrics_port=metrics_port, node_port=node_port)
    return service, metrics_port, node_port


class TestPrometheusQueries:
    def test_calls_range_query_twice_with_hourly_step(self) -> None:
        service, metrics_port, _ = _make_service()

        service.analyze(HotNodeAnalysisCommand())

        assert metrics_port.range_query.call_count == 2
        for call in metrics_port.range_query.call_args_list:
            assert call.kwargs.get("step", call.args[3] if len(call.args) > 3 else None) == "1h"


class TestMultiSeriesGrouping:
    def test_both_node_series_are_used_not_just_the_first(self) -> None:
        """The distinguishing new behavior — unlike ECA-74/75, this service
        must not hard-index samples[0]."""
        metrics_port = MagicMock()
        metrics_port.range_query.side_effect = [
            [
                _range_sample("worker-1", _series(92.0)),
                _range_sample("worker-2", _series(30.0)),
            ],
            [
                _range_sample("worker-1", _series(30.0)),
                _range_sample("worker-2", _series(30.0)),
            ],
        ]
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
        metrics_port = MagicMock()
        metrics_port.range_query.side_effect = [
            [_range_sample("worker-1", _series(92.0))],
            [_range_sample("worker-1", _series(30.0))],
        ]
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
