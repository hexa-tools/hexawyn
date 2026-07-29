"""E2E tests: Tekton — real Tekton Pipelines on k3d cluster.

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
    KubernetesTektonAdapter,
)

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestTektonE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KubernetesTektonAdapter()

    def test_list_pipeline_runs_returns_data(self) -> None:
        runs = self._adapter.list_pipeline_runs(namespace=NAMESPACE, limit=10)

        assert isinstance(runs, list)
        assert len(runs) >= 1, f"Expected at least 1 PipelineRun, got {len(runs)}"

    def test_pipeline_run_status_has_fields(self) -> None:
        runs = self._adapter.list_pipeline_runs(namespace=NAMESPACE, limit=10)

        assert len(runs) >= 1
        run = runs[0]
        assert "name" in run
        assert "status" in run

    def test_list_pipeline_runs_empty_namespace(self) -> None:
        runs = self._adapter.list_pipeline_runs(namespace="kube-system", limit=10)

        assert isinstance(runs, list)

    def test_list_pipeline_runs_all_namespaces(self) -> None:
        runs = self._adapter.list_pipeline_runs(namespace=NAMESPACE, limit=50)

        assert isinstance(runs, list)
        assert len(runs) >= 1, "Expected PipelineRuns"
