from __future__ import annotations

from hexawyn.application.ports.driven.helm_release_version_port import HelmReleaseVersionPort
from hexawyn.application.use_case.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.detect_outdated_helm_releases.response import (
    DetectOutdatedHelmReleasesResponse,
    HelmReleaseEntry,
    OutdatedHelmResult,
)


class DetectOutdatedHelmReleasesUseCase:
    def __init__(self, port: HelmReleaseVersionPort) -> None:
        self._port = port

    def execute(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases = self._port.list_releases(command.namespace)

        entries: list[HelmReleaseEntry] = []
        outdated = 0
        up_to_date = 0
        errors = 0

        for rel in releases:
            chart_name = rel["chart_name"]
            try:
                latest = self._port.fetch_latest_version(chart_name)
            except Exception:
                entries.append(
                    HelmReleaseEntry(
                        release_name=rel["release_name"],
                        namespace=rel["namespace"],
                        chart_name=chart_name,
                        current_version=rel["chart_version"],
                        latest_version="",
                        delta_type="error",
                        breaking_changes="",
                        repo_error=latest.get("repo_error", ""),
                    )
                )
                errors += 1
                continue

            current = rel["chart_version"]
            latest_ver = latest.get("latest_version", "")
            breaking = latest.get("breaking_changes", "")
            repo_error = latest.get("repo_error", "")

            if repo_error:
                delta = "error"
                errors += 1
            elif current == latest_ver:
                delta = "up_to_date"
                up_to_date += 1
            else:
                delta = "patch"
                outdated += 1

            entries.append(
                HelmReleaseEntry(
                    release_name=rel["release_name"],
                    namespace=rel["namespace"],
                    chart_name=chart_name,
                    current_version=current,
                    latest_version=latest_ver,
                    delta_type=delta,
                    breaking_changes=breaking,
                    repo_error=repo_error,
                )
            )

        result = OutdatedHelmResult(
            total_releases=len(releases),
            outdated_count=outdated,
            up_to_date_count=up_to_date,
            error_count=errors,
            releases=entries,
        )
        return DetectOutdatedHelmReleasesResponse(result=result)
