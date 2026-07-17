from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
)


def _now() -> datetime:
    return datetime(2026, 6, 16, 3, 0, 0, tzinfo=UTC)


def _raw(
    name: str,
    available: bool = True,
    progressing: bool = False,
    degraded: bool = False,
    message: str = "",
    degraded_since: str | None = None,
    available_unknown: bool = False,
) -> ClusterOperatorRawData:
    return ClusterOperatorRawData(
        name=name,
        available=available,
        progressing=progressing,
        degraded=degraded,
        available_unknown=available_unknown,
        message=message,
        degraded_since=degraded_since,
    )


class TestSummary:
    def test_counts_healthy_degraded_progressing(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw(f"op-{i}") for i in range(30)]
        operators.append(_raw("etcd", degraded=True, message="etcd member not responding"))
        operators.append(_raw("ingress", progressing=True, message="Updating router deployment"))

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.total == 32
        assert report.healthy == 30
        assert report.degraded == 1
        assert report.progressing == 1
        assert report.all_healthy is False

    def test_all_available_is_all_healthy(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("authentication"), _raw("dns"), _raw("network")]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.all_healthy is True
        assert report.healthy == 3
        assert report.degraded == 0


class TestConditionParsing:
    def test_degraded_message_surfaced(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("etcd", degraded=True, message="etcd member ip-10-0-1-5 not responding")]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].message == "etcd member ip-10-0-1-5 not responding"
        assert report.operators[0].health == "degraded"

    def test_available_unknown_is_not_healthy(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("kube-apiserver", available=False, available_unknown=True)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].health == "unknown"
        assert report.healthy == 0
        assert report.all_healthy is False

    def test_degraded_takes_priority_over_progressing(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("etcd", progressing=True, degraded=True, message="bad")]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].health == "degraded"
        assert report.degraded == 1
        assert report.progressing == 0


class TestChronicity:
    def test_progressing_three_minutes_is_transient(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        since = (_now() - timedelta(minutes=3)).isoformat().replace("+00:00", "Z")
        operators = [_raw("ingress", progressing=True, degraded=True, degraded_since=since)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].is_chronic is False
        assert report.operators[0].degraded_duration_minutes == 3

    def test_degraded_two_hours_is_chronic(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        since = (_now() - timedelta(hours=2)).isoformat().replace("+00:00", "Z")
        operators = [_raw("etcd", degraded=True, degraded_since=since)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].is_chronic is True
        assert report.operators[0].degraded_duration_minutes == 120

    def test_exactly_fifteen_minutes_is_not_chronic(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        since = (_now() - timedelta(minutes=15)).isoformat().replace("+00:00", "Z")
        operators = [_raw("etcd", degraded=True, degraded_since=since)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].is_chronic is False

    def test_sixteen_minutes_is_chronic(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        since = (_now() - timedelta(minutes=16)).isoformat().replace("+00:00", "Z")
        operators = [_raw("etcd", degraded=True, degraded_since=since)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].is_chronic is True

    def test_missing_degraded_since_is_not_chronic(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("etcd", degraded=True, degraded_since=None)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].degraded_duration_minutes == 0
        assert report.operators[0].is_chronic is False

    def test_malformed_degraded_since_is_not_chronic(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("etcd", degraded=True, degraded_since="not-a-date")]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].degraded_duration_minutes == 0
        assert report.operators[0].is_chronic is False


class TestOrdering:
    def test_unhealthy_operators_listed_first(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [
            _raw("authentication"),
            _raw("ingress", progressing=True),
            _raw("etcd", degraded=True),
        ]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].name == "etcd"
        assert report.operators[1].name == "ingress"
        assert report.operators[2].name == "authentication"


class TestAvailabilityEdgeCases:
    def test_available_false_without_unknown_flag_is_unknown(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        operators = [_raw("network", available=False)]

        report = ClusterOperatorHealthService(clock=_now).evaluate(operators)

        assert report.operators[0].health == "unknown"
        assert report.healthy == 0
        assert report.all_healthy is False

    def test_default_clock_is_used_when_none_injected(self) -> None:
        from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
            ClusterOperatorHealthService,
        )

        since = "2020-01-01T00:00:00Z"
        report = ClusterOperatorHealthService().evaluate(
            [_raw("etcd", degraded=True, degraded_since=since)]
        )

        assert report.total == 1
        assert report.operators[0].is_chronic is True
        assert report.operators[0].degraded_duration_minutes > 15
