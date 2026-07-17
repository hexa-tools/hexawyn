"""RED → GREEN — Outdated Helm Release domain logic."""

from hexawyn.domain.services.outdated_helm.outdated_helm_engine import (
    HelmOutdatedReleaseEngine,
    _as_bool,
    _compare_semver,
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

        assert result.outdated_count == 5
        assert result.up_to_date_count == 3
        assert result.total_releases == 8


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

        assert result.total_releases == 2
        assert result.outdated_count == 2

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
