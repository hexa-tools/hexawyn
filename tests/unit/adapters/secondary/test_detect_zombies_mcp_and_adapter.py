"""RED → GREEN — Layer 7: MCP tool + VanillaAdapter ZombieDetectionPort."""

import asyncio
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _fake_core_api(pods: list) -> MagicMock:
    api = MagicMock()
    pod_list = MagicMock()
    pod_list.items = pods
    api.list_pod_for_all_namespaces.return_value = pod_list
    return api


def _fake_pod(
    name: str,
    namespace: str = "production",
    phase: str = "Running",
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.status.phase = phase
    pod.metadata.owner_references = None
    container = MagicMock()
    container.resources.requests = {}
    pod.spec.containers = [container]
    return pod


class TestVanillaAdapterZombieDetectionPort:
    def test_implements_zombie_detection_port(self) -> None:
        assert isinstance(VanillaAdapter("test", api=MagicMock()), ZombieDetectionPort)

    def test_get_zombie_workloads_returns_list(self) -> None:
        pod = _fake_pod("test-pod")
        adapter = VanillaAdapter("test", api=_fake_core_api([pod]))

        result = adapter.get_zombie_workloads(window_hours=24)

        assert isinstance(result, list)

    def test_returns_pods_with_expected_keys(self) -> None:
        pod = _fake_pod("svc", "prod")
        adapter = VanillaAdapter("test", api=_fake_core_api([pod]))

        result = adapter.get_zombie_workloads(window_hours=24)

        assert len(result) > 0
        pod_result = result[0]
        assert "pod_name" in pod_result
        assert "namespace" in pod_result
        assert "traffic_rps" in pod_result
        assert "cpu_cores" in pod_result
        assert "memory_gb" in pod_result
        assert "age_days" in pod_result
        assert "has_service" in pod_result
        assert "is_cronjob" in pod_result
        assert "is_terminating" in pod_result
        assert "has_sidecar" in pod_result
        assert "sidecar_traffic_rps" in pod_result
        assert "seven_day_traffic_rps" in pod_result

    def test_includes_zero_traffic_pod(self) -> None:
        pod = _fake_pod("idle-pod", "staging")
        adapter = VanillaAdapter("test", api=_fake_core_api([pod]))

        result = adapter.get_zombie_workloads(window_hours=24)

        zero_traffic = [p for p in result if p["traffic_rps"] == 0.0]
        assert len(zero_traffic) > 0

    def test_cluster_unreachable_raises(self) -> None:
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.side_effect = Exception("forbidden")
        adapter = VanillaAdapter("test", api=core_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.get_zombie_workloads(window_hours=24)


class TestMCPDetectZombiesTool:
    def test_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        assert "detect_zombies" in {t.name for t in tools}

    def test_returns_zombie_candidates_and_waste(self) -> None:
        mock_port = MagicMock(spec=ZombieDetectionPort)
        mock_port.get_zombie_workloads.return_value = [
            ZombiePodData(
                pod_name="legacy-api",
                namespace="production",
                traffic_rps=0.0,
                cpu_cores=0.5,
                memory_gb=1.0,
                age_days=180,
                has_service=False,
                is_cronjob=False,
                is_terminating=False,
                has_sidecar=False,
                sidecar_traffic_rps=0.0,
                seven_day_traffic_rps=0.0,
            ),
        ]

        with patch("hexawyn.mcp.server.build_zombie_detection_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.detect_zombies import detect_zombies

            result = detect_zombies()

        assert result["error"] is None
        assert result["zombie_count"] == 1
        assert result["total_wasted_cores"] > 0
        assert result["total_wasted_gb"] > 0
        assert len(result["zombie_candidates"]) == 1

    def test_cluster_error_captured_in_error_field(self) -> None:
        mock_port = MagicMock(spec=ZombieDetectionPort)
        mock_port.get_zombie_workloads.side_effect = ClusterUnreachableError("down")

        with patch("hexawyn.mcp.server.build_zombie_detection_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.detect_zombies import detect_zombies

            result = detect_zombies()

        assert result["error"] is not None
        assert result["zombie_count"] == 0


class TestMCPServerZombieBuilder:
    def test_build_zombie_detection_adapter_returns_zombie_detection_port(self) -> None:
        from hexawyn.application.ports.driven.zombie_detection_port import (
            ZombieDetectionPort,
        )
        from hexawyn.mcp.server import build_zombie_detection_adapter

        result = build_zombie_detection_adapter()

        assert isinstance(result, ZombieDetectionPort)
