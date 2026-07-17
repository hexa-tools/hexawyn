from dataclasses import fields


class TestSlaBreach:
    def test_fields(self) -> None:
        from hexawyn.domain.models.sla_report import SlaBreach

        names = {f.name for f in fields(SlaBreach)}
        assert names == {
            "service_name",
            "date",
            "duration_minutes",
            "impacted_users",
            "root_cause_ref",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.sla_report import SlaBreach

        breach = SlaBreach(
            service_name="checkout-service",
            date="2026-02-14",
            duration_minutes=45,
            impacted_users=1200,
            root_cause_ref="INC-482",
        )

        assert breach.duration_minutes == 45
        assert breach.impacted_users == 1200


class TestServiceSla:
    def test_fields(self) -> None:
        from hexawyn.domain.models.sla_report import ServiceSla

        names = {f.name for f in fields(ServiceSla)}
        assert names == {
            "service_name",
            "sla_target_pct",
            "actual_uptime_pct",
            "met",
            "exceeded",
            "breaches",
            "breach_count",
            "prorated",
            "coverage_days",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.sla_report import ServiceSla

        service = ServiceSla(
            service_name="payment-service",
            sla_target_pct=99.9,
            actual_uptime_pct=99.95,
            met=True,
            exceeded=True,
            breaches=[],
            breach_count=0,
            prorated=False,
            coverage_days=90,
        )

        assert service.actual_uptime_pct == 99.95
        assert service.exceeded is True


class TestSlaReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.sla_report import SlaReport

        report = SlaReport(quarter_label="2026-Q1")

        assert report.quarter_label == "2026-Q1"
        assert report.services == []
        assert report.overall_met_count == 0
        assert report.overall_breached_count == 0
        assert report.trend == "stable"
        assert report.previous_avg_uptime_pct is None
        assert report.current_avg_uptime_pct == 0.0
        assert report.has_data is True
        assert report.warning == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.sla_report import SlaReport

        report = SlaReport(
            quarter_label="2026-Q1",
            overall_met_count=2,
            overall_breached_count=1,
            trend="improving",
            previous_avg_uptime_pct=99.5,
            current_avg_uptime_pct=99.8,
        )

        assert report.overall_met_count == 2
        assert report.trend == "improving"
