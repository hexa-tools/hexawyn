from __future__ import annotations

from hexawyn.application.ports.driven.hot_node_analysis_port import PodUsageRaw
from hexawyn.domain.models.hot_node_analysis import TopConsumer


class TestNodeSeries:
    def test_happy_path_returns_series_for_known_node(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import node_series

        series = {
            "node-1": {
                "cpu_percent_series": [("2026-01-01T00:00:00Z", 80.0)],
                "memory_percent_series": [("2026-01-01T00:00:00Z", 60.0)],
            },
        }

        result = node_series(series, "node-1")

        assert result["cpu_percent_series"] == [("2026-01-01T00:00:00Z", 80.0)]
        assert result["memory_percent_series"] == [("2026-01-01T00:00:00Z", 60.0)]

    def test_unknown_node_returns_empty_series(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import node_series

        result = node_series({}, "missing-node")

        assert result["cpu_percent_series"] == []
        assert result["memory_percent_series"] == []

    def test_empty_dict_returns_empty_series(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import node_series

        result = node_series({}, "any-node")

        assert result["cpu_percent_series"] == []
        assert result["memory_percent_series"] == []

    def test_none_based_result_does_not_raise(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import node_series

        result = node_series({"other": None}, "absent")  # type: ignore[dict-item]

        assert result["cpu_percent_series"] == []
        assert result["memory_percent_series"] == []


class TestGroupNonDaemonsetPods:
    def test_happy_path_groups_pods_by_node(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": "app-1",
                "namespace": "default",
                "node_name": "node-a",
                "cpu_usage_cores": 2.0,
                "memory_usage_gb": 4.0,
                "is_daemonset": False,
            },
            {
                "pod_name": "app-2",
                "namespace": "default",
                "node_name": "node-a",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 2.0,
                "is_daemonset": False,
            },
            {
                "pod_name": "app-3",
                "namespace": "kube-system",
                "node_name": "node-b",
                "cpu_usage_cores": 0.5,
                "memory_usage_gb": 1.0,
                "is_daemonset": False,
            },
        ]

        result = group_non_daemonset_pods(pods)

        assert "node-a" in result
        assert "node-b" in result
        assert len(result["node-a"]) == 2  # noqa: PLR2004
        assert len(result["node-b"]) == 1
        assert result["node-a"][0].pod_name == "app-1"

    def test_daemonset_pods_excluded(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": "fluentd",
                "namespace": "kube-system",
                "node_name": "node-a",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 2.0,
                "is_daemonset": True,
            },
            {
                "pod_name": "app",
                "namespace": "default",
                "node_name": "node-a",
                "cpu_usage_cores": 2.0,
                "memory_usage_gb": 4.0,
                "is_daemonset": False,
            },
        ]

        result = group_non_daemonset_pods(pods)

        assert len(result["node-a"]) == 1
        assert result["node-a"][0].pod_name == "app"

    def test_empty_pod_list_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        result = group_non_daemonset_pods([])

        assert result == {}

    def test_all_daemonsets_returns_empty(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": "ds-1",
                "namespace": "kube-system",
                "node_name": "node-a",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 1.0,
                "is_daemonset": True,
            },
            {
                "pod_name": "ds-2",
                "namespace": "kube-system",
                "node_name": "node-b",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 1.0,
                "is_daemonset": True,
            },
        ]

        result = group_non_daemonset_pods(pods)

        assert result == {}

    def test_result_contains_top_consumer_instances(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": "single",
                "namespace": "ns",
                "node_name": "n1",
                "cpu_usage_cores": 3.5,
                "memory_usage_gb": 8.0,
                "is_daemonset": False,
            },
        ]

        result = group_non_daemonset_pods(pods)

        consumer = result["n1"][0]
        assert isinstance(consumer, TopConsumer)
        assert consumer.pod_name == "single"
        assert consumer.namespace == "ns"
        assert consumer.cpu_usage_cores == 3.5  # noqa: PLR2004
        assert consumer.memory_usage_gb == 8.0  # noqa: PLR2004

    def test_multiple_nodes_correctly_separated(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": f"pod-{i}",
                "namespace": "ns",
                "node_name": f"node-{i}",
                "cpu_usage_cores": 1.0,
                "memory_usage_gb": 1.0,
                "is_daemonset": False,
            }
            for i in range(5)
        ]

        result = group_non_daemonset_pods(pods)

        assert len(result) == 5  # noqa: PLR2004
        for i in range(5):
            assert len(result[f"node-{i}"]) == 1

    def test_zero_cpu_memory_values_accepted(self) -> None:
        from hexawyn.domain.services.hot_node_analysis.pod_grouper import (
            group_non_daemonset_pods,
        )

        pods: list[PodUsageRaw] = [
            {
                "pod_name": "idle",
                "namespace": "ns",
                "node_name": "node-x",
                "cpu_usage_cores": 0.0,
                "memory_usage_gb": 0.0,
                "is_daemonset": False,
            },
        ]

        result = group_non_daemonset_pods(pods)

        consumer = result["node-x"][0]
        assert consumer.cpu_usage_cores == 0.0
        assert consumer.memory_usage_gb == 0.0
