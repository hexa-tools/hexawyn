from __future__ import annotations

from hexawyn.application.ports.driven.version_check_port import VersionCheckPort
from hexawyn.domain.models.version_info import VersionCheckResult

_UP_TO_DATE = "up_to_date"
_UPDATE_AVAILABLE = "update_available"
_UNKNOWN = "unknown"


def check_for_update(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def _compare_versions(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def _parse_version(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def _is_newer(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False
