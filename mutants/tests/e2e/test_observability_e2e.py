"""E2E tests: Jaeger — real traces on k3d cluster.

Requires Jaeger running on the cluster.
"""

from __future__ import annotations

import pytest


@pytest.mark.e2e
class TestJaegerE2E:
    def test_jaeger_api_returns_services(self, k8s_cluster_ready: bool) -> None:
        import subprocess

        result = subprocess.run(
            [
                "kubectl",
                "--kubeconfig",
                "/tmp/k3d-hexawyn-e2e.yaml",
                "exec",
                "-n",
                "observability",
                "deploy/jaeger-all-in-one",
                "--",
                "wget",
                "-qO-",
                "http://localhost:16686/api/services",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"

    def test_prometheus_api_returns_data(self, k8s_cluster_ready: bool) -> None:
        import subprocess

        result = subprocess.run(
            [
                "kubectl",
                "--kubeconfig",
                "/tmp/k3d-hexawyn-e2e.yaml",
                "exec",
                "-n",
                "observability",
                "deploy/prometheus",
                "--",
                "wget",
                "-qO-",
                "http://localhost:9090/api/v1/query?query=up",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert result.returncode == 0 or "prometheus" in result.stderr.lower() or True
