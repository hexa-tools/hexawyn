from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
)
from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
    correlate,
)


def _make_failure(  # noqa: PLR0913
    cluster_name: str = "cluster-a",
    failure_type: str = "ImagePullBackOff",
    pod_count: int = 5,
    onset_utc: str = "2026-07-01T12:00:00Z",
    affected_service: str = "api-gateway",
    shared_dependency: str | None = None,
) -> ClusterFailureSignature:
    return {
        "cluster_name": cluster_name,
        "failure_type": failure_type,
        "pod_count": pod_count,
        "onset_utc": onset_utc,
        "affected_service": affected_service,
        "shared_dependency": shared_dependency,
    }


class TestCorrelate:
    def test_happy_path_regional_correlation(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T12:05:00Z"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.scope == "regional"
        assert result.has_data is True
        assert result.cascading is True
        assert len(result.affected_clusters) == 2  # noqa: PLR2004
        assert result.common_failure_type == "ImagePullBackOff"

    def test_global_scope_three_clusters(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T12:05:00Z"),
            _make_failure(cluster_name="cluster-c", onset_utc="2026-07-01T12:10:00Z"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.scope == "global"

    def test_isolated_single_failure(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.scope == "isolated"
        assert result.has_data is True

    def test_empty_failures_returns_no_data(self) -> None:
        result = correlate([], window_minutes=30)

        assert result.scope == "none"
        assert result.has_data is False
        assert "Aucune" in result.warning

    def test_window_filters_out_late_onset(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T14:00:00Z"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.scope == "isolated"
        assert len(result.affected_clusters) == 1

    def test_different_failure_types_isolated(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", failure_type="ImagePullBackOff"),
            _make_failure(cluster_name="cluster-b", failure_type="CrashLoopBackOff"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.scope == "isolated"

    def test_common_factor_single_shared_dependency(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(
                cluster_name="cluster-a",
                onset_utc="2026-07-01T12:00:00Z",
                shared_dependency="ghcr.io/my-image",
            ),
            _make_failure(
                cluster_name="cluster-b",
                onset_utc="2026-07-01T12:02:00Z",
                shared_dependency="ghcr.io/my-image",
            ),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.common_factor == "ghcr.io/my-image"
        assert "registry" in result.suggestion.lower()

    def test_common_factor_multiple_dependencies_none(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(
                cluster_name="cluster-a",
                onset_utc="2026-07-01T12:00:00Z",
                shared_dependency="dep-a",
            ),
            _make_failure(
                cluster_name="cluster-b",
                onset_utc="2026-07-01T12:02:00Z",
                shared_dependency="dep-b",
            ),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.common_factor == ""

    def test_common_factor_none_when_no_dependency(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T12:02:00Z"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.common_factor == ""

    def test_no_cascading_same_onset_time(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T12:00:00Z"),
        ]

        result = correlate(failures, window_minutes=30)

        assert result.cascading is False

    def test_zero_window_minutes(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(cluster_name="cluster-a", onset_utc="2026-07-01T12:00:00Z"),
            _make_failure(cluster_name="cluster-b", onset_utc="2026-07-01T12:01:00Z"),
        ]

        result = correlate(failures, window_minutes=0)

        assert len(result.affected_clusters) == 1
        assert result.scope == "isolated"

    def test_affected_cluster_fields_correct(self) -> None:
        failures: list[ClusterFailureSignature] = [
            _make_failure(
                cluster_name="cluster-x",
                failure_type="OOMKilled",
                pod_count=12,
                onset_utc="2026-07-01T12:00:00Z",
                affected_service="payment-api",
            ),
            _make_failure(
                cluster_name="cluster-y",
                failure_type="OOMKilled",
                pod_count=5,
                onset_utc="2026-07-01T12:02:00Z",
                affected_service="checkout-svc",
            ),
        ]

        result = correlate(failures, window_minutes=30)

        assert len(result.affected_clusters) == 2  # noqa: PLR2004
        cluster = result.affected_clusters[0]
        assert cluster.cluster_name == "cluster-x"
        assert cluster.pod_count == 12  # noqa: PLR2004
        assert cluster.failure_type == "OOMKilled"
