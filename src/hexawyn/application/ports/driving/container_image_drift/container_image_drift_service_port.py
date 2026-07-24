from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.detect_container_image_drift.command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.use_case.detect_container_image_drift.response import (
    ContainerImageDriftResponse,
)


class ContainerImageDriftServicePort(ABC):
    @abstractmethod
    def detect_image_drift(
        self, command: ContainerImageDriftCommand
    ) -> ContainerImageDriftResponse: ...
