from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)


def _incident(
    downtime: int, severity: str = "minor", planned: bool = False
) -> ReliabilityIncidentRaw:
    return ReliabilityIncidentRaw(
        date="2026-06-14",
        severity=severity,
        downtime_minutes=downtime,
        resolution_minutes=downtime,
        root_cause="",
        resolved=True,
        planned_maintenance=planned,
    )


class TestUptimeFormula:
    def test_two_hours_over_thirty_days_is_99_72(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        # 2h = 120 min downtime over 30 days = 43200 min → 99.72%.
        uptime = compute_uptime_pct(incidents=[_incident(120)], period_minutes=43200)

        assert uptime == 99.72

    def test_no_incidents_is_hundred_percent(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        assert compute_uptime_pct(incidents=[], period_minutes=43200) == 100.0

    def test_multiple_incidents_downtime_summed(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        uptime = compute_uptime_pct(incidents=[_incident(15), _incident(45)], period_minutes=43200)

        # 60 min downtime over 43200 → 99.86%.
        assert uptime == 99.86


class TestMaintenanceExclusion:
    def test_planned_maintenance_excluded(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        uptime = compute_uptime_pct(incidents=[_incident(120, planned=True)], period_minutes=43200)

        assert uptime == 100.0


class TestEdgeCases:
    def test_zero_period_returns_hundred(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        assert compute_uptime_pct(incidents=[_incident(10)], period_minutes=0) == 100.0

    def test_downtime_exceeding_period_clamps_to_zero(self) -> None:
        from hexawyn.domain.services.platform_reliability.uptime_calculator import (
            compute_uptime_pct,
        )

        uptime = compute_uptime_pct(incidents=[_incident(1000)], period_minutes=500)

        assert uptime == 0.0
