from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.response import (
    DetectOutdatedHelmReleasesResponse,
)


class DetectOutdatedHelmReleasesServicePort(ABC):
    @abstractmethod
    def detect_outdated(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse: ...
