from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
)
from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (  # noqa: E501
    ClusterOperatorHealthService,
)


def _make_operator(  # noqa: PLR0913
    name: str = "authentication",
    available: bool = True,
    progressing: bool = False,
    degraded: bool = False,
    available_unknown: bool = False,
    message: str = "",
    degraded_since: str | None = None,
) -> ClusterOperatorRawData:
    return {
        "name": name,
        "available": available,
        "progressing": progressing,
        "degraded": degraded,
        "available_unknown": available_unknown,
        "message": message,
        "degraded_since": degraded_since,
    }


class TestClusterOperatorHealthService:
    def test_happy_path_all_healthy(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication"),
            _make_operator(name="console"),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.total == 2  # noqa: PLR2004
        assert report.healthy == 2  # noqa: PLR2004
        assert report.degraded == 0
        assert report.progressing == 0
        assert report.all_healthy is True

    def test_degraded_operator(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.degraded == 1
        assert report.healthy == 0
        assert report.all_healthy is False
        assert report.operators[0].health == "degraded"

    def test_progressing_operator(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", available=False, progressing=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.progressing == 1
        assert report.operators[0].health == "progressing"

    def test_unknown_when_available_unknown(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", available_unknown=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].health == "unknown"

    def test_unknown_when_no_condition_true(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", available=False),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].health == "unknown"

    def test_available_unknown_overrides_degraded(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True, available_unknown=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].health == "unknown"

    def test_degraded_overrides_progressing(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True, progressing=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].health == "degraded"

    def test_not_chronic_under_threshold(self) -> None:
        recent = datetime(2026, 7, 1, 12, 10, 0, tzinfo=UTC)

        def fixed_clock() -> datetime:
            return recent

        operators: list[ClusterOperatorRawData] = [
            _make_operator(
                name="authentication",
                degraded=True,
                degraded_since="2026-07-01T12:00:00Z",
            ),
        ]
        service = ClusterOperatorHealthService(clock=fixed_clock)
        report = service.evaluate(operators)

        assert report.operators[0].is_chronic is False
        assert report.operators[0].degraded_duration_minutes <= 15  # noqa: PLR2004

    def test_chronic_beyond_threshold(self) -> None:
        stuck_time = datetime(2026, 7, 1, 13, 0, 0, tzinfo=UTC)

        def fixed_clock() -> datetime:
            return stuck_time

        operators: list[ClusterOperatorRawData] = [
            _make_operator(
                name="authentication",
                degraded=True,
                degraded_since="2026-07-01T12:00:00Z",
            ),
        ]
        service = ClusterOperatorHealthService(clock=fixed_clock)
        report = service.evaluate(operators)

        assert report.operators[0].is_chronic is True
        assert report.operators[0].degraded_duration_minutes > 15  # noqa: PLR2004

    def test_non_degraded_zero_chronic_duration(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication"),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].degraded_duration_minutes == 0
        assert report.operators[0].is_chronic is False

    def test_degraded_since_none_zero_duration(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True, degraded_since=None),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].degraded_duration_minutes == 0

    def test_invalid_degraded_since_returns_zero(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True, degraded_since="not-a-date"),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].degraded_duration_minutes == 0

    def test_empty_operators_list(self) -> None:
        service = ClusterOperatorHealthService()
        report = service.evaluate([])

        assert report.total == 0
        assert report.healthy == 0
        assert report.all_healthy is True

    def test_mixed_operators(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication"),
            _make_operator(name="console", degraded=True),
            _make_operator(name="dns", progressing=True, available=False),
            _make_operator(name="image-registry", available_unknown=True),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.total == 4  # noqa: PLR2004
        assert report.healthy == 1
        assert report.degraded == 1
        assert report.progressing == 1
        assert report.all_healthy is False

    def test_operator_with_message(self) -> None:
        operators: list[ClusterOperatorRawData] = [
            _make_operator(name="authentication", degraded=True, message="RoutesNotAvailable"),
        ]
        service = ClusterOperatorHealthService()
        report = service.evaluate(operators)

        assert report.operators[0].message == "RoutesNotAvailable"
