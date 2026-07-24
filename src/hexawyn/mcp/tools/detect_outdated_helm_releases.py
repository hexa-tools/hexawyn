"""MCP tool: detect_outdated_helm_releases — find outdated Helm releases."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.detect_outdated_helm_releases.detect_outdated_helm_releases_use_case import (
    DetectOutdatedHelmReleasesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_outdated_helm_releases(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "releases": [
                {
                    "release_name": rel.release_name,
                    "namespace": rel.namespace,
                    "chart_name": rel.chart_name,
                    "current_version": rel.current_version,
                    "latest_version": rel.latest_version,
                    "delta_type": rel.delta_type,
                    "breaking_changes": rel.breaking_changes,
                    "repo_error": rel.repo_error,
                }
                for rel in r.releases
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "total_releases": 0,
            "outdated_count": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_outdated_helm_releases)
