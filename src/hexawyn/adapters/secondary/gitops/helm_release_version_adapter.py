from __future__ import annotations

from hexawyn.application.ports.driven.helm_release_version_port import (
    ChartLatestRawData,
    HelmReleaseRawData,
    HelmReleaseVersionPort,
)


class HelmReleaseVersionAdapter(HelmReleaseVersionPort):
    def list_releases(self, namespace: str | None) -> list[HelmReleaseRawData]:
        return []

    def fetch_latest_version(self, chart_name: str) -> ChartLatestRawData:
        return ChartLatestRawData(
            chart_name=chart_name,
            latest_version="",
            breaking_changes="",
            repo_error="",
        )
