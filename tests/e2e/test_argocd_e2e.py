"""E2E tests: ArgoCD — real ArgoCD on k3d cluster."""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.gitops_adapter import GitOpsAdapter
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter


@pytest.mark.e2e
class TestArgoCDE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = GitOpsAdapter(VanillaAdapter("k3d-hexawyn-e2e"))

    def test_gitops_list_apps_does_not_crash(self) -> None:
        apps = self._adapter.list_apps()
        assert isinstance(apps, list)

    def test_gitops_list_sources_does_not_crash(self) -> None:
        sources = self._adapter.list_sources()
        assert isinstance(sources, list)

    def test_gitops_get_nonexistent_app_raises(self) -> None:
        with pytest.raises(Exception):
            self._adapter.get_app(name="does-not-exist")
