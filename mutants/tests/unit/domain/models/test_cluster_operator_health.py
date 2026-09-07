from dataclasses import fields


class TestClusterOperatorStatus:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.cluster_operator_health import ClusterOperatorStatus

        field_names = {f.name for f in fields(ClusterOperatorStatus)}

        assert field_names == {
            "name",
            "available",
            "progressing",
            "degraded",
            "health",
            "message",
            "degraded_duration_minutes",
            "is_chronic",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.cluster_operator_health import ClusterOperatorStatus

        status = ClusterOperatorStatus(
            name="etcd",
            available=True,
            progressing=False,
            degraded=True,
            health="degraded",
            message="etcd member not responding",
            degraded_duration_minutes=120,
            is_chronic=True,
        )

        assert status.name == "etcd"
        assert status.is_chronic is True


class TestClusterOperatorHealthReport:
    def test_defaults_to_all_healthy_empty(self) -> None:
        from hexawyn.domain.models.cluster_operator_health import (
            ClusterOperatorHealthReport,
        )

        report = ClusterOperatorHealthReport()

        assert report.operators == []
        assert report.total == 0
        assert report.healthy == 0
        assert report.degraded == 0
        assert report.progressing == 0
        assert report.all_healthy is True

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.cluster_operator_health import (
            ClusterOperatorHealthReport,
        )

        report = ClusterOperatorHealthReport(
            total=32, healthy=30, degraded=1, progressing=1, all_healthy=False
        )

        assert report.total == 32  # noqa: PLR2004
        assert report.healthy == 30  # noqa: PLR2004
        assert report.all_healthy is False
