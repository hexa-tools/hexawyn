"""E2E tests: crashloop_scenario — real pods on real k3d cluster.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).
Marked with @pytest.mark.e2e — run manually, never in CI.

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestCrashloopE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaAdapter("k3d-hexawyn-e2e")

    def test_list_pods_detects_crashloop(self, crashloop_pod: str) -> None:
        pods = self._adapter.list_pods(namespace=NAMESPACE)

        crashloop_pods = [p for p in pods if p.get("status", "") == "CrashLoop"]
        assert len(crashloop_pods) >= 1, "Expected at least one CrashLoopBackOff pod"
        assert crashloop_pods[0]["name"] == "crashloop-test"

    def test_list_pods_detects_pending(self, pending_pod: str) -> None:
        pods = self._adapter.list_pods(namespace=NAMESPACE)

        pending = [p for p in pods if p.get("status", "") == "Pending"]
        assert any(
            p["name"] == "pending-test" for p in pending
        ), "Expected pending-test pod in Pending state"

    def test_list_pods_sees_healthy(self, healthy_deployment: str) -> None:
        pods = self._adapter.list_pods(namespace=NAMESPACE)

        running = [p for p in pods if p.get("status", "") == "Running"]
        healthy_pods = [p for p in running if p["name"].startswith("healthy-app")]
        assert len(healthy_pods) >= 1, "Expected at least one healthy-app pod Running"

    def test_list_namespace_pods_isolation(self, k8s_cluster_ready: bool) -> None:
        pods = self._adapter.list_pods(namespace="kube-system")

        assert len(pods) >= 1, "kube-system should have pods"
        assert all(
            p["namespace"] == "kube-system" for p in pods
        ), "All pods should be in kube-system namespace"
