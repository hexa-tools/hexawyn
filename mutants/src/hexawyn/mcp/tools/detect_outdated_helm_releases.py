"""MCP tool: detect_outdated_helm_releases — find outdated Helm releases."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.detect_outdated_helm_releases_use_case import (  # noqa: E501
    DetectOutdatedHelmReleasesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_outdated_helm_releases__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_outdated_helm_releases__mutmut)
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
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = None
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=None)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = None  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(None)  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=None))  # type: ignore
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


def x_detect_outdated_helm_releases__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = None
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


def x_detect_outdated_helm_releases__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "XXtotal_releasesXX": r.total_releases,
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


def x_detect_outdated_helm_releases__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "TOTAL_RELEASES": r.total_releases,
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


def x_detect_outdated_helm_releases__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "XXoutdated_countXX": r.outdated_count,
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


def x_detect_outdated_helm_releases__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "OUTDATED_COUNT": r.outdated_count,
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


def x_detect_outdated_helm_releases__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "XXup_to_date_countXX": r.up_to_date_count,
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


def x_detect_outdated_helm_releases__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "UP_TO_DATE_COUNT": r.up_to_date_count,
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


def x_detect_outdated_helm_releases__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "XXerror_countXX": r.error_count,
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


def x_detect_outdated_helm_releases__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "ERROR_COUNT": r.error_count,
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


def x_detect_outdated_helm_releases__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "XXreleasesXX": [
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


def x_detect_outdated_helm_releases__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "RELEASES": [
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


def x_detect_outdated_helm_releases__mutmut_18(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "releases": [
                {
                    "XXrelease_nameXX": rel.release_name,
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


def x_detect_outdated_helm_releases__mutmut_19(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "releases": [
                {
                    "RELEASE_NAME": rel.release_name,
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


def x_detect_outdated_helm_releases__mutmut_20(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "releases": [
                {
                    "release_name": rel.release_name,
                    "XXnamespaceXX": rel.namespace,
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


def x_detect_outdated_helm_releases__mutmut_21(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
        r = response.result
        return {
            "total_releases": r.total_releases,
            "outdated_count": r.outdated_count,
            "up_to_date_count": r.up_to_date_count,
            "error_count": r.error_count,
            "releases": [
                {
                    "release_name": rel.release_name,
                    "NAMESPACE": rel.namespace,
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


def x_detect_outdated_helm_releases__mutmut_22(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXchart_nameXX": rel.chart_name,
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


def x_detect_outdated_helm_releases__mutmut_23(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "CHART_NAME": rel.chart_name,
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


def x_detect_outdated_helm_releases__mutmut_24(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXcurrent_versionXX": rel.current_version,
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


def x_detect_outdated_helm_releases__mutmut_25(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "CURRENT_VERSION": rel.current_version,
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


def x_detect_outdated_helm_releases__mutmut_26(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXlatest_versionXX": rel.latest_version,
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


def x_detect_outdated_helm_releases__mutmut_27(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "LATEST_VERSION": rel.latest_version,
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


def x_detect_outdated_helm_releases__mutmut_28(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXdelta_typeXX": rel.delta_type,
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


def x_detect_outdated_helm_releases__mutmut_29(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "DELTA_TYPE": rel.delta_type,
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


def x_detect_outdated_helm_releases__mutmut_30(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXbreaking_changesXX": rel.breaking_changes,
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


def x_detect_outdated_helm_releases__mutmut_31(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "BREAKING_CHANGES": rel.breaking_changes,
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


def x_detect_outdated_helm_releases__mutmut_32(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "XXrepo_errorXX": rel.repo_error,
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


def x_detect_outdated_helm_releases__mutmut_33(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
                    "REPO_ERROR": rel.repo_error,
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


def x_detect_outdated_helm_releases__mutmut_34(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXerrorXX": None,
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


def x_detect_outdated_helm_releases__mutmut_35(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "ERROR": None,
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


def x_detect_outdated_helm_releases__mutmut_36(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXtotal_releasesXX": 0,
            "outdated_count": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_37(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "TOTAL_RELEASES": 0,
            "outdated_count": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_38(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "total_releases": 1,
            "outdated_count": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_39(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXoutdated_countXX": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_40(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "OUTDATED_COUNT": 0,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_41(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "outdated_count": 1,
            "up_to_date_count": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_42(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXup_to_date_countXX": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_43(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "UP_TO_DATE_COUNT": 0,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_44(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "up_to_date_count": 1,
            "error_count": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_45(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXerror_countXX": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_46(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "ERROR_COUNT": 0,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_47(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "error_count": 1,
            "releases": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_48(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXreleasesXX": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_49(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "RELEASES": [],
            "error": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_50(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "XXerrorXX": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_51(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "ERROR": str(exc),
        }


def x_detect_outdated_helm_releases__mutmut_52(namespace: str | None = None) -> dict[str, object]:
    """Detect Helm releases that are outdated compared to the latest chart version.

    Lists all Helm releases with their current version, queries repositories
    for the latest version, and computes the version delta (major/minor/patch).

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.mcp.server import build_helm_release_version_adapter

    try:
        adapter = build_helm_release_version_adapter()
        use_case = DetectOutdatedHelmReleasesUseCase(port=adapter)  # type: ignore
        response = use_case.execute(DetectOutdatedHelmReleasesCommand(namespace=namespace))  # type: ignore
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
            "error": str(None),
        }

mutants_x_detect_outdated_helm_releases__mutmut['_mutmut_orig'] = x_detect_outdated_helm_releases__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_1'] = x_detect_outdated_helm_releases__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_2'] = x_detect_outdated_helm_releases__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_3'] = x_detect_outdated_helm_releases__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_4'] = x_detect_outdated_helm_releases__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_5'] = x_detect_outdated_helm_releases__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_6'] = x_detect_outdated_helm_releases__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_7'] = x_detect_outdated_helm_releases__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_8'] = x_detect_outdated_helm_releases__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_9'] = x_detect_outdated_helm_releases__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_10'] = x_detect_outdated_helm_releases__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_11'] = x_detect_outdated_helm_releases__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_12'] = x_detect_outdated_helm_releases__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_13'] = x_detect_outdated_helm_releases__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_14'] = x_detect_outdated_helm_releases__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_15'] = x_detect_outdated_helm_releases__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_16'] = x_detect_outdated_helm_releases__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_17'] = x_detect_outdated_helm_releases__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_18'] = x_detect_outdated_helm_releases__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_19'] = x_detect_outdated_helm_releases__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_20'] = x_detect_outdated_helm_releases__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_21'] = x_detect_outdated_helm_releases__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_22'] = x_detect_outdated_helm_releases__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_23'] = x_detect_outdated_helm_releases__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_24'] = x_detect_outdated_helm_releases__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_25'] = x_detect_outdated_helm_releases__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_26'] = x_detect_outdated_helm_releases__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_27'] = x_detect_outdated_helm_releases__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_28'] = x_detect_outdated_helm_releases__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_29'] = x_detect_outdated_helm_releases__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_30'] = x_detect_outdated_helm_releases__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_31'] = x_detect_outdated_helm_releases__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_32'] = x_detect_outdated_helm_releases__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_33'] = x_detect_outdated_helm_releases__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_34'] = x_detect_outdated_helm_releases__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_35'] = x_detect_outdated_helm_releases__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_36'] = x_detect_outdated_helm_releases__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_37'] = x_detect_outdated_helm_releases__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_38'] = x_detect_outdated_helm_releases__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_39'] = x_detect_outdated_helm_releases__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_40'] = x_detect_outdated_helm_releases__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_41'] = x_detect_outdated_helm_releases__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_42'] = x_detect_outdated_helm_releases__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_43'] = x_detect_outdated_helm_releases__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_44'] = x_detect_outdated_helm_releases__mutmut_44 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_45'] = x_detect_outdated_helm_releases__mutmut_45 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_46'] = x_detect_outdated_helm_releases__mutmut_46 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_47'] = x_detect_outdated_helm_releases__mutmut_47 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_48'] = x_detect_outdated_helm_releases__mutmut_48 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_49'] = x_detect_outdated_helm_releases__mutmut_49 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_50'] = x_detect_outdated_helm_releases__mutmut_50 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_51'] = x_detect_outdated_helm_releases__mutmut_51 # type: ignore # mutmut generated
mutants_x_detect_outdated_helm_releases__mutmut['x_detect_outdated_helm_releases__mutmut_52'] = x_detect_outdated_helm_releases__mutmut_52 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_outdated_helm_releases)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_outdated_helm_releases)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
