from __future__ import annotations

import json
import subprocess

from hexawyn.application.ports.driven.helm_release_version_port import (
    ChartLatestRawData,
    HelmReleaseRawData,
    HelmReleaseVersionPort,
)


class HelmReleaseVersionAdapter(HelmReleaseVersionPort):
    def list_releases(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []

    def fetch_latest_version(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
