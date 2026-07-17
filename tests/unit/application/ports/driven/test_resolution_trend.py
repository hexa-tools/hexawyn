from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)


def _incident(resolution: int) -> ReliabilityIncidentRaw:
    return ReliabilityIncidentRaw(
        date="2026-06-14",
        severity="minor",
        downtime_minutes=resolution,
        resolution_minutes=resolution,
        root_cause="",
        resolved=True,
        planned_maintenance=False,
    )


class TestAverageResolution:
    def test_average_of_resolution_minutes(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution(incidents=[_incident(10), _incident(14)], previous_avg=None)

        assert result.avg_resolution_minutes == 12

    def test_no_incidents_zero_average(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution(incidents=[], previous_avg=None)

        assert result.avg_resolution_minutes == 0


class TestDeltaAndTrend:
    def test_improving_when_faster_than_previous(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        # 12 min now vs ~14 previous → -15% (improving = faster).
        result = compute_resolution(incidents=[_incident(12)], previous_avg=14)

        assert result.resolution_delta_pct < 0
        assert result.resolution_trend == "improving"

    def test_degrading_when_slower(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution(incidents=[_incident(20)], previous_avg=10)

        assert result.resolution_delta_pct > 0
        assert result.resolution_trend == "degrading"

    def test_stable_when_no_previous(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution(incidents=[_incident(12)], previous_avg=None)

        assert result.resolution_trend == "stable"
        assert result.resolution_delta_pct == 0.0

    def test_stable_when_equal(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution(incidents=[_incident(12)], previous_avg=12)

        assert result.resolution_trend == "stable"

    def test_delta_pct_is_minus_15(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        # Previous 14.1 → current 12 = -14.9% ≈ -15%.
        result = compute_resolution(incidents=[_incident(12)], previous_avg=14)

        assert -16.0 <= result.resolution_delta_pct <= -14.0
