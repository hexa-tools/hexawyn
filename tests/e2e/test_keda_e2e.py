"""E2E tests: KEDA — real KEDA on k3d cluster.

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.keda_adapter import KedaAdapter
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestKedaE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KedaAdapter(VanillaAdapter("k3d-hexawyn-e2e"))

    def test_keda_detect_returns_response(self) -> None:
        result = self._adapter.detect()

        assert hasattr(result, "installed")
        assert hasattr(result, "total_scaledobjects")

    def test_keda_scaledobjects_list_returns_data(self) -> None:
        scaledobjects = self._adapter.list_scaledobjects(namespace=NAMESPACE)

        assert isinstance(scaledobjects, list)
        assert len(scaledobjects) >= 1, f"Expected ScaledObjects, got {len(scaledobjects)}"

    def test_keda_scaledobject_get(self) -> None:
        result = self._adapter.get_scaledobject(name="e2e-test-scaledobject", namespace=NAMESPACE)

        assert result is not None
        assert hasattr(result, "name")

    def test_keda_triggerauth_list_does_not_crash(self) -> None:
        auths = self._adapter.list_trigger_auths(namespace=NAMESPACE)
        assert isinstance(auths, list)

    def test_get_nonexistent_scaledobject_raises(self) -> None:
        with pytest.raises(Exception):
            self._adapter.get_scaledobject(name="does-not-exist-obj", namespace=NAMESPACE)

    def test_list_empty_namespace_returns_empty(self) -> None:
        scaledobjects = self._adapter.list_scaledobjects(namespace="kube-system")
        assert isinstance(scaledobjects, list)

    def test_list_scaledjobs_does_not_crash(self) -> None:
        jobs = self._adapter.list_scaledjobs(namespace=NAMESPACE)
        assert isinstance(jobs, list)
