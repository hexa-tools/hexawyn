from __future__ import annotations

from hexawyn.domain.models.outdated_helm import OutdatedHelmRelease, OutdatedHelmReport


class HelmOutdatedReleaseEngine:
    def compute(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = _as_bool(rel.get("is_pinned"))

            if is_pinned:
                continue

            latest_info = latest_map.get(chart_name, {})
            latest = str(latest_info.get("latest_version", ""))
            repo_error = str(latest_info.get("repo_error", ""))

            if repo_error:
                result.error_count += 1
                result.releases.append(
                    OutdatedHelmRelease(
                        release_name=str(rel.get("release_name", "")),
                        namespace=str(rel.get("namespace", "")),
                        chart_name=chart_name,
                        current_version=current,
                        latest_version=latest or "unknown",
                        delta_type="error",
                        breaking_changes="",
                        is_pinned=False,
                        repo_error=repo_error,
                    )
                )
                continue

            if not latest_info:
                result.error_count += 1
                result.releases.append(
                    OutdatedHelmRelease(
                        release_name=str(rel.get("release_name", "")),
                        namespace=str(rel.get("namespace", "")),
                        chart_name=chart_name,
                        current_version=current,
                        latest_version="unknown",
                        delta_type="error",
                        breaking_changes="",
                        is_pinned=False,
                        repo_error="chart not found in repository",
                    )
                )
                continue

            delta = _compare_semver(current, latest)
            breaking = _get_breaking_changes(delta, latest_info)

            if delta == "up_to_date":
                result.up_to_date_count += 1
            elif delta == "error":
                result.error_count += 1
            else:
                result.outdated_count += 1

            result.releases.append(
                OutdatedHelmRelease(
                    release_name=str(rel.get("release_name", "")),
                    namespace=str(rel.get("namespace", "")),
                    chart_name=chart_name,
                    current_version=current,
                    latest_version=latest,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result


def _get_breaking_changes(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def _parse_semver(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def _compare_semver(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "error"
    if cur == lat:
        return "up_to_date"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)
