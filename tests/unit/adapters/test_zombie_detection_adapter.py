from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.zombie_detection_adapter import (
    VanillaZombieDetectionAdapter,
)
from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
from hexawyn.domain.errors import ClusterUnreachableError


def _fake_pod(  # noqa: PLR0913
    name: str,
    namespace: str,
    phase: str = "Running",
    kind: str | None = None,
    cpu: str = "100m",
    mem: str = "128Mi",
) -> MagicMock:
    pod = MagicMock()

    metadata = MagicMock()
    metadata.name = name
    metadata.namespace = namespace
    if kind is not None:
        ref = MagicMock()
        ref.kind = kind
        metadata.owner_references = [ref]
    else:
        metadata.owner_references = None
    pod.metadata = metadata

    spec = MagicMock()
    container = MagicMock()
    resources = MagicMock()
    resources.requests = {"cpu": cpu, "memory": mem}
    container.resources = resources
    spec.containers = [container]
    pod.spec = spec

    status = MagicMock()
    status.phase = phase
    pod.status = status

    return pod


class TestVanillaZombieDetectionAdapter:
    def test_implements_zombie_detection_port(self) -> None:
        api = MagicMock()
        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        assert isinstance(adapter, ZombieDetectionPort)

    def test_get_zombie_workloads_returns_zombie_pods(self) -> None:
        api = MagicMock()
        pod = _fake_pod(name="zombie-pod-1", namespace="default")
        response = MagicMock()
        response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        result = adapter.get_zombie_workloads(window_hours=24)

        assert len(result) == 1
        entry = result[0]
        assert entry["pod_name"] == "zombie-pod-1"
        assert entry["namespace"] == "default"
        assert entry["traffic_rps"] == 0.0
        assert entry["is_terminating"] is False
        assert entry["is_cronjob"] is False
        assert entry["has_sidecar"] is False

    def test_get_zombie_workloads_detects_cronjob(self) -> None:
        api = MagicMock()
        pod = _fake_pod(name="cron-pod-1", namespace="default", kind="CronJob")
        response = MagicMock()
        response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        result = adapter.get_zombie_workloads(window_hours=24)

        assert len(result) == 1
        assert result[0]["is_cronjob"] is True

    def test_get_zombie_workloads_detects_terminating(self) -> None:
        api = MagicMock()
        pod = _fake_pod(name="dying-pod", namespace="default", phase="Terminating")
        response = MagicMock()
        response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        result = adapter.get_zombie_workloads(window_hours=24)

        assert len(result) == 1
        assert result[0]["is_terminating"] is True

    def test_get_zombie_workloads_detects_sidecar(self) -> None:
        api = MagicMock()
        pod = _fake_pod(name="sidecar-pod", namespace="default")
        spec = pod.spec
        container2 = MagicMock()
        resources2 = MagicMock()
        resources2.requests = {"cpu": "50m", "memory": "64Mi"}
        container2.resources = resources2
        spec.containers = [spec.containers[0], container2]
        pod.spec = spec

        response = MagicMock()
        response.items = [pod]
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        result = adapter.get_zombie_workloads(window_hours=24)

        assert len(result) == 1
        assert result[0]["has_sidecar"] is True

    def test_get_zombie_workloads_empty_pods(self) -> None:
        api = MagicMock()
        response = MagicMock()
        response.items = []
        api.list_pod_for_all_namespaces.return_value = response

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        result = adapter.get_zombie_workloads(window_hours=24)

        assert result == []

    def test_get_zombie_workloads_api_error_raises_cluster_unreachable(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.side_effect = OSError("Connection refused")

        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=[])
        with pytest.raises(ClusterUnreachableError):
            adapter.get_zombie_workloads(window_hours=24)

    def test_pod_cache_stored(self) -> None:
        api = MagicMock()
        cache = [MagicMock()]
        adapter = VanillaZombieDetectionAdapter(api=api, pod_cache=cache)
        assert adapter._pod_cache is cache
