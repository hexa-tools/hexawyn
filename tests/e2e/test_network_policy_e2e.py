"""E2E tests: network_policy — audit network policies on real cluster.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
    KubernetesNetworkPolicyAdapter,
)

NAMESPACE = "hexawyn-test"


def _kubectl_args() -> list[str]:
    import os

    kubeconfig = os.environ.get("KUBECONFIG", "")
    if kubeconfig:
        return ["--kubeconfig", kubeconfig.split(":")[0]]
    return []


@pytest.mark.e2e
class TestNetworkPolicyE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KubernetesNetworkPolicyAdapter()

    def test_list_namespaces_returns_data(self) -> None:
        namespaces = self._adapter.list_namespaces_with_pod_counts()

        assert isinstance(namespaces, list)
        assert len(namespaces) >= 1

        for ns in namespaces:
            assert "name" in ns
            assert "pod_count" in ns
            assert ns["pod_count"] >= 0

    def test_list_network_policies_returns_list(self) -> None:
        policies = self._adapter.list_network_policies()

        assert isinstance(policies, list)
        for p in policies:
            assert "name" in p
            assert "namespace" in p

    def test_calico_global_policies_does_not_crash(self) -> None:
        has_calico = self._adapter.has_calico_global_network_policies()

        assert isinstance(has_calico, bool)

    def test_istio_peer_auth_does_not_crash(self) -> None:
        has_istio = self._adapter.has_istio_strict_peer_authentication()

        assert isinstance(has_istio, bool)

    def test_create_and_detect_network_policy(self, k8s_cluster_ready: bool) -> None:
        import subprocess

        kb = _kubectl_args()
        policy_yaml = """apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: e2e-test-policy
  namespace: hexawyn-test
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector: {}
"""
        subprocess.run(
            ["kubectl", *kb, "apply", "-f", "-"],
            input=policy_yaml,
            text=True,
            capture_output=True,
            check=True,
        )

        try:
            policies = self._adapter.list_network_policies()
            ns_policies = [p for p in policies if p["namespace"] == NAMESPACE]
            assert any(
                p["name"] == "e2e-test-policy" for p in ns_policies
            ), "Expected e2e-test-policy in namespace"
        finally:
            subprocess.run(
                ["kubectl", *kb, "delete", "networkpolicy", "e2e-test-policy", "-n", NAMESPACE],
                capture_output=True,
            )
