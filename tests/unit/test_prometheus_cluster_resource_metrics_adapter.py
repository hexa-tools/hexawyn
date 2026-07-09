from datetime import UTC, datetime
from unittest.mock import MagicMock

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort


def _start_end() -> tuple[datetime, datetime]:
    end = datetime(2026, 1, 10, tzinfo=UTC)
    start = datetime(2026, 1, 1, tzinfo=UTC)
    return start, end


class TestGetCurrentUsage:
    def test_returns_cpu_and_memory_from_instant_queries(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.instant_query.side_effect = [
            [{"metric": {}, "value": 12.5}],
            [{"metric": {}, "value": 48.0}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)

        usage = adapter.get_current_usage(timeout_seconds=15.0)

        assert usage == {"cpu_cores": 12.5, "memory_gb": 48.0}
        assert metrics.instant_query.call_count == 2

    def test_returns_zero_when_no_samples(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.instant_query.return_value = []
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)

        usage = adapter.get_current_usage(timeout_seconds=15.0)

        assert usage == {"cpu_cores": 0.0, "memory_gb": 0.0}


class TestGetDailyUsage:
    def test_extracts_daily_series_with_day_step(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.range_query.side_effect = [
            [{"metric": {}, "values": [("t1", 1.0), ("t2", 2.0)]}],
            [{"metric": {}, "values": [("t1", 3.0), ("t2", 4.0)]}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)
        start, end = _start_end()

        daily = adapter.get_daily_usage(start, end, timeout_seconds=15.0)

        assert daily == {"cpu_daily_cores": [1.0, 2.0], "memory_daily_gb": [3.0, 4.0]}
        assert metrics.range_query.call_args_list[0].kwargs["step"] == "1d"

    def test_returns_empty_lists_when_no_samples(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.range_query.return_value = []
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)
        start, end = _start_end()

        daily = adapter.get_daily_usage(start, end, timeout_seconds=15.0)

        assert daily == {"cpu_daily_cores": [], "memory_daily_gb": []}


class TestGetNodeUtilization:
    def test_groups_series_by_node_with_hour_step(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.range_query.side_effect = [
            [{"metric": {"instance": "node-a"}, "values": [("t1", 80.0)]}],
            [{"metric": {"instance": "node-a"}, "values": [("t1", 55.0)]}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)
        start, end = _start_end()

        result = adapter.get_node_utilization(start, end, timeout_seconds=15.0)

        assert result["node-a"]["cpu_percent_series"] == [("t1", 80.0)]
        assert result["node-a"]["memory_percent_series"] == [("t1", 55.0)]
        assert metrics.range_query.call_args_list[0].kwargs["step"] == "1h"

    def test_uses_node_label_fallback_and_unknown(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )

        metrics = MagicMock(spec=MetricsQueryPort)
        metrics.range_query.side_effect = [
            [{"metric": {"node": "node-b"}, "values": [("t1", 10.0)]}],
            [{"metric": {}, "values": [("t1", 20.0)]}],
        ]
        adapter = PrometheusClusterResourceMetricsAdapter(metrics_query_port=metrics)
        start, end = _start_end()

        result = adapter.get_node_utilization(start, end, timeout_seconds=15.0)

        assert result["node-b"]["cpu_percent_series"] == [("t1", 10.0)]
        assert result["unknown"]["memory_percent_series"] == [("t1", 20.0)]
