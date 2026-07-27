from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import (
    QuarterSlaData,
    ServiceSlaRaw,
    SlaBreachRaw,
)
from hexawyn.domain.services.sla_report.sla_report_service import (
    SlaReportService,
)


def _make_service_raw(  # noqa: PLR0913
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


def _make_breach(  # noqa: PLR0913
    service_name: str = "api-gateway",
    date: str = "2026-07-01",
    duration_minutes: int = 30,
    impacted_users: int = 500,
    root_cause_ref: str = "INC-001",
    planned_maintenance: bool = False,
) -> SlaBreachRaw:
    return {
        "service_name": service_name,
        "date": date,
        "duration_minutes": duration_minutes,
        "impacted_users": impacted_users,
        "root_cause_ref": root_cause_ref,
        "planned_maintenance": planned_maintenance,
    }


def _make_quarter_data(
    has_data: bool = True,
    services: list[ServiceSlaRaw] | None = None,
    breaches: list[SlaBreachRaw] | None = None,
) -> QuarterSlaData:
    return {
        "has_data": has_data,
        "services": services or [],
        "breaches": breaches or [],
    }


class TestSlaReportService:
    def test_happy_path_generates_report(self) -> None:
        data = _make_quarter_data(
            services=[
                _make_service_raw(service_name="svc-a", uptime_pct=99.95, sla_target_pct=99.9),
                _make_service_raw(service_name="svc-b", uptime_pct=99.95, sla_target_pct=99.9),
            ],
            breaches=[
                _make_breach(service_name="svc-b"),
            ],
        )

        service = SlaReportService()
        report = service.generate(data, "Q2 2026", previous_avg=None)

        assert report.quarter_label == "Q2 2026"
        assert report.has_data is True
        assert len(report.services) == 2  # noqa: PLR2004
        assert report.overall_met_count == 2  # noqa: PLR2004
        assert report.overall_breached_count == 0
        assert report.trend == "stable"

    def test_no_data_returns_warning(self) -> None:
        data = _make_quarter_data(has_data=False)

        service = SlaReportService()
        report = service.generate(data, "Q3 2026", previous_avg=None)

        assert report.has_data is False
        assert "incident" in report.warning.lower()

    def test_breaches_excluding_planned_maintenance(self) -> None:
        data = _make_quarter_data(
            services=[_make_service_raw(service_name="svc-a", uptime_pct=99.5)],
            breaches=[
                _make_breach(service_name="svc-a", duration_minutes=60, planned_maintenance=True),
                _make_breach(service_name="svc-a", duration_minutes=30, planned_maintenance=False),
            ],
        )

        service = SlaReportService()
        report = service.generate(data, "Q2", previous_avg=None)

        assert len(report.services) == 1
        assert report.services[0].breach_count == 1
        assert report.services[0].breaches[0].duration_minutes == 30  # noqa: PLR2004

    def test_empty_services_zero_average(self) -> None:
        data = _make_quarter_data(services=[])

        service = SlaReportService()
        report = service.generate(data, "Q2", previous_avg=None)

        assert report.current_avg_uptime_pct == 0.0
        assert report.overall_met_count == 0
        assert report.overall_breached_count == 0

    def test_trend_classified_from_previous_average(self) -> None:
        data = _make_quarter_data(
            services=[_make_service_raw(uptime_pct=99.9)],
        )

        service = SlaReportService()
        report = service.generate(data, "Q3", previous_avg=99.5)

        assert report.previous_avg_uptime_pct == 99.5  # noqa: PLR2004
        assert report.trend == "improving"

    def test_prorated_service_flag_set(self) -> None:
        data = _make_quarter_data(
            services=[_make_service_raw(coverage_days=45, quarter_days=90)],
        )

        service = SlaReportService()
        report = service.generate(data, "Q2", previous_avg=None)

        assert report.services[0].prorated is True

    def test_service_not_met_counted_as_breached(self) -> None:
        data = _make_quarter_data(
            services=[
                _make_service_raw(service_name="svc-a", uptime_pct=99.95),
                _make_service_raw(service_name="svc-b", uptime_pct=99.5, sla_target_pct=99.9),
            ],
        )

        service = SlaReportService()
        report = service.generate(data, "Q2", previous_avg=None)

        assert report.overall_met_count == 1
        assert report.overall_breached_count == 1

    def test_multiple_breaches_grouped_by_service(self) -> None:
        data = _make_quarter_data(
            services=[_make_service_raw(service_name="svc-a")],
            breaches=[
                _make_breach(service_name="svc-a", date="2026-07-01"),
                _make_breach(service_name="svc-a", date="2026-07-15"),
            ],
        )

        service = SlaReportService()
        report = service.generate(data, "Q2", previous_avg=None)

        assert report.services[0].breach_count == 2  # noqa: PLR2004
