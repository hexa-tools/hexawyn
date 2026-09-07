from dataclasses import fields


class TestAffectedCluster:
    def test_fields(self) -> None:
        from hexawyn.domain.models.cross_cluster_correlation import AffectedCluster

        names = {f.name for f in fields(AffectedCluster)}
        assert names == {"cluster_name", "onset_utc", "pod_count", "failure_type"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.cross_cluster_correlation import AffectedCluster

        cluster = AffectedCluster(
            cluster_name="prod-eu",
            onset_utc="2026-06-16T09:00:00Z",
            pod_count=8,
            failure_type="ImagePullBackOff",
        )

        assert cluster.pod_count == 8  # noqa: PLR2004
        assert cluster.failure_type == "ImagePullBackOff"


class TestCrossClusterCorrelationReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.cross_cluster_correlation import CrossClusterCorrelationReport

        report = CrossClusterCorrelationReport()

        assert report.scope == "none"
        assert report.affected_clusters == []
        assert report.common_failure_type == ""
        assert report.common_factor == ""
        assert report.suggestion == ""
        assert report.cascading is False

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.cross_cluster_correlation import CrossClusterCorrelationReport

        report = CrossClusterCorrelationReport(
            scope="global",
            common_failure_type="ImagePullBackOff",
            common_factor="container registry ghcr.io",
            suggestion="Check ghcr.io registry availability",
            cascading=False,
        )

        assert report.scope == "global"
        assert report.common_factor == "container registry ghcr.io"
