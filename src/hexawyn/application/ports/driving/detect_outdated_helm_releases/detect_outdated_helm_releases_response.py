from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.outdated_helm import OutdatedHelmReport


@dataclass
class DetectOutdatedHelmReleasesResponse:
    result: OutdatedHelmReport
