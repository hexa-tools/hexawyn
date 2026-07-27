from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_container_image_drift.command import (  # type: ignore
    ContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (  # type: ignore
    ContainerImageDriftResponse,
)


class ContainerImageDriftServicePort(ABC):
    @abstractmethod
    def detect_image_drift(
        self, command: ContainerImageDriftCommand
    ) -> ContainerImageDriftResponse: ...
