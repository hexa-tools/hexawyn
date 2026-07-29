from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    DetectContainerImageDriftResponse,
)


class ContainerImageDriftServicePort(ABC):
    @abstractmethod
    def detect_image_drift(
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse: ...
