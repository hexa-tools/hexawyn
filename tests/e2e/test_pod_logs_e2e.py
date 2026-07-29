"""E2E tests: pod_logs — fetch real logs from cluster pods.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
    KubernetesPodLogsAdapter,
)
from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestPodLogsE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = KubernetesPodLogsAdapter()

    def test_fetch_logs_from_healthy_pod(self, healthy_deployment: str) -> None:
        pods = self._get_pods_by_label("app=healthy-app", NAMESPACE)
        assert pods, "No healthy-app pods found"

        pod_name = pods[0]
        request = AnalyzePodLogsRequest(
            pod_name=pod_name, namespace=NAMESPACE, time_window_minutes=5
        )

        logs = self._adapter.fetch_logs(request)

        assert isinstance(logs, list)
        assert len(logs) > 0, f"Expected logs from {pod_name}"

    def test_fetch_logs_from_crashloop_pod(self, crashloop_pod: str) -> None:
        request = AnalyzePodLogsRequest(
            pod_name="crashloop-test", namespace=NAMESPACE, time_window_minutes=5
        )

        logs = self._adapter.fetch_logs(request)

        assert isinstance(logs, list)
        assert len(logs) > 0, "Expected logs from crashloop-test"
        assert any(
            "Starting" in line.message for line in logs
        ), "Expected 'Starting' message in crashloop logs"

    def test_fetch_logs_resource_not_found(self, k8s_cluster_ready: bool) -> None:
        from hexawyn.domain.errors import ResourceNotFoundError

        request = AnalyzePodLogsRequest(
            pod_name="does-not-exist-e2e-log", namespace=NAMESPACE, time_window_minutes=5
        )

        with pytest.raises(ResourceNotFoundError):
            self._adapter.fetch_logs(request)

    def _get_pods_by_label(self, label: str, namespace: str) -> list[str]:
        from kubernetes import client, config

        config.load_kube_config()
        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(namespace=namespace, label_selector=label)
        return [p.metadata.name for p in pods.items]
