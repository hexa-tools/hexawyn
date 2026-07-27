from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)
from hexawyn.domain.services.platform_reliability.resolution_trend import ResolutionResult


def _make_incident(resolution_minutes: int = 60) -> ReliabilityIncidentRaw:
    return {
        "date": "2026-01-01",
        "severity": "critical",
        "downtime_minutes": 10,
        "resolution_minutes": resolution_minutes,
        "root_cause": "test",
        "resolved": True,
        "planned_maintenance": False,
    }


class TestComputeResolution:
    def test_happy_path_avg_and_improving_trend(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(30),
            _make_incident(50),
        ]
        previous = 100

        result = compute_resolution(incidents, previous)

        assert isinstance(result, ResolutionResult)
        assert result.avg_resolution_minutes == 40  # noqa: PLR2004
        assert result.resolution_delta_pct < 0
        assert result.resolution_trend == "improving"

    def test_no_incidents_avg_zero(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution([], previous_avg=50)

        assert result.avg_resolution_minutes == 0

    def test_previous_none_returns_stable(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(30)]

        result = compute_resolution(incidents, previous_avg=None)

        assert result.resolution_trend == "stable"
        assert result.resolution_delta_pct == 0.0

    def test_previous_zero_returns_stable(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(30)]

        result = compute_resolution(incidents, previous_avg=0)

        assert result.resolution_trend == "stable"
        assert result.resolution_delta_pct == 0.0

    def test_negative_previous_treated_as_zero(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(30)]

        result = compute_resolution(incidents, previous_avg=-1)

        assert result.resolution_delta_pct == 0.0
        assert result.resolution_trend == "stable"

    def test_degrading_trend(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(200),
        ]
        previous = 100

        result = compute_resolution(incidents, previous)

        assert result.resolution_trend == "degrading"
        assert result.resolution_delta_pct > 0

    def test_stable_trend_within_tolerance(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(101),
        ]
        previous = 100

        result = compute_resolution(incidents, previous)

        assert result.resolution_trend == "stable"

    def test_improving_beyond_tolerance(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(90),
        ]
        previous = 100

        result = compute_resolution(incidents, previous)

        assert result.resolution_trend == "improving"

    def test_delta_pct_rounded_to_one_decimal(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(67)]
        previous = 100

        result = compute_resolution(incidents, previous)

        assert result.resolution_delta_pct == round((67 - 100) / 100 * 100, 1)

    def test_single_incident_avg_equals_its_resolution(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [_make_incident(45)]

        result = compute_resolution(incidents, previous_avg=60)

        assert result.avg_resolution_minutes == 45  # noqa: PLR2004

    def test_average_rounded_to_int(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        incidents: list[ReliabilityIncidentRaw] = [
            _make_incident(10),
            _make_incident(12),
            _make_incident(13),
        ]

        result = compute_resolution(incidents, previous_avg=20)

        assert result.avg_resolution_minutes == 12  # noqa: PLR2004

    def test_empty_incidents_with_previous_avg(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution([], previous_avg=42)

        assert result.avg_resolution_minutes == 0
        assert result.resolution_trend == "improving"

    def test_resolution_result_is_dataclass(self) -> None:
        from hexawyn.domain.services.platform_reliability.resolution_trend import (
            compute_resolution,
        )

        result = compute_resolution([_make_incident(30)], previous_avg=60)

        assert hasattr(result, "avg_resolution_minutes")
        assert hasattr(result, "resolution_delta_pct")
        assert hasattr(result, "resolution_trend")
