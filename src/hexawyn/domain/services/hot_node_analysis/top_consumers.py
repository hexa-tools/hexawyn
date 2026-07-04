from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import TopConsumer


def select_top_consumers(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, reverse=True)[:count]
