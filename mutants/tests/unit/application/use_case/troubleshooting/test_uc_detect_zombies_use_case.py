from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombiePodData,
)
from hexawyn.application.use_case.troubleshooting.detect_zombies.command import (
    DetectZombiesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_zombies.detect_zombies_use_case import (
    DetectZombiesUseCase,
)
from hexawyn.application.use_case.troubleshooting.detect_zombies.response import (
    DetectZombiesResponse,
)


def _make_pod(**overrides: object) -> ZombiePodData:
    base: ZombiePodData = {
        "pod_name": "idle-nginx",
        "namespace": "default",
        "traffic_rps": 0.0,
        "cpu_cores": 0.5,
        "memory_gb": 1.0,
        "age_days": 30,
        "has_service": False,
        "is_cronjob": False,
        "is_terminating": False,
        "has_sidecar": False,
        "sidecar_traffic_rps": 0.0,
        "seven_day_traffic_rps": 0.0,
    }
    base.update(overrides)  # type: ignore[typeddict-item]
    return base


class TestDetectZombiesUseCase:
    def test_execute_returns_detect_zombies_response(self) -> None:
        port = MagicMock()
        port.get_zombie_workloads.return_value = []

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert isinstance(result, DetectZombiesResponse)

    def test_execute_detects_zombie_pod_with_zero_traffic(self) -> None:
        idle_pod = _make_pod()
        port = MagicMock()
        port.get_zombie_workloads.return_value = [idle_pod]

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 1
        candidate = result.result.zombie_candidates[0]
        assert candidate.pod_name == "idle-nginx"
        assert candidate.namespace == "default"

    def test_execute_excludes_terminating_pods(self) -> None:
        terminating_pod = _make_pod(
            pod_name="terminating-pod",
            is_terminating=True,
        )
        port = MagicMock()
        port.get_zombie_workloads.return_value = [terminating_pod]

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 0

    def test_execute_excludes_pods_with_traffic(self) -> None:
        active_pod = _make_pod(
            pod_name="active-app",
            traffic_rps=100.0,
        )
        port = MagicMock()
        port.get_zombie_workloads.return_value = [active_pod]

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 0

    def test_execute_passes_analysis_window_hours_to_port(self) -> None:
        port = MagicMock()
        port.get_zombie_workloads.return_value = []

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        use_case.execute(DetectZombiesCommand(analysis_window_hours=48))

        port.get_zombie_workloads.assert_called_once_with(48)

    def test_execute_pod_with_service_flags_review_needed(self) -> None:
        service_pod = _make_pod(
            pod_name="service-pod",
            has_service=True,
        )
        port = MagicMock()
        port.get_zombie_workloads.return_value = [service_pod]

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert result.result.zombie_candidates[0].risk == "review_needed"

    def test_execute_no_zombies_returns_empty_candidates(self) -> None:
        port = MagicMock()
        port.get_zombie_workloads.return_value = []

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert result.result.zombie_candidates == []
        assert result.result.total_wasted_cores == 0.0

    def test_execute_mixed_zombie_and_active(self) -> None:
        idle = _make_pod(pod_name="idle")
        active = _make_pod(pod_name="active", traffic_rps=100.0)
        port = MagicMock()
        port.get_zombie_workloads.return_value = [idle, active]

        use_case = DetectZombiesUseCase(zombie_detection_port=port)
        result = use_case.execute(DetectZombiesCommand())

        assert len(result.result.zombie_candidates) == 1
        assert result.result.zombie_candidates[0].pod_name == "idle"
