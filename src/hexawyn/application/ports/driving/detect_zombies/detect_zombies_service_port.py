from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_zombies.detect_zombies_command import (
    DetectZombiesCommand,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_response import (
    DetectZombiesResponse,
)


class DetectZombiesServicePort(ABC):
    @abstractmethod
    def detect_zombies(self, command: DetectZombiesCommand) -> DetectZombiesResponse: ...
