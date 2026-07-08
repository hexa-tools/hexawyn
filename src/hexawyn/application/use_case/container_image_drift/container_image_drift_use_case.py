from __future__ import annotations

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
    ContainerImageDriftResponse,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
    ContainerImageDriftServicePort,
)


class ContainerImageDriftUseCase:
    def __init__(self, service: ContainerImageDriftServicePort) -> None:
        self._svc = service

    def execute(self, command: ContainerImageDriftCommand) -> ContainerImageDriftResponse:
        return self._svc.detect_image_drift(command)
