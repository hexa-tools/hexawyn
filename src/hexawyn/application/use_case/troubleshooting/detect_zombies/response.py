from dataclasses import dataclass

from hexawyn.domain.models.zombie_detection import ZombieDetectionResult


@dataclass
class DetectZombiesResponse:
    result: ZombieDetectionResult
