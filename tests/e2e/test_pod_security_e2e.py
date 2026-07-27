"""E2E tests: pod_security — audit pod security contexts on real cluster.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
    KubernetesPodSecurityAdapter,
)

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestPodSecurityE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KubernetesPodSecurityAdapter()

    def test_list_pod_security_specs_returns_data(self, healthy_deployment: str) -> None:
        specs = self._adapter.list_pod_security_specs()

        assert isinstance(specs, list)
        assert len(specs) >= 1, "Expected at least 1 pod security spec"

        namespace_specs = [s for s in specs if s["namespace"] == NAMESPACE]
        assert len(namespace_specs) >= 1, f"Expected pods in {NAMESPACE} namespace"

    def test_pod_security_specs_have_required_fields(self, healthy_deployment: str) -> None:
        specs = self._adapter.list_pod_security_specs()

        for spec in specs:
            assert "pod_name" in spec
            assert "namespace" in spec
            assert "host_pid" in spec
            assert "host_network" in spec
            assert "containers" in spec
            assert isinstance(spec["host_pid"], bool)
            assert isinstance(spec["host_network"], bool)

    def test_healthy_pod_has_no_host_namespace(self, healthy_deployment: str) -> None:
        specs = self._adapter.list_pod_security_specs()

        namespace_specs = [s for s in specs if s["namespace"] == NAMESPACE]
        healthy_specs = [s for s in namespace_specs if s["pod_name"].startswith("healthy-app")]

        assert len(healthy_specs) >= 1, "Expected healthy-app pods"
        for spec in healthy_specs:
            assert spec["host_pid"] is False, "healthy-app should not use hostPID"
            assert spec["host_network"] is False, "healthy-app should not use hostNetwork"

    def test_get_namespace_psa_levels_returns_dict(self, k8s_cluster_ready: bool) -> None:
        levels = self._adapter.get_namespace_psa_enforce_levels()

        assert isinstance(levels, dict)
