from __future__ import annotations

from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_response import (
    DetectOutdatedHelmReleasesResponse,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_service_port import (
    DetectOutdatedHelmReleasesServicePort,
)


class DetectOutdatedHelmReleasesUseCase:
    def __init__(self, service: DetectOutdatedHelmReleasesServicePort) -> None:
        self._service = service

    def execute(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        return self._service.detect_outdated(command)
