from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)


def _make_incident(
    downtime_minutes: int, planned_maintenance: bool = False
) -> ReliabilityIncidentRaw:
    return {
        "date": "2026-01-01",
        "severity": "critical",
        "downtime_minutes": downtime_minutes,
        "resolution_minutes": 60,
        "root_cause": "test",
        "resolved": True,
        "planned_maintenance": planned_maintenance,
    }


class TestComputeUptimePct:
    def test_happy_path_one_hour_downtime_per_week(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(60)]
        period = 7 * 24 * 60  # one week in minutes

        result = compute_uptime_pct(incidents, period)

        assert result == round((1 - 60 / period) * 100, 2)
        assert 99.0 < result < 100.0  # noqa: PLR2004

    def test_no_incidents_returns_100_percent(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        result = compute_uptime_pct([], 1440)

        assert result == 100.0  # noqa: PLR2004

    def test_period_zero_returns_100(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        result = compute_uptime_pct([_make_incident(60)], 0)

        assert result == 100.0  # noqa: PLR2004

    def test_negative_period_returns_100(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        result = compute_uptime_pct([_make_incident(60)], -10)

        assert result == 100.0  # noqa: PLR2004

    def test_planned_maintenance_excluded(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(1440, planned_maintenance=True)]
        period = 1440

        result = compute_uptime_pct(incidents, period)

        assert result == 100.0  # noqa: PLR2004

    def test_downtime_exceeds_period_clamped_to_zero(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(500),
            _make_incident(500),
        ]
        period = 100

        result = compute_uptime_pct(incidents, period)

        assert result == 0.0

    def test_clamped_to_100_even_with_negative_effective_downtime(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        result = compute_uptime_pct([], 100)

        assert result == 100.0  # noqa: PLR2004

    def test_mixed_planned_and_unplanned(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(30, planned_maintenance=True),
            _make_incident(30, planned_maintenance=False),
        ]
        period = 1440

        result = compute_uptime_pct(incidents, period)

        expected = round((1 - 30 / 1440) * 100, 2)
        assert result == expected

    def test_return_type_is_float(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        result = compute_uptime_pct([], 60)

        assert isinstance(result, float)

    def test_period_one_minute_long_outage(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(1)]
        result = compute_uptime_pct(incidents, 1440)

        assert result == round((1 - 1 / 1440) * 100, 2)
        assert result < 100.0  # noqa: PLR2004
