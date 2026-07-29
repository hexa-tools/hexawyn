"""E2E tests: list_namespaces — real cluster namespace listing.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

_MIN_BASE_NAMESPACES = 3
_MIN_ACTIVE_NAMESPACES = 2


@pytest.mark.e2e
class TestListNamespacesE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaAdapter("k3d-hexawyn-e2e")

    def test_lists_default_namespaces(self) -> None:
        namespaces = self._adapter.list_namespaces()

        assert isinstance(namespaces, list)
        assert (
            len(namespaces) >= _MIN_BASE_NAMESPACES
        ), "Expected at least kube-system, default, kube-public"

        ns_names = {ns["name"] for ns in namespaces}
        assert "kube-system" in ns_names, "kube-system namespace should always exist"
        assert "default" in ns_names, "default namespace should always exist"

    def test_each_namespace_has_required_fields(self) -> None:
        namespaces = self._adapter.list_namespaces()

        for ns in namespaces:
            assert "name" in ns, f"Namespace missing 'name' field: {ns}"
            assert "status" in ns, f"Namespace missing 'status' field: {ns}"
            assert "age" in ns, f"Namespace missing 'age' field: {ns}"

    def test_active_namespaces_have_active_status(self) -> None:
        namespaces = self._adapter.list_namespaces()

        active = [ns for ns in namespaces if ns["status"] == "Active"]
        assert len(active) >= _MIN_ACTIVE_NAMESPACES, "Expected at least 2 Active namespaces"
