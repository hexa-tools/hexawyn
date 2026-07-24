"""Unit tests for DetectZombiesUseCase (post-refacto — driven port injected directly)."""

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.application.use_case.detect_zombies.command import DetectZombiesCommand
from hexawyn.application.use_case.detect_zombies.detect_zombies_use_case import (
    DetectZombiesUseCase,
)
from hexawyn.application.use_case.detect_zombies.response import DetectZombiesResponse
from hexawyn.domain.models.zombie_detection import ZombieDetectionResult


class TestDetectZombiesUseCase:
    def test_calls_port_with_window_hours(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = []
        use_case = DetectZombiesUseCase(zombie_detection_port=port)

        use_case.execute(DetectZombiesCommand(analysis_window_hours=48))

        port.get_zombie_workloads.assert_called_once_with(48)

    def test_returns_detect_zombies_response(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = []
        use_case = DetectZombiesUseCase(zombie_detection_port=port)

        result = use_case.execute(DetectZombiesCommand())

        assert isinstance(result, DetectZombiesResponse)
        assert isinstance(result.result, ZombieDetectionResult)

    def test_engine_detects_zero_traffic_pod(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = [
            ZombiePodData(
                pod_name="idle-pod", namespace="production", traffic_rps=0.0,
                cpu_cores=0.5, memory_gb=1.0, age_days=30, has_service=False,
                is_cronjob=False, is_terminating=False, has_sidecar=False,
                sidecar_traffic_rps=0.0, seven_day_traffic_rps=0.0,
            ),
        ]
        use_case = DetectZombiesUseCase(zombie_detection_port=port)

        result = use_case.execute(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 1
        assert result.result.zombie_candidates[0].pod_name == "idle-pod"
        assert result.result.total_wasted_cores == 0.5
        assert result.result.total_wasted_gb == 1.0

    def test_port_error_propagates(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.side_effect = RuntimeError("cluster unreachable")
        use_case = DetectZombiesUseCase(zombie_detection_port=port)

        with pytest.raises(RuntimeError, match="cluster unreachable"):
            use_case.execute(DetectZombiesCommand())
