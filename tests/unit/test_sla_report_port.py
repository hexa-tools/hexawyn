from abc import ABC


class TestSlaReportPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import SlaReportPort

        assert issubclass(SlaReportPort, ABC)

    def test_declares_required_methods(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import SlaReportPort

        expected = {"get_quarter_sla_data", "get_previous_quarter_avg_uptime"}

        assert expected <= SlaReportPort.__abstractmethods__


class TestRawTypedDicts:
    def test_service_sla_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import ServiceSlaRaw

        raw: ServiceSlaRaw = {
            "service_name": "checkout-service",
            "sla_target_pct": 99.9,
            "uptime_pct": 99.6,
            "coverage_days": 90,
            "quarter_days": 90,
            "maintenance_minutes": 0,
        }

        assert raw["service_name"] == "checkout-service"
        assert raw["coverage_days"] == 90

    def test_sla_breach_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import SlaBreachRaw

        raw: SlaBreachRaw = {
            "service_name": "checkout-service",
            "date": "2026-02-14",
            "duration_minutes": 45,
            "impacted_users": 1200,
            "root_cause_ref": "INC-482",
            "planned_maintenance": False,
        }

        assert raw["duration_minutes"] == 45
        assert raw["planned_maintenance"] is False

    def test_quarter_sla_data_shape(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData

        data: QuarterSlaData = {
            "has_data": True,
            "services": [],
            "breaches": [],
        }

        assert data["has_data"] is True
