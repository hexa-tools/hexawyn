from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_response import (
    DetectOutdatedHelmReleasesResponse,
)


class DetectOutdatedHelmReleasesServicePort(ABC):
    @abstractmethod
    def detect_outdated(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse: ...
