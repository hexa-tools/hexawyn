"""E2E tests: namespace_overview — real namespace statistics.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
    KubernetesNamespaceAdapter,
)

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestNamespaceOverviewE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KubernetesNamespaceAdapter()

    def test_get_overview_returns_data(self, healthy_deployment: str) -> None:
        overview = self._adapter.get_namespace_overview_data(NAMESPACE)

        assert "namespace_status" in overview
        assert overview["namespace_status"] == "Active"

    def test_overview_includes_pods(self, healthy_deployment: str) -> None:
        overview = self._adapter.get_namespace_overview_data(NAMESPACE)

        assert "pods" in overview
        assert len(overview["pods"]) >= 1, "Expected at least 1 pod in namespace"

        pod_names = {p["name"] for p in overview["pods"]}
        assert any(
            name.startswith("healthy-app") for name in pod_names
        ), "Expected healthy-app pods in namespace overview"

    def test_overview_includes_deployments(self, healthy_deployment: str) -> None:
        overview = self._adapter.get_namespace_overview_data(NAMESPACE)

        assert "deployments" in overview
        deployments = overview["deployments"]
        assert len(deployments) >= 1

        dep_names = {d["name"] for d in deployments}
        assert "healthy-app" in dep_names

    def test_non_existent_namespace_raises(self, k8s_cluster_ready: bool) -> None:
        from hexawyn.domain.errors import ResourceNotFoundError

        with pytest.raises(ResourceNotFoundError):
            self._adapter.get_namespace_overview_data("does-not-exist-e2e-ns")
