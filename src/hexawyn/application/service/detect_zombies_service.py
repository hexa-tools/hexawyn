from __future__ import annotations

from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
from hexawyn.application.use_case.detect_zombies.command import (
    DetectZombiesCommand,
)
from hexawyn.application.use_case.detect_zombies.response import (
    DetectZombiesResponse,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_service_port import (
    DetectZombiesServicePort,
)
from hexawyn.domain.services.zombie_detection.zombie_detection_engine import (
    ZombieDetectionEngine,
)


class DetectZombiesService(DetectZombiesServicePort):
    def __init__(
        self,
        zombie_detection_port: ZombieDetectionPort,
    ) -> None:
        self._port = zombie_detection_port
        self._engine = ZombieDetectionEngine()

    def detect_zombies(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)
