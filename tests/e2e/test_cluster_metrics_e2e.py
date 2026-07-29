"""E2E tests: cluster_metrics — real cluster resource metrics.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

_MAX_USAGE_PCT = 100.0


@pytest.mark.e2e
class TestClusterMetricsE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaAdapter("k3d-hexawyn-e2e")

    def test_returns_metrics_with_positive_node_count(self) -> None:
        metrics = self._adapter.get_cluster_metrics()

        assert metrics["node_count"] >= 1, "Expected at least 1 node"
        assert metrics["pod_count"] >= 0, "Pod count should be >= 0"

    def test_metrics_have_valid_ranges(self) -> None:
        metrics = self._adapter.get_cluster_metrics()

        assert (
            0.0 <= metrics["cpu_usage_pct"] <= _MAX_USAGE_PCT
        ), f"CPU usage {metrics['cpu_usage_pct']}% out of range"
        assert (
            0.0 <= metrics["memory_usage_pct"] <= _MAX_USAGE_PCT
        ), f"Memory usage {metrics['memory_usage_pct']}% out of range"

    def test_metrics_are_consistent(self) -> None:
        first = self._adapter.get_cluster_metrics()
        second = self._adapter.get_cluster_metrics()

        assert isinstance(first["node_count"], int)
        assert isinstance(second["node_count"], int)
        assert (
            first["node_count"] == second["node_count"]
        ), "Node count should be stable between calls"
