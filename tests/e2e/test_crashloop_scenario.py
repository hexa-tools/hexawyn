"""E2E tests: crashloop_scenario — real pods on real k3d cluster.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).
Marked with @pytest.mark.e2e — run manually, never in CI.

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import time

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

NAMESPACE = "hexawyn-test"


def _poll_for_pod_status(
    adapter: VanillaAdapter,
    namespace: str,
    pod_name: str,
    expected_status: str,
    timeout: float = 45.0,
) -> dict[str, object] | None:
    """Poll until a pod reaches the expected status.

    A CrashLoopBackOff pod only reads as ``CrashLoop`` while it is in the
    (long) backoff wait; during the brief running burst between crashes the
    adapter honestly reports the pod phase (``Running``). Polling across the
    cycle makes the assertion deterministic.
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        for pod in adapter.list_pods(namespace=namespace):
            if pod.get("name") == pod_name and pod.get("status") == expected_status:
                return pod
        time.sleep(1.0)
    return None


@pytest.mark.e2e
class TestCrashloopE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaAdapter("k3d-hexawyn-e2e")

    def test_list_pods_detects_crashloop(self, crashloop_pod: str) -> None:
        pod = _poll_for_pod_status(self._adapter, NAMESPACE, "crashloop-test", "CrashLoop")

        assert pod is not None, "Expected at least one CrashLoopBackOff pod"
        assert pod["name"] == "crashloop-test"

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
