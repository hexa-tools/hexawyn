"""RED → GREEN — Layer 1: Outdated Helm domain models."""

from hexawyn.domain.models.outdated_helm import OutdatedHelmRelease, OutdatedHelmReport


class TestOutdatedHelmRelease:
    def test_is_frozen(self) -> None:
        import pytest

        rel = OutdatedHelmRelease(
            release_name="test",
            namespace="default",
            chart_name="chart",
            current_version="1.0.0",
            latest_version="2.0.0",
            delta_type="major",
            breaking_changes="breaking",
            is_pinned=False,
            repo_error="",
        )
        with pytest.raises(Exception):
            rel.delta_type = "minor"  # type: ignore[misc]

    def test_all_fields_accessible(self) -> None:
        rel = OutdatedHelmRelease(
            release_name="nginx",
            namespace="prod",
            chart_name="nginx-ingress",
            current_version="4.7.1",
            latest_version="4.10.3",
            delta_type="minor",
            breaking_changes="",
            is_pinned=False,
            repo_error="",
        )
        assert rel.release_name == "nginx"
        assert rel.delta_type == "minor"
        assert rel.is_pinned is False


class TestOutdatedHelmReport:
    def test_default_values(self) -> None:
        report = OutdatedHelmReport()
        assert report.total_releases == 0
        assert report.outdated_count == 0
        assert report.releases == []

    def test_can_populate(self) -> None:
        report = OutdatedHelmReport(
            total_releases=8,
            outdated_count=5,
            up_to_date_count=3,
            error_count=0,
        )
        assert report.total_releases == 8  # noqa: PLR2004
        assert report.outdated_count == 5  # noqa: PLR2004
