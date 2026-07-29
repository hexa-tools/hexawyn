from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import ServiceSlaRaw
from hexawyn.domain.services.sla_report.uptime_calculator import (
    evaluate_service,
)


def _make_service(  # noqa: PLR0913
    service_name: str = "api-gateway",
    sla_target_pct: float = 99.9,
    uptime_pct: float = 99.95,
    coverage_days: int = 90,
    quarter_days: int = 92,
    maintenance_minutes: int = 0,
) -> ServiceSlaRaw:
    return {
        "service_name": service_name,
        "sla_target_pct": sla_target_pct,
        "uptime_pct": uptime_pct,
        "coverage_days": coverage_days,
        "quarter_days": quarter_days,
        "maintenance_minutes": maintenance_minutes,
    }


class TestEvaluateService:
    def test_happy_path_met_and_exceeded(self) -> None:
        raw = _make_service(
            uptime_pct=99.95, sla_target_pct=99.9, coverage_days=90, quarter_days=90
        )
        result = evaluate_service(raw)

        assert result.actual_uptime_pct == 99.95  # noqa: PLR2004
        assert result.met is True
        assert result.exceeded is True
        assert result.prorated is False
        assert result.coverage_days == 90  # noqa: PLR2004

    def test_uptime_equals_target_met_but_not_exceeded(self) -> None:
        raw = _make_service(uptime_pct=99.9, sla_target_pct=99.9)
        result = evaluate_service(raw)

        assert result.met is True
        assert result.exceeded is False

    def test_uptime_below_target_not_met(self) -> None:
        raw = _make_service(uptime_pct=99.5, sla_target_pct=99.9)
        result = evaluate_service(raw)

        assert result.met is False
        assert result.exceeded is False

    def test_prorated_when_coverage_less_than_quarter(self) -> None:
        raw = _make_service(coverage_days=45, quarter_days=90)
        result = evaluate_service(raw)

        assert result.prorated is True

    def test_not_prorated_when_full_coverage(self) -> None:
        raw = _make_service(coverage_days=90, quarter_days=90)
        result = evaluate_service(raw)

        assert result.prorated is False

    def test_maintenance_minutes_excluded_from_downtime(self) -> None:
        raw = _make_service(uptime_pct=99.0, maintenance_minutes=1440)
        result = evaluate_service(raw)

        assert result.actual_uptime_pct > 99.0  # noqa: PLR2004

    def test_zero_coverage_days_returns_raw_uptime(self) -> None:
        raw = _make_service(uptime_pct=99.9, coverage_days=0)
        result = evaluate_service(raw)

        assert result.actual_uptime_pct == 99.9  # noqa: PLR2004
        assert result.prorated is True

    def test_high_maintenance_can_exceed_100(self) -> None:
        raw = _make_service(uptime_pct=98.0, maintenance_minutes=100000)
        result = evaluate_service(raw)

        assert result.actual_uptime_pct >= 100.0  # noqa: PLR2004
        assert result.met is True

    def test_coverage_days_exceeds_quarter_days(self) -> None:
        raw = _make_service(coverage_days=100, quarter_days=90)
        result = evaluate_service(raw)

        assert result.prorated is False

    def test_negative_coverage_days_returns_raw_uptime(self) -> None:
        raw = _make_service(uptime_pct=95.0, coverage_days=-1)
        result = evaluate_service(raw)

        assert result.actual_uptime_pct == 95.0  # noqa: PLR2004

    def test_result_is_frozen_dataclass(self) -> None:
        raw = _make_service()
        result = evaluate_service(raw)

        assert hasattr(result, "actual_uptime_pct")
        assert hasattr(result, "met")
        assert hasattr(result, "exceeded")
        assert hasattr(result, "prorated")
        assert hasattr(result, "coverage_days")
