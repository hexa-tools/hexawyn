from __future__ import annotations

from hexawyn.domain.models.outdated_helm import OutdatedHelmRelease, OutdatedHelmReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class HelmOutdatedReleaseEngine:
    @_mutmut_mutated(mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_orig(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_1(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_2(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = None

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_3(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_4(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(None)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_5(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get(None, ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_6(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", None))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_7(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get(""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_8(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_9(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("XXchart_nameXX", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_10(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("CHART_NAME", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_11(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", "XXXX"))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_12(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_13(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(None)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_14(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get(None, ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_15(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", None))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_16(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get(""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_17(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_18(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("XXchart_versionXX", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_19(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("CHART_VERSION", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_20(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", "XXXX"))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_21(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = None

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_22(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = _as_bool(None)

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_23(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = _as_bool(rel.get(None))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_24(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = _as_bool(rel.get("XXis_pinnedXX"))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_25(
        self,
        releases: list[dict[str, object]],
        latest_map: dict[str, dict[str, object]],
    ) -> OutdatedHelmReport:
        result = OutdatedHelmReport()
        result.total_releases = len(releases)

        for rel in releases:
            chart_name = str(rel.get("chart_name", ""))
            current = str(rel.get("chart_version", ""))
            is_pinned = _as_bool(rel.get("IS_PINNED"))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_26(
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
                break

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_27(
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

            latest_info = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_28(
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

            latest_info = latest_map.get(None, {})
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_29(
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

            latest_info = latest_map.get(chart_name, None)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_30(
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

            latest_info = latest_map.get({})
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_31(
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

            latest_info = latest_map.get(chart_name, )
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_32(
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
            latest = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_33(
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
            latest = str(None)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_34(
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
            latest = str(latest_info.get(None, ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_35(
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
            latest = str(latest_info.get("latest_version", None))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_36(
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
            latest = str(latest_info.get(""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_37(
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
            latest = str(latest_info.get("latest_version", ))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_38(
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
            latest = str(latest_info.get("XXlatest_versionXX", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_39(
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
            latest = str(latest_info.get("LATEST_VERSION", ""))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_40(
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
            latest = str(latest_info.get("latest_version", "XXXX"))
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_41(
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
            repo_error = None

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_42(
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
            repo_error = str(None)

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_43(
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
            repo_error = str(latest_info.get(None, ""))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_44(
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
            repo_error = str(latest_info.get("repo_error", None))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_45(
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
            repo_error = str(latest_info.get(""))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_46(
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
            repo_error = str(latest_info.get("repo_error", ))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_47(
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
            repo_error = str(latest_info.get("XXrepo_errorXX", ""))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_48(
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
            repo_error = str(latest_info.get("REPO_ERROR", ""))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_49(
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
            repo_error = str(latest_info.get("repo_error", "XXXX"))

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_50(
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
                result.error_count = 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_51(
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
                result.error_count -= 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_52(
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
                result.error_count += 2
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_53(
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
                    None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_54(
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
                        release_name=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_55(
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
                        namespace=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_56(
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
                        chart_name=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_57(
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
                        current_version=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_58(
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
                        latest_version=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_59(
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
                        delta_type=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_60(
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
                        breaking_changes=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_61(
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
                        is_pinned=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_62(
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
                        repo_error=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_63(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_64(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_65(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_66(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_67(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_68(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_69(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_70(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_71(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_72(
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
                        release_name=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_73(
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
                        release_name=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_74(
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
                        release_name=str(rel.get("release_name", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_75(
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
                        release_name=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_76(
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
                        release_name=str(rel.get("release_name", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_77(
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
                        release_name=str(rel.get("XXrelease_nameXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_78(
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
                        release_name=str(rel.get("RELEASE_NAME", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_79(
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
                        release_name=str(rel.get("release_name", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_80(
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
                        namespace=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_81(
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
                        namespace=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_82(
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
                        namespace=str(rel.get("namespace", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_83(
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
                        namespace=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_84(
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
                        namespace=str(rel.get("namespace", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_85(
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
                        namespace=str(rel.get("XXnamespaceXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_86(
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
                        namespace=str(rel.get("NAMESPACE", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_87(
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
                        namespace=str(rel.get("namespace", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_88(
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
                        latest_version=latest and "unknown",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_89(
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
                        latest_version=latest or "XXunknownXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_90(
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
                        latest_version=latest or "UNKNOWN",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_91(
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
                        delta_type="XXerrorXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_92(
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
                        delta_type="ERROR",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_93(
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
                        breaking_changes="XXXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_94(
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
                        is_pinned=True,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_95(
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
                break

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_96(
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

            if latest_info:
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_97(
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
                result.error_count = 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_98(
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
                result.error_count -= 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_99(
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
                result.error_count += 2
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_100(
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
                    None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_101(
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
                        release_name=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_102(
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
                        namespace=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_103(
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
                        chart_name=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_104(
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
                        current_version=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_105(
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
                        latest_version=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_106(
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
                        delta_type=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_107(
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
                        breaking_changes=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_108(
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
                        is_pinned=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_109(
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
                        repo_error=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_110(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_111(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_112(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_113(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_114(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_115(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_116(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_117(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_118(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_119(
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
                        release_name=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_120(
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
                        release_name=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_121(
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
                        release_name=str(rel.get("release_name", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_122(
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
                        release_name=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_123(
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
                        release_name=str(rel.get("release_name", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_124(
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
                        release_name=str(rel.get("XXrelease_nameXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_125(
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
                        release_name=str(rel.get("RELEASE_NAME", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_126(
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
                        release_name=str(rel.get("release_name", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_127(
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
                        namespace=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_128(
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
                        namespace=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_129(
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
                        namespace=str(rel.get("namespace", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_130(
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
                        namespace=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_131(
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
                        namespace=str(rel.get("namespace", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_132(
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
                        namespace=str(rel.get("XXnamespaceXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_133(
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
                        namespace=str(rel.get("NAMESPACE", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_134(
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
                        namespace=str(rel.get("namespace", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_135(
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
                        latest_version="XXunknownXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_136(
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
                        latest_version="UNKNOWN",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_137(
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
                        delta_type="XXerrorXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_138(
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
                        delta_type="ERROR",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_139(
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
                        breaking_changes="XXXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_140(
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
                        is_pinned=True,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_141(
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
                        repo_error="XXchart not found in repositoryXX",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_142(
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
                        repo_error="CHART NOT FOUND IN REPOSITORY",
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_143(
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
                break

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_144(
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

            delta = None
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_145(
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

            delta = _compare_semver(None, latest)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_146(
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

            delta = _compare_semver(current, None)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_147(
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

            delta = _compare_semver(latest)
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_148(
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

            delta = _compare_semver(current, )
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_149(
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
            breaking = None

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_150(
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
            breaking = _get_breaking_changes(None, latest_info)

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_151(
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
            breaking = _get_breaking_changes(delta, None)

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_152(
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
            breaking = _get_breaking_changes(latest_info)

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_153(
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
            breaking = _get_breaking_changes(delta, )

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_154(
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

            if delta != "up_to_date":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_155(
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

            if delta == "XXup_to_dateXX":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_156(
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

            if delta == "UP_TO_DATE":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_157(
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
                result.up_to_date_count = 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_158(
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
                result.up_to_date_count -= 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_159(
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
                result.up_to_date_count += 2
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_160(
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
            elif delta != "error":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_161(
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
            elif delta == "XXerrorXX":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_162(
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
            elif delta == "ERROR":
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_163(
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
                result.error_count = 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_164(
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
                result.error_count -= 1
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_165(
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
                result.error_count += 2
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_166(
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
                result.outdated_count = 1

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_167(
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
                result.outdated_count -= 1

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_168(
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
                result.outdated_count += 2

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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_169(
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
                None
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_170(
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
                    release_name=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_171(
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
                    namespace=None,
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_172(
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
                    chart_name=None,
                    current_version=current,
                    latest_version=latest,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_173(
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
                    current_version=None,
                    latest_version=latest,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_174(
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
                    latest_version=None,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_175(
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
                    delta_type=None,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_176(
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
                    breaking_changes=None,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_177(
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
                    is_pinned=None,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_178(
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
                    repo_error=None,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_179(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_180(
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_181(
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
                    current_version=current,
                    latest_version=latest,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_182(
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
                    latest_version=latest,
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_183(
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
                    delta_type=delta,
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_184(
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
                    breaking_changes=breaking,
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_185(
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
                    is_pinned=False,
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_186(
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
                    repo_error=repo_error,
                )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_187(
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
                    )
            )

        return result
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_188(
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
                    release_name=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_189(
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
                    release_name=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_190(
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
                    release_name=str(rel.get("release_name", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_191(
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
                    release_name=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_192(
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
                    release_name=str(rel.get("release_name", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_193(
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
                    release_name=str(rel.get("XXrelease_nameXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_194(
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
                    release_name=str(rel.get("RELEASE_NAME", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_195(
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
                    release_name=str(rel.get("release_name", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_196(
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
                    namespace=str(None),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_197(
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
                    namespace=str(rel.get(None, "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_198(
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
                    namespace=str(rel.get("namespace", None)),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_199(
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
                    namespace=str(rel.get("")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_200(
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
                    namespace=str(rel.get("namespace", )),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_201(
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
                    namespace=str(rel.get("XXnamespaceXX", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_202(
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
                    namespace=str(rel.get("NAMESPACE", "")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_203(
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
                    namespace=str(rel.get("namespace", "XXXX")),
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
    def xǁHelmOutdatedReleaseEngineǁcompute__mutmut_204(
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
                    is_pinned=True,
                    repo_error=repo_error,
                )
            )

        return result

mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['_mutmut_orig'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_1'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_2'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_3'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_4'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_5'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_6'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_7'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_8'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_9'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_10'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_11'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_12'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_13'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_14'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_15'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_16'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_17'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_18'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_19'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_20'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_21'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_22'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_23'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_24'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_25'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_26'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_27'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_28'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_29'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_30'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_31'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_32'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_33'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_34'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_35'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_36'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_37'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_38'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_39'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_40'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_41'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_42'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_43'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_44'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_45'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_46'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_47'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_48'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_49'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_50'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_51'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_52'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_53'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_54'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_55'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_56'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_57'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_58'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_59'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_60'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_61'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_62'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_63'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_64'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_65'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_66'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_67'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_68'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_69'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_70'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_71'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_72'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_73'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_74'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_75'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_76'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_77'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_78'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_79'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_80'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_81'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_82'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_83'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_84'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_85'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_86'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_87'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_88'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_89'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_90'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_91'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_92'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_93'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_94'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_95'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_96'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_97'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_98'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_99'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_100'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_101'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_102'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_102 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_103'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_103 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_104'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_104 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_105'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_105 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_106'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_106 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_107'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_107 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_108'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_108 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_109'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_109 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_110'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_110 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_111'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_111 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_112'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_112 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_113'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_113 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_114'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_114 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_115'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_115 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_116'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_116 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_117'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_117 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_118'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_118 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_119'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_119 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_120'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_120 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_121'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_121 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_122'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_122 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_123'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_123 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_124'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_124 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_125'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_125 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_126'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_126 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_127'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_127 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_128'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_128 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_129'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_129 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_130'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_130 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_131'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_131 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_132'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_132 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_133'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_133 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_134'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_134 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_135'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_135 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_136'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_136 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_137'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_137 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_138'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_138 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_139'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_139 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_140'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_140 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_141'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_141 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_142'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_142 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_143'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_143 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_144'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_144 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_145'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_145 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_146'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_146 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_147'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_147 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_148'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_148 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_149'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_149 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_150'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_150 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_151'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_151 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_152'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_152 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_153'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_153 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_154'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_154 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_155'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_155 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_156'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_156 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_157'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_157 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_158'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_158 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_159'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_159 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_160'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_160 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_161'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_161 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_162'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_162 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_163'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_163 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_164'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_164 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_165'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_165 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_166'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_166 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_167'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_167 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_168'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_168 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_169'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_169 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_170'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_170 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_171'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_171 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_172'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_172 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_173'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_173 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_174'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_174 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_175'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_175 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_176'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_176 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_177'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_177 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_178'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_178 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_179'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_179 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_180'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_180 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_181'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_181 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_182'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_182 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_183'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_183 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_184'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_184 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_185'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_185 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_186'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_186 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_187'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_187 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_188'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_188 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_189'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_189 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_190'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_190 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_191'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_191 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_192'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_192 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_193'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_193 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_194'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_194 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_195'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_195 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_196'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_196 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_197'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_197 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_198'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_198 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_199'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_199 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_200'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_200 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_201'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_201 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_202'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_202 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_203'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_203 # type: ignore # mutmut generated
mutants_xǁHelmOutdatedReleaseEngineǁcompute__mutmut['xǁHelmOutdatedReleaseEngineǁcompute__mutmut_204'] = HelmOutdatedReleaseEngine.xǁHelmOutdatedReleaseEngineǁcompute__mutmut_204 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_breaking_changes__mutmut)
def _get_breaking_changes(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_orig(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_1(delta: str, latest_info: dict[str, object]) -> str:
    if delta != "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_2(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "XXmajorXX":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_3(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "MAJOR":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_4(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = None
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_5(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(None)
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_6(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get(None, ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_7(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", None))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_8(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get(""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_9(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_10(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("XXbreaking_changesXX", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_11(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("BREAKING_CHANGES", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_12(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", "XXXX"))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_13(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "XXMajor update: potentially breaking changesXX"
    return ""


def x__get_breaking_changes__mutmut_14(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "major update: potentially breaking changes"
    return ""


def x__get_breaking_changes__mutmut_15(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "MAJOR UPDATE: POTENTIALLY BREAKING CHANGES"
    return ""


def x__get_breaking_changes__mutmut_16(delta: str, latest_info: dict[str, object]) -> str:
    if delta == "major":
        provided = str(latest_info.get("breaking_changes", ""))
        if provided:
            return provided
        return "Major update: potentially breaking changes"
    return "XXXX"

mutants_x__get_breaking_changes__mutmut['_mutmut_orig'] = x__get_breaking_changes__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_1'] = x__get_breaking_changes__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_2'] = x__get_breaking_changes__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_3'] = x__get_breaking_changes__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_4'] = x__get_breaking_changes__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_5'] = x__get_breaking_changes__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_6'] = x__get_breaking_changes__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_7'] = x__get_breaking_changes__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_8'] = x__get_breaking_changes__mutmut_8 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_9'] = x__get_breaking_changes__mutmut_9 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_10'] = x__get_breaking_changes__mutmut_10 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_11'] = x__get_breaking_changes__mutmut_11 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_12'] = x__get_breaking_changes__mutmut_12 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_13'] = x__get_breaking_changes__mutmut_13 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_14'] = x__get_breaking_changes__mutmut_14 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_15'] = x__get_breaking_changes__mutmut_15 # type: ignore # mutmut generated
mutants_x__get_breaking_changes__mutmut['x__get_breaking_changes__mutmut_16'] = x__get_breaking_changes__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_semver__mutmut)
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


def x__parse_semver__mutmut_orig(version: str) -> tuple[int, int, int]:
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


def x__parse_semver__mutmut_1(version: str) -> tuple[int, int, int]:
    if version:
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


def x__parse_semver__mutmut_2(version: str) -> tuple[int, int, int]:
    if not version:
        return (1, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_3(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 1, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_4(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 1)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_5(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = None
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_6(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split(None)[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_7(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("XX-XX")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_8(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[1]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_9(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = None
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_10(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(None)
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_11(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split("XX.XX")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_12(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = None
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_13(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(None) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_14(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[1]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_15(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) >= 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_16(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 1 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_17(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 1
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_18(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = None
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_19(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(None) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_20(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[2]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_21(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) >= 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_22(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 2 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_23(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 1
        patch = int(parts[2]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_24(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = None  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_25(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(None) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_26(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[3]) if len(parts) > 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_27(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) >= 2 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_28(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 3 else 0  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_29(version: str) -> tuple[int, int, int]:
    if not version:
        return (0, 0, 0)
    clean = version.split("-")[0]
    parts = clean.split(".")
    try:
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 1  # noqa: PLR2004
        return (major, minor, patch)
    except (ValueError, IndexError):
        return (0, 0, 0)


def x__parse_semver__mutmut_30(version: str) -> tuple[int, int, int]:
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
        return (1, 0, 0)


def x__parse_semver__mutmut_31(version: str) -> tuple[int, int, int]:
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
        return (0, 1, 0)


def x__parse_semver__mutmut_32(version: str) -> tuple[int, int, int]:
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
        return (0, 0, 1)

mutants_x__parse_semver__mutmut['_mutmut_orig'] = x__parse_semver__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_1'] = x__parse_semver__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_2'] = x__parse_semver__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_3'] = x__parse_semver__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_4'] = x__parse_semver__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_5'] = x__parse_semver__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_6'] = x__parse_semver__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_7'] = x__parse_semver__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_8'] = x__parse_semver__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_9'] = x__parse_semver__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_10'] = x__parse_semver__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_11'] = x__parse_semver__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_12'] = x__parse_semver__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_13'] = x__parse_semver__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_14'] = x__parse_semver__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_15'] = x__parse_semver__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_16'] = x__parse_semver__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_17'] = x__parse_semver__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_18'] = x__parse_semver__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_19'] = x__parse_semver__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_20'] = x__parse_semver__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_21'] = x__parse_semver__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_22'] = x__parse_semver__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_23'] = x__parse_semver__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_24'] = x__parse_semver__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_25'] = x__parse_semver__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_26'] = x__parse_semver__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_27'] = x__parse_semver__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_28'] = x__parse_semver__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_29'] = x__parse_semver__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_30'] = x__parse_semver__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_31'] = x__parse_semver__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_semver__mutmut['x__parse_semver__mutmut_32'] = x__parse_semver__mutmut_32 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compare_semver__mutmut)
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


def x__compare_semver__mutmut_orig(current: str, latest: str) -> str:
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


def x__compare_semver__mutmut_1(current: str, latest: str) -> str:
    if latest:
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


def x__compare_semver__mutmut_2(current: str, latest: str) -> str:
    if not latest:
        return "XXdeprecatedXX"
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


def x__compare_semver__mutmut_3(current: str, latest: str) -> str:
    if not latest:
        return "DEPRECATED"
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


def x__compare_semver__mutmut_4(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = None
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


def x__compare_semver__mutmut_5(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(None)
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


def x__compare_semver__mutmut_6(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = None
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


def x__compare_semver__mutmut_7(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(None)
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


def x__compare_semver__mutmut_8(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur != (0, 0, 0):
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


def x__compare_semver__mutmut_9(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (1, 0, 0):
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


def x__compare_semver__mutmut_10(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 1, 0):
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


def x__compare_semver__mutmut_11(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 1):
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


def x__compare_semver__mutmut_12(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "XXerrorXX"
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


def x__compare_semver__mutmut_13(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "ERROR"
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


def x__compare_semver__mutmut_14(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat != (0, 0, 0):
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


def x__compare_semver__mutmut_15(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (1, 0, 0):
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


def x__compare_semver__mutmut_16(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 1, 0):
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


def x__compare_semver__mutmut_17(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 1):
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


def x__compare_semver__mutmut_18(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "XXerrorXX"
    if cur == lat:
        return "up_to_date"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_19(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "ERROR"
    if cur == lat:
        return "up_to_date"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_20(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "error"
    if cur != lat:
        return "up_to_date"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_21(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "error"
    if cur == lat:
        return "XXup_to_dateXX"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_22(current: str, latest: str) -> str:
    if not latest:
        return "deprecated"
    cur = _parse_semver(current)
    lat = _parse_semver(latest)
    if cur == (0, 0, 0):
        return "error"
    if lat == (0, 0, 0):
        return "error"
    if cur == lat:
        return "UP_TO_DATE"
    if lat[0] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_23(current: str, latest: str) -> str:
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
    if lat[1] > cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_24(current: str, latest: str) -> str:
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
    if lat[0] >= cur[0]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_25(current: str, latest: str) -> str:
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
    if lat[0] > cur[1]:
        return "major"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_26(current: str, latest: str) -> str:
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
        return "XXmajorXX"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_27(current: str, latest: str) -> str:
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
        return "MAJOR"
    if lat[1] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_28(current: str, latest: str) -> str:
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
    if lat[2] > cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_29(current: str, latest: str) -> str:
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
    if lat[1] >= cur[1]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_30(current: str, latest: str) -> str:
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
    if lat[1] > cur[2]:
        return "minor"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_31(current: str, latest: str) -> str:
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
        return "XXminorXX"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_32(current: str, latest: str) -> str:
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
        return "MINOR"
    if lat[2] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_33(current: str, latest: str) -> str:
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
    if lat[3] > cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_34(current: str, latest: str) -> str:
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
    if lat[2] >= cur[2]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_35(current: str, latest: str) -> str:
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
    if lat[2] > cur[3]:
        return "patch"
    return "up_to_date"


def x__compare_semver__mutmut_36(current: str, latest: str) -> str:
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
        return "XXpatchXX"
    return "up_to_date"


def x__compare_semver__mutmut_37(current: str, latest: str) -> str:
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
        return "PATCH"
    return "up_to_date"


def x__compare_semver__mutmut_38(current: str, latest: str) -> str:
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
    return "XXup_to_dateXX"


def x__compare_semver__mutmut_39(current: str, latest: str) -> str:
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
    return "UP_TO_DATE"

mutants_x__compare_semver__mutmut['_mutmut_orig'] = x__compare_semver__mutmut_orig # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_1'] = x__compare_semver__mutmut_1 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_2'] = x__compare_semver__mutmut_2 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_3'] = x__compare_semver__mutmut_3 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_4'] = x__compare_semver__mutmut_4 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_5'] = x__compare_semver__mutmut_5 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_6'] = x__compare_semver__mutmut_6 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_7'] = x__compare_semver__mutmut_7 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_8'] = x__compare_semver__mutmut_8 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_9'] = x__compare_semver__mutmut_9 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_10'] = x__compare_semver__mutmut_10 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_11'] = x__compare_semver__mutmut_11 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_12'] = x__compare_semver__mutmut_12 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_13'] = x__compare_semver__mutmut_13 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_14'] = x__compare_semver__mutmut_14 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_15'] = x__compare_semver__mutmut_15 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_16'] = x__compare_semver__mutmut_16 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_17'] = x__compare_semver__mutmut_17 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_18'] = x__compare_semver__mutmut_18 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_19'] = x__compare_semver__mutmut_19 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_20'] = x__compare_semver__mutmut_20 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_21'] = x__compare_semver__mutmut_21 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_22'] = x__compare_semver__mutmut_22 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_23'] = x__compare_semver__mutmut_23 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_24'] = x__compare_semver__mutmut_24 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_25'] = x__compare_semver__mutmut_25 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_26'] = x__compare_semver__mutmut_26 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_27'] = x__compare_semver__mutmut_27 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_28'] = x__compare_semver__mutmut_28 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_29'] = x__compare_semver__mutmut_29 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_30'] = x__compare_semver__mutmut_30 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_31'] = x__compare_semver__mutmut_31 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_32'] = x__compare_semver__mutmut_32 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_33'] = x__compare_semver__mutmut_33 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_34'] = x__compare_semver__mutmut_34 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_35'] = x__compare_semver__mutmut_35 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_36'] = x__compare_semver__mutmut_36 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_37'] = x__compare_semver__mutmut_37 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_38'] = x__compare_semver__mutmut_38 # type: ignore # mutmut generated
mutants_x__compare_semver__mutmut['x__compare_semver__mutmut_39'] = x__compare_semver__mutmut_39 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated
