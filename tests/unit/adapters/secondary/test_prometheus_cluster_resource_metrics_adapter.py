from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
    PrometheusClusterResourceMetricsAdapter,
)
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)


class TestPrometheusClusterResourceMetricsAdapter:
    def test_implements_port(self) -> None:
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=Mock())
        assert isinstance(adapter, ClusterResourceMetricsPort)

    def test_get_current_usage(self) -> None:
        metrics_port = Mock()
        metrics_port.instant_query.side_effect = [
            [{"metric": {}, "value": 12.5}],
            [{"metric": {}, "value": 64.0}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics_port)
        result = adapter.get_current_usage(timeout_seconds=15.0)
        assert result["cpu_cores"] == 12.5  # noqa: PLR2004
        assert result["memory_gb"] == 64.0  # noqa: PLR2004

    def test_get_current_usage_no_samples(self) -> None:
        metrics_port = Mock()
        metrics_port.instant_query.return_value = []
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics_port)
        result = adapter.get_current_usage(timeout_seconds=15.0)
        assert result["cpu_cores"] == 0.0
        assert result["memory_gb"] == 0.0

    def test_get_daily_usage(self) -> None:
        metrics_port = Mock()
        metrics_port.range_query.side_effect = [
            [
                {
                    "metric": {},
                    "values": [("2024-01-01T00:00:00Z", 10.0), ("2024-01-02T00:00:00Z", 12.0)],
                }
            ],
            [
                {
                    "metric": {},
                    "values": [("2024-01-01T00:00:00Z", 50.0), ("2024-01-02T00:00:00Z", 55.0)],
                }
            ],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics_port)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 3, tzinfo=UTC)
        result = adapter.get_daily_usage(start=start, end=end, timeout_seconds=15.0)
        assert result["cpu_daily_cores"] == [10.0, 12.0]
        assert result["memory_daily_gb"] == [50.0, 55.0]

    def test_get_node_utilization(self) -> None:
        metrics_port = Mock()
        metrics_port.range_query.side_effect = [
            [{"metric": {"instance": "node-1"}, "values": [("t1", 45.0)]}],
            [{"metric": {"instance": "node-1"}, "values": [("t1", 60.0)]}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics_port)
        start = datetime(2024, 1, 1, tzinfo=UTC)
        end = datetime(2024, 1, 2, tzinfo=UTC)
        result = adapter.get_node_utilization(start=start, end=end, timeout_seconds=15.0)
        assert "node-1" in result
        assert result["node-1"]["cpu_percent_series"] == [("t1", 45.0)]
        assert result["node-1"]["memory_percent_series"] == [("t1", 60.0)]
