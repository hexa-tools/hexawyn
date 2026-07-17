from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
)


def _sig(
    cluster: str = "prod-eu",
    failure: str = "ImagePullBackOff",
    pods: int = 8,
    onset: str = "2026-06-16T09:00:00Z",
    service: str = "payment-service",
    dependency: str | None = "ghcr.io",
) -> ClusterFailureSignature:
    return ClusterFailureSignature(
        cluster_name=cluster,
        failure_type=failure,
        pod_count=pods,
        onset_utc=onset,
        affected_service=service,
        shared_dependency=dependency,
    )


class TestCorrelation:
    def test_same_failure_two_clusters_regional(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", onset="2026-06-16T09:00:00Z"),
                _sig("prod-us", onset="2026-06-16T09:02:00Z"),
            ],
            window_minutes=30,
        )

        assert report.scope == "regional"
        assert report.common_failure_type == "ImagePullBackOff"

    def test_isolated_single_cluster(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate([_sig("prod-eu")], window_minutes=30)

        assert report.scope == "isolated"

    def test_different_failures_no_correlation(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", failure="ImagePullBackOff"),
                _sig("prod-us", failure="CrashLoopBackOff"),
            ],
            window_minutes=30,
        )

        assert report.scope in ("isolated", "none")


class TestCascading:
    def test_delayed_onset_cascading(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-us", onset="2026-06-16T09:00:00Z"),
                _sig("prod-eu", onset="2026-06-16T09:10:00Z"),
            ],
            window_minutes=30,
        )

        assert report.cascading is True


class TestScopeClassification:
    def test_three_clusters_all_global(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu"),
                _sig("prod-us"),
                _sig("prod-asia"),
            ],
            window_minutes=30,
        )

        assert report.scope == "global"

    def test_outside_window_excluded(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", onset="2026-06-16T09:00:00Z"),
                _sig("prod-us", onset="2026-06-16T10:00:00Z"),
            ],
            window_minutes=30,
        )

        # EU at 09:00, US at 10:00 = 60 min apart, outside 30 min window.
        assert report.scope in ("isolated", "none")


class TestEdgeCases:
    def test_same_onset_not_cascading(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", onset="2026-06-16T09:00:00Z"),
                _sig("prod-us", onset="2026-06-16T09:00:00Z"),
            ],
            window_minutes=30,
        )

        assert report.cascading is False

    def test_global_with_shared_dependency(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", dependency="ghcr.io"),
                _sig("prod-us", dependency="ghcr.io"),
                _sig("prod-asia", dependency="ghcr.io"),
            ],
            window_minutes=30,
        )

        assert report.scope == "global"
        assert "ghcr.io" in report.suggestion.lower()

    def test_different_dependencies_no_common(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", dependency="ecr.io"),
                _sig("prod-us", dependency="ghcr.io"),
            ],
            window_minutes=30,
        )

        assert report.common_factor == ""

    def test_suggestion_without_dependency(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", dependency=None),
                _sig("prod-us", dependency=None),
                _sig("prod-asia", dependency=None),
            ],
            window_minutes=30,
        )

        assert report.scope == "global"
        assert "infrastructure" in report.suggestion.lower()

    def test_single_type_all_same_is_isolated(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [_sig("prod-eu"), _sig("prod-eu", failure="OtherType")],
            window_minutes=30,
        )

        assert report.scope == "isolated"

    def test_regional_without_dependency_suggestion(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", dependency=None),
                _sig("prod-us", dependency=None),
            ],
            window_minutes=30,
        )

        assert report.scope == "regional"
        assert "regional" in report.suggestion.lower()

    def test_two_clusters_regional_suggestion(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", failure="CrashLoopBackOff", dependency=None),
                _sig("prod-us", failure="CrashLoopBackOff", dependency=None),
            ],
            window_minutes=30,
        )

        assert report.scope == "regional"
        assert report.suggestion != ""

    def test_cascading_true(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-us", onset="2026-06-16T09:00:00Z"),
                _sig("prod-eu", onset="2026-06-16T09:10:00Z"),
            ],
            window_minutes=30,
        )

        assert report.cascading is True

    def test_grouped_empty_fallback(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate(
            [
                _sig("prod-eu", failure="TypeA"),
                _sig("prod-us", failure="TypeB"),
                _sig("prod-asia", failure="TypeC"),
            ],
            window_minutes=30,
        )

        assert report.scope in ("isolated", "none")


class TestEmpty:
    def test_no_data_returns_empty(self) -> None:
        from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
            correlate,
        )

        report = correlate([], window_minutes=30)

        assert report.scope == "none"
        assert report.has_data is False
