from __future__ import annotations

from hexawyn.application.ports.driven.helm_release_version_port import (
    HelmReleaseVersionPort,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.response import (
    DetectOutdatedHelmReleasesResponse,
)
from hexawyn.domain.services.outdated_helm.outdated_helm_engine import (
    HelmOutdatedReleaseEngine,
)


class DetectOutdatedHelmReleasesUseCase:
    def __init__(self, helm_port: HelmReleaseVersionPort) -> None:
        self._port = helm_port
        self._engine = HelmOutdatedReleaseEngine()

    def detect_outdated(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore
