from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
    ContainerImageDriftResponse,
)


class ContainerImageDriftServicePort(ABC):
    @abstractmethod
    def detect_image_drift(
        self, command: ContainerImageDriftCommand
    ) -> ContainerImageDriftResponse: ...
