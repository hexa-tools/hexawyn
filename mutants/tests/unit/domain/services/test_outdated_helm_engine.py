"""RED → GREEN — Outdated Helm Release domain logic."""

from hexawyn.domain.models.outdated_helm import OutdatedHelmRelease
from hexawyn.domain.services.outdated_helm.outdated_helm_engine import (
    HelmOutdatedReleaseEngine,
    _as_bool,
    _compare_semver,
    _get_breaking_changes,
    _parse_semver,
)


def _release(
    name: str = "nginx-ingress",
    namespace: str = "default",
    chart_name: str = "nginx-ingress",
    chart_version: str = "4.7.1",
    is_pinned: bool = False,
) -> dict[str, object]:
    return {
        "release_name": name,
        "namespace": namespace,
        "chart_name": chart_name,
        "chart_version": chart_version,
        "is_pinned": is_pinned,
    }


def _latest(
    version: str = "4.10.3",
    breaking_changes: str = "",
    repo_error: str = "",
) -> dict[str, object]:
    return {
        "chart_name": _release()["chart_name"],
        "latest_version": version,
        "breaking_changes": breaking_changes,
        "repo_error": repo_error,
    }


class TestSemverComparison:
    def test_minor_delta_detected(self) -> None:
        releases = [_release(chart_version="4.7.1")]
        latest_map = {"nginx-ingress": _latest(version="4.10.3")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.outdated_count == 1
        assert result.releases[0].delta_type == "minor"
        assert result.releases[0].current_version == "4.7.1"
        assert result.releases[0].latest_version == "4.10.3"

    def test_major_delta_critical(self) -> None:
        releases = [_release(chart_version="1.12.0", chart_name="cert-manager")]
        latest_map = {
            "cert-manager": _latest(
                version="2.0.0",
                breaking_changes="API group changed: v1alpha2 removed",
            )
        }

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.outdated_count == 1
        assert result.releases[0].delta_type == "major"
        assert "v1alpha2 removed" in result.releases[0].breaking_changes

    def test_up_to_date_not_counted_as_outdated(self) -> None:
        releases = [_release(chart_version="2.45.0")]
        latest_map = {"nginx-ingress": _latest(version="2.45.0")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.outdated_count == 0
        assert result.up_to_date_count == 1

    def test_patch_delta_detected(self) -> None:
        releases = [_release(chart_version="4.7.0")]
        latest_map = {"nginx-ingress": _latest(version="4.7.1")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.releases[0].delta_type == "patch"

    def test_five_of_eight_outdated(self) -> None:
        releases = [
            _release(name=f"release-{i}", chart_name=f"chart-{i}", chart_version=f"1.{i}.0")
            for i in range(8)
        ]
        latest_map = {f"chart-{i}": _latest(version=f"1.{i}.0") for i in range(3)}
        latest_map.update({f"chart-{i}": _latest(version=f"2.{i}.0") for i in range(3, 8)})

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.outdated_count == 5  # noqa: PLR2004
        assert result.up_to_date_count == 3  # noqa: PLR2004
        assert result.total_releases == 8  # noqa: PLR2004


class TestEdgeCases:
    def test_repo_error_marks_as_skipped(self) -> None:
        releases = [_release(chart_version="1.0.0")]
        latest_map = {"nginx-ingress": _latest(repo_error="timeout")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.error_count == 1
        assert result.releases[0].delta_type == "error"
        assert result.releases[0].repo_error == "timeout"

    def test_pinned_release_excluded(self) -> None:
        releases = [_release(is_pinned=True)]
        latest_map = {"nginx-ingress": _latest(version="2.0.0")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.outdated_count == 0
        assert result.total_releases == 1
        assert len(result.releases) == 0

    def test_chart_removed_from_repo_deprecated(self) -> None:
        releases = [_release(chart_version="1.0.0")]
        latest_map = {"nginx-ingress": _latest(version="")}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.releases[0].delta_type == "deprecated"
        assert result.outdated_count == 1

    def test_multiple_releases_different_namespaces(self) -> None:
        releases = [
            _release(name="nginx-prod", namespace="production", chart_version="4.7.1"),
            _release(name="nginx-staging", namespace="staging", chart_version="4.10.0"),
        ]
        latest_map = {
            "nginx-ingress": _latest(version="4.10.3"),
        }

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.total_releases == 2  # noqa: PLR2004
        assert result.outdated_count == 2  # noqa: PLR2004

    def test_chart_not_in_latest_map_gets_default(self) -> None:
        releases = [_release(chart_version="1.0.0")]
        latest_map: dict[str, dict[str, object]] = {}

        engine = HelmOutdatedReleaseEngine()
        result = engine.compute(releases, latest_map)

        assert result.releases[0].delta_type == "error"
        assert result.releases[0].repo_error == "chart not found in repository"


class TestSemverParser:
    def test_parse_simple_semver(self) -> None:
        assert _parse_semver("4.7.1") == (4, 7, 1)

    def test_parse_with_pre_release_ignored(self) -> None:
        assert _parse_semver("4.7.1-beta.1") == (4, 7, 1)

    def test_parse_invalid_returns_zeros(self) -> None:
        assert _parse_semver("invalid") == (0, 0, 0)

    def test_parse_empty_returns_zeros(self) -> None:
        assert _parse_semver("") == (0, 0, 0)

    def test_compare_minor_update(self) -> None:
        assert _compare_semver("4.7.1", "4.10.3") == "minor"

    def test_compare_major_update(self) -> None:
        assert _compare_semver("1.12.0", "2.0.0") == "major"

    def test_compare_patch_update(self) -> None:
        assert _compare_semver("4.7.0", "4.7.1") == "patch"

    def test_compare_same_version(self) -> None:
        assert _compare_semver("2.45.0", "2.45.0") == "up_to_date"

    def test_compare_empty_latest_is_deprecated(self) -> None:
        assert _compare_semver("1.0.0", "") == "deprecated"

    def test_compare_invalid_current(self) -> None:
        assert _compare_semver("bad", "4.7.1") == "error"

    def test_compare_invalid_latest(self) -> None:
        assert _compare_semver("1.0.0", "bad") == "error"

    def test_compare_current_newer_than_latest(self) -> None:
        assert _compare_semver("2.0.0", "1.0.0") == "up_to_date"

    def test_parse_single_part(self) -> None:
        assert _parse_semver("1") == (1, 0, 0)

    def test_parse_two_parts(self) -> None:
        assert _parse_semver("1.2") == (1, 2, 0)

    def test_as_bool_none_returns_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_returns_true(self) -> None:
        assert _as_bool("yes") is True

    def test_as_bool_zero_returns_false(self) -> None:
        assert _as_bool(0) is False

    def test_invalid_current_version_in_engine_returns_error(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(chart_version="bad")]
        latest_map = {"nginx-ingress": _latest(version="4.7.1")}

        result = engine.compute(releases, latest_map)

        assert result.error_count == 1
        assert result.releases[0].delta_type == "error"


def _expected_release(  # noqa: PLR0913
    release_name: str = "nginx-ingress",
    namespace: str = "default",
    chart_name: str = "nginx-ingress",
    current_version: str = "4.7.1",
    latest_version: str = "4.10.3",
    delta_type: str = "minor",
    breaking_changes: str = "",
    is_pinned: bool = False,
    repo_error: str = "",
) -> OutdatedHelmRelease:
    return OutdatedHelmRelease(
        release_name=release_name,
        namespace=namespace,
        chart_name=chart_name,
        current_version=current_version,
        latest_version=latest_version,
        delta_type=delta_type,
        breaking_changes=breaking_changes,
        is_pinned=is_pinned,
        repo_error=repo_error,
    )


class TestRepoErrorEquality:
    def test_repo_error_entry_exact_fields(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(name="nginx-prod", namespace="prod", chart_version="4.7.1")]
        latest_map = {
            "nginx-ingress": _latest(version="4.10.3", repo_error="timeout"),
        }

        result = engine.compute(releases, latest_map)

        assert result.error_count == 1
        assert result.releases == [
            _expected_release(
                release_name="nginx-prod",
                namespace="prod",
                latest_version="4.10.3",
                delta_type="error",
                repo_error="timeout",
            )
        ]

    def test_repo_error_entry_unknown_latest_when_missing(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        latest_map = {"nginx-ingress": {"repo_error": "404", "breaking_changes": ""}}

        result = engine.compute([_release()], latest_map)

        assert result.releases[0].latest_version == "unknown"
        assert result.releases[0].repo_error == "404"

    def test_repo_error_entry_defaults_when_keys_missing(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases: list[dict[str, object]] = [{"is_pinned": False}]
        latest_map: dict[str, dict[str, object]] = {"": {"repo_error": "boom"}}

        result = engine.compute(releases, latest_map)

        assert result.releases == [
            _expected_release(
                release_name="",
                namespace="",
                chart_name="",
                current_version="",
                latest_version="unknown",
                delta_type="error",
                repo_error="boom",
            )
        ]


class TestChartNotFoundEquality:
    def test_chart_not_found_entry_exact_fields(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(name="nginx-prod", namespace="prod", chart_version="1.2.3")]

        result = engine.compute(releases, {})

        assert result.error_count == 1
        assert result.releases == [
            _expected_release(
                release_name="nginx-prod",
                namespace="prod",
                current_version="1.2.3",
                latest_version="unknown",
                delta_type="error",
                repo_error="chart not found in repository",
            )
        ]

    def test_chart_not_found_entry_defaults_when_keys_missing(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases: list[dict[str, object]] = [{"is_pinned": False}]

        result = engine.compute(releases, {})

        assert result.releases == [
            _expected_release(
                release_name="",
                namespace="",
                chart_name="",
                current_version="",
                latest_version="unknown",
                delta_type="error",
                repo_error="chart not found in repository",
            )
        ]


class TestDeltaBranchEquality:
    def test_up_to_date_entry_exact_fields(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(name="nginx-prod", namespace="prod", chart_version="4.10.3")]
        latest_map = {"nginx-ingress": _latest(version="4.10.3")}

        result = engine.compute(releases, latest_map)

        assert result.up_to_date_count == 1
        assert result.releases == [
            _expected_release(
                release_name="nginx-prod",
                namespace="prod",
                current_version="4.10.3",
                latest_version="4.10.3",
                delta_type="up_to_date",
            )
        ]

    def test_major_entry_carries_provided_breaking_changes(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(chart_name="cert-manager", chart_version="1.12.0")]
        latest_map = {
            "cert-manager": _latest(
                version="2.0.0",
                breaking_changes="API group changed: v1alpha2 removed",
            )
        }

        result = engine.compute(releases, latest_map)

        assert result.releases == [
            _expected_release(
                chart_name="cert-manager",
                current_version="1.12.0",
                latest_version="2.0.0",
                delta_type="major",
                breaking_changes="API group changed: v1alpha2 removed",
            )
        ]

    def test_error_delta_entry_from_invalid_current(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [_release(chart_version="not-a-version")]

        result = engine.compute(releases, {"nginx-ingress": _latest(version="4.10.3")})

        assert result.error_count == 1
        assert result.releases == [
            _expected_release(
                current_version="not-a-version",
                delta_type="error",
            )
        ]

    def test_up_to_date_entry_defaults_when_name_keys_missing(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases: list[dict[str, object]] = [
            {"chart_name": "nginx-ingress", "chart_version": "4.10.3"}
        ]
        latest_map = {"nginx-ingress": _latest(version="4.10.3")}

        result = engine.compute(releases, latest_map)

        assert result.releases == [
            _expected_release(
                release_name="",
                namespace="",
                current_version="4.10.3",
                latest_version="4.10.3",
                delta_type="up_to_date",
            )
        ]

    def test_deprecated_when_latest_missing_version_key(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        latest_map: dict[str, dict[str, object]] = {
            "nginx-ingress": {"chart_name": "nginx-ingress"}
        }

        result = engine.compute([_release(chart_version="1.0.0")], latest_map)

        assert result.releases == [
            _expected_release(
                current_version="1.0.0",
                latest_version="",
                delta_type="deprecated",
            )
        ]
        assert result.outdated_count == 1


class TestPinnedReleaseOrdering:
    def test_pinned_release_before_outdated_still_processes_later(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [
            _release(name="pinned-nginx", is_pinned=True),
            _release(name="nginx-live", chart_version="4.7.1"),
        ]
        latest_map = {"nginx-ingress": _latest(version="4.10.3")}

        result = engine.compute(releases, latest_map)

        assert len(result.releases) == 1
        assert result.releases[0].release_name == "nginx-live"


class TestErrorOrdering:
    def test_repo_error_before_outdated_still_processes_later(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [
            _release(name="broken-nginx", chart_name="broken-chart", chart_version="1.0.0"),
            _release(name="nginx-live", chart_version="4.7.1"),
        ]
        latest_map: dict[str, dict[str, object]] = {
            "broken-chart": {"repo_error": "boom", "breaking_changes": ""},
            "nginx-ingress": _latest(version="4.10.3"),
        }

        result = engine.compute(releases, latest_map)

        assert len(result.releases) == 2  # noqa: PLR2004
        assert result.releases[1].release_name == "nginx-live"
        assert result.releases[1].delta_type == "minor"

    def test_chart_not_found_before_outdated_still_processes_later(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [
            _release(name="missing-nginx", chart_name="ghost-chart", chart_version="1.0.0"),
            _release(name="nginx-live", chart_version="4.7.1"),
        ]
        latest_map = {"nginx-ingress": _latest(version="4.10.3")}

        result = engine.compute(releases, latest_map)

        assert len(result.releases) == 2  # noqa: PLR2004
        assert result.releases[1].release_name == "nginx-live"


class TestErrorCountAccumulation:
    def test_multiple_error_kinds_accumulate(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [
            _release(name="repo-broken", chart_name="broken-chart", chart_version="1.0.0"),
            _release(name="ghost-release", chart_name="ghost-chart", chart_version="1.0.0"),
            _release(name="bad-version", chart_name="normal-chart", chart_version="not-a-version"),
        ]
        latest_map: dict[str, dict[str, object]] = {
            "broken-chart": {"repo_error": "boom", "breaking_changes": ""},
            "normal-chart": _latest(version="4.10.3"),
        }

        result = engine.compute(releases, latest_map)

        assert result.error_count == 3  # noqa: PLR2004

    def test_two_repo_errors_accumulate(self) -> None:
        engine = HelmOutdatedReleaseEngine()
        releases = [
            _release(name="first", chart_name="broken-a", chart_version="1.0.0"),
            _release(name="second", chart_name="broken-b", chart_version="1.0.0"),
        ]
        latest_map: dict[str, dict[str, object]] = {
            "broken-a": {"repo_error": "boom", "breaking_changes": ""},
            "broken-b": {"repo_error": "boom", "breaking_changes": ""},
        }

        result = engine.compute(releases, latest_map)

        assert result.error_count == 2  # noqa: PLR2004


class TestBreakingChangesHelper:
    def test_major_without_provided_returns_fallback(self) -> None:
        assert _get_breaking_changes("major", {}) == "Major update: potentially breaking changes"

    def test_major_with_provided_returns_it(self) -> None:
        assert _get_breaking_changes("major", {"breaking_changes": "custom note"}) == "custom note"

    def test_minor_delta_returns_empty(self) -> None:
        assert _get_breaking_changes("minor", {"breaking_changes": "ignored"}) == ""

    def test_patch_delta_returns_empty(self) -> None:
        assert _get_breaking_changes("patch", {}) == ""
