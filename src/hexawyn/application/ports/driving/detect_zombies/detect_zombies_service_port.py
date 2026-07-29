from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_zombies.command import (
    DetectZombiesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_zombies.response import (
    DetectZombiesResponse,
)


class DetectZombiesServicePort(ABC):
    @abstractmethod
    def detect_zombies(self, command: DetectZombiesCommand) -> DetectZombiesResponse: ...
