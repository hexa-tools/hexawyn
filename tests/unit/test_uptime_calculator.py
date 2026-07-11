from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import ServiceSlaRaw


def _svc(
    uptime: float = 99.9,
    target: float = 99.9,
    coverage: int = 90,
    quarter: int = 90,
    maintenance: int = 0,
) -> ServiceSlaRaw:
    return ServiceSlaRaw(
        service_name="svc",
        sla_target_pct=target,
        uptime_pct=uptime,
        coverage_days=coverage,
        quarter_days=quarter,
        maintenance_minutes=maintenance,
    )


class TestStatus:
    def test_met_when_uptime_equals_target(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=99.9, target=99.9))

        assert result.met is True
        assert result.exceeded is False

    def test_exceeded_when_uptime_above_target(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=99.95, target=99.9))

        assert result.met is True
        assert result.exceeded is True

    def test_breached_when_uptime_below_target(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=99.6, target=99.9))

        assert result.met is False
        assert result.exceeded is False

    def test_hundred_percent_exceeds(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=100.0, target=99.9))

        assert result.exceeded is True


class TestProration:
    def test_prorated_when_coverage_less_than_quarter(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(coverage=45, quarter=90))

        assert result.prorated is True
        assert result.coverage_days == 45

    def test_not_prorated_when_full_coverage(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(coverage=90, quarter=90))

        assert result.prorated is False


class TestMaintenanceExclusion:
    def test_maintenance_minutes_improve_effective_uptime(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        # Raw uptime 99.0% over 90 days; excluding 1 day of planned maintenance
        # raises the effective uptime above the raw figure.
        with_maintenance = evaluate_service(
            _svc(uptime=99.0, target=99.9, coverage=90, quarter=90, maintenance=1440)
        )
        without = evaluate_service(
            _svc(uptime=99.0, target=99.9, coverage=90, quarter=90, maintenance=0)
        )

        assert with_maintenance.actual_uptime_pct > without.actual_uptime_pct

    def test_no_maintenance_keeps_raw_uptime(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=99.6, maintenance=0))

        assert result.actual_uptime_pct == 99.6

    def test_zero_coverage_returns_raw_uptime(self) -> None:
        from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

        result = evaluate_service(_svc(uptime=99.6, coverage=0, quarter=90, maintenance=100))

        assert result.actual_uptime_pct == 99.6
