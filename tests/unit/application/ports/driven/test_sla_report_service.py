from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import (
    QuarterSlaData,
    ServiceSlaRaw,
    SlaBreachRaw,
)


def _svc(
    name: str,
    uptime: float,
    target: float = 99.9,
    coverage: int = 90,
    quarter: int = 90,
    maintenance: int = 0,
) -> ServiceSlaRaw:
    return ServiceSlaRaw(
        service_name=name,
        sla_target_pct=target,
        uptime_pct=uptime,
        coverage_days=coverage,
        quarter_days=quarter,
        maintenance_minutes=maintenance,
    )


def _breach(
    name: str,
    date: str,
    duration: int,
    users: int = 500,
    planned: bool = False,
) -> SlaBreachRaw:
    return SlaBreachRaw(
        service_name=name,
        date=date,
        duration_minutes=duration,
        impacted_users=users,
        root_cause_ref="INC-1",
        planned_maintenance=planned,
    )


def _data(
    services: list[ServiceSlaRaw],
    breaches: list[SlaBreachRaw] | None = None,
    has_data: bool = True,
) -> QuarterSlaData:
    return QuarterSlaData(has_data=has_data, services=services, breaches=breaches or [])


class TestHappyPath:
    def test_all_services_above_target_green(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data([_svc("payment", 99.95), _svc("checkout", 99.92)])

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=None)

        assert report.overall_met_count == 2
        assert report.overall_breached_count == 0

    def test_ticket_scenario(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data(
            [_svc("payment-service", 99.95), _svc("checkout-service", 99.6)],
            breaches=[
                _breach("checkout-service", "2026-02-14", 15),
                _breach("checkout-service", "2026-02-20", 45),
            ],
        )

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=None)

        payment = next(s for s in report.services if s.service_name == "payment-service")
        checkout = next(s for s in report.services if s.service_name == "checkout-service")
        assert payment.breach_count == 0
        assert checkout.breach_count == 2


class TestBreachAttribution:
    def test_breaches_attached_to_their_service(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data(
            [_svc("checkout", 99.6)],
            breaches=[_breach("checkout", "2026-02-14", 15), _breach("checkout", "2026-02-14", 30)],
        )

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=None)

        checkout = report.services[0]
        assert checkout.breach_count == 2
        assert len(checkout.breaches) == 2

    def test_planned_maintenance_breach_excluded(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data(
            [_svc("checkout", 99.6)],
            breaches=[
                _breach("checkout", "2026-02-14", 15),
                _breach("checkout", "2026-02-16", 120, planned=True),
            ],
        )

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=None)

        assert report.services[0].breach_count == 1


class TestProration:
    def test_mid_quarter_onboarding_prorated(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data([_svc("auth-service", 99.9, coverage=42, quarter=90)])

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=None)

        assert report.services[0].prorated is True
        assert report.services[0].coverage_days == 42


class TestNoData:
    def test_missing_data_warns(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        report = SlaReportService().generate(
            _data([], has_data=False), quarter="2026-Q1", previous_avg=None
        )

        assert report.has_data is False
        assert report.warning != ""
        assert report.services == []


class TestTrend:
    def test_trend_improving(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        data = _data([_svc("payment", 99.9), _svc("checkout", 99.9)])

        report = SlaReportService().generate(data, quarter="2026-Q1", previous_avg=99.5)

        assert report.previous_avg_uptime_pct == 99.5
        assert report.current_avg_uptime_pct == 99.9
        assert report.trend == "improving"

    def test_empty_services_with_data_flag_yields_zero_average(self) -> None:
        from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService

        report = SlaReportService().generate(
            _data([], has_data=True), quarter="2026-Q1", previous_avg=None
        )

        assert report.current_avg_uptime_pct == 0.0
        assert report.services == []
