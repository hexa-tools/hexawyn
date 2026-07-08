"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_command import (
    DetectZombiesCommand,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_response import (
    DetectZombiesResponse,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_service_port import (
    DetectZombiesServicePort,
)
from hexawyn.application.service.detect_zombies_service import DetectZombiesService
from hexawyn.application.use_case.detect_zombies.detect_zombies_use_case import (
    DetectZombiesUseCase,
)
from hexawyn.domain.models.zombie_detection import ZombieDetectionResult


class TestZombieDetectionPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(ZombieDetectionPort)

    def test_concrete_impl_must_implement_get_zombie_workloads(self) -> None:
        class BadAdapter(ZombieDetectionPort):
            pass

        with pytest.raises(TypeError):
            BadAdapter()  # type: ignore[abstract]

    def test_concrete_impl_accepted(self) -> None:
        class GoodAdapter(ZombieDetectionPort):
            def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]:
                return []

        adapter = GoodAdapter()
        assert adapter.get_zombie_workloads(24) == []


class TestDetectZombiesCommand:
    def test_default_window_is_24(self) -> None:
        cmd = DetectZombiesCommand()
        assert cmd.analysis_window_hours == 24

    def test_custom_window(self) -> None:
        cmd = DetectZombiesCommand(analysis_window_hours=72)
        assert cmd.analysis_window_hours == 72

    def test_is_frozen(self) -> None:
        cmd = DetectZombiesCommand()
        with pytest.raises(Exception):
            cmd.analysis_window_hours = 48  # type: ignore[misc]


class TestDetectZombiesResponse:
    def test_holds_result(self) -> None:
        result = ZombieDetectionResult(
            analysis_window_hours=24,
            zombie_candidates=[],
            total_wasted_cores=0.0,
            total_wasted_gb=0.0,
        )
        response = DetectZombiesResponse(result=result)
        assert response.result is result


class TestDetectZombiesService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = []
        return port

    def test_calls_port_with_window_hours(self) -> None:
        port = self._mock_port()
        service = DetectZombiesService(zombie_detection_port=port)

        service.detect_zombies(DetectZombiesCommand(analysis_window_hours=48))

        port.get_zombie_workloads.assert_called_once_with(48)

    def test_returns_detect_zombies_response(self) -> None:
        port = self._mock_port()
        service = DetectZombiesService(zombie_detection_port=port)

        result = service.detect_zombies(DetectZombiesCommand())

        assert isinstance(result, DetectZombiesResponse)
        assert isinstance(result.result, ZombieDetectionResult)

    def test_engine_detects_zero_traffic_pod(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = [
            ZombiePodData(
                pod_name="idle-pod",
                namespace="production",
                traffic_rps=0.0,
                cpu_cores=0.5,
                memory_gb=1.0,
                age_days=30,
                has_service=False,
                is_cronjob=False,
                is_terminating=False,
                has_sidecar=False,
                sidecar_traffic_rps=0.0,
                seven_day_traffic_rps=0.0,
            ),
        ]
        service = DetectZombiesService(zombie_detection_port=port)

        result = service.detect_zombies(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 1
        assert result.result.zombie_candidates[0].pod_name == "idle-pod"
        assert result.result.total_wasted_cores == 0.5
        assert result.result.total_wasted_gb == 1.0

    def test_service_passes_data_source_from_port(self) -> None:
        port = MagicMock(spec=ZombieDetectionPort)
        port.get_zombie_workloads.return_value = []
        service = DetectZombiesService(zombie_detection_port=port)

        result = service.detect_zombies(DetectZombiesCommand())

        assert result.result.analysis_window_hours == 24


class TestDetectZombiesUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectZombiesServicePort)
        inner = ZombieDetectionResult(
            zombie_candidates=[],
        )
        service.detect_zombies.return_value = DetectZombiesResponse(result=inner)
        use_case = DetectZombiesUseCase(service=service)

        result = use_case.execute(DetectZombiesCommand())

        service.detect_zombies.assert_called_once()
        assert result.result is inner

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=DetectZombiesServicePort)
        service.detect_zombies.return_value = DetectZombiesResponse(
            result=ZombieDetectionResult(),
        )
        use_case = DetectZombiesUseCase(service=service)
        cmd = DetectZombiesCommand(analysis_window_hours=72)

        use_case.execute(cmd)

        service.detect_zombies.assert_called_once_with(cmd)
