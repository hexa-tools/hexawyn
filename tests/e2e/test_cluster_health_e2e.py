"""E2E tests: cluster_health — findings and health score from real cluster.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter


@pytest.mark.e2e
class TestClusterHealthE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaAdapter("k3d-hexawyn-e2e")

    def test_get_findings_returns_list(self) -> None:
        findings = self._adapter.get_findings()

        assert isinstance(findings, list)
        for finding in findings:
            assert "severity" in finding
            assert "message" in finding
            assert "remediation" in finding

    def test_get_health_score_positive(self) -> None:
        score = self._adapter.get_health_score()

        assert isinstance(score, int)
        assert score >= 0, f"Health score should be >= 0, got {score}"

    def test_get_health_status_returns_string(self) -> None:
        status = self._adapter.get_health_status()

        assert isinstance(status, str)
        assert len(status) > 0
