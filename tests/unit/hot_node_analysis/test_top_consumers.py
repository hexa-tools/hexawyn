"""Unit tests for select_top_consumers — pure sort-and-slice."""

from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import TopConsumer
from hexawyn.domain.services.hot_node_analysis.top_consumers import select_top_consumers


def _consumer(name: str, cpu: float) -> TopConsumer:
    return TopConsumer(
        pod_name=name, namespace="production", cpu_usage_cores=cpu, memory_usage_gb=1.0
    )


class TestSelectTopConsumers:
    def test_sorts_by_cpu_usage_descending(self) -> None:
        pods = [_consumer("small", 0.2), _consumer("large", 0.8), _consumer("medium", 0.5)]

        top = select_top_consumers(pods, count=3)

        assert [p.pod_name for p in top] == ["large", "medium", "small"]

    def test_slices_to_requested_count(self) -> None:
        pods = [_consumer("a", 0.9), _consumer("b", 0.7), _consumer("c", 0.5), _consumer("d", 0.3)]

        top = select_top_consumers(pods, count=2)

        assert [p.pod_name for p in top] == ["a", "b"]

    def test_fewer_pods_than_requested_count_returns_all(self) -> None:
        pods = [_consumer("only", 0.5)]

        top = select_top_consumers(pods, count=3)

        assert len(top) == 1

    def test_empty_pods_returns_empty(self) -> None:
        assert select_top_consumers([], count=3) == []
