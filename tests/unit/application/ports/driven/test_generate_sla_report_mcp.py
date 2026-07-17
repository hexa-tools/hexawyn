"""RED → GREEN — MCP tool: generate_sla_report."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.sla_report_port import (
    QuarterSlaData,
    ServiceSlaRaw,
    SlaBreachRaw,
    SlaReportPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _svc(name: str, uptime: float, coverage: int = 90) -> ServiceSlaRaw:
    return ServiceSlaRaw(
        service_name=name,
        sla_target_pct=99.9,
        uptime_pct=uptime,
        coverage_days=coverage,
        quarter_days=90,
        maintenance_minutes=0,
    )


def _breach(name: str, date: str, duration: int) -> SlaBreachRaw:
    return SlaBreachRaw(
        service_name=name,
        date=date,
        duration_minutes=duration,
        impacted_users=1200,
        root_cause_ref="INC-482",
        planned_maintenance=False,
    )


def _port(data: QuarterSlaData, previous: float | None = None) -> MagicMock:
    port = MagicMock(spec=SlaReportPort)
    port.get_quarter_sla_data.return_value = data
    port.get_previous_quarter_avg_uptime.return_value = previous
    return port


class TestGenerateSlaReportTool:
    def test_returns_per_service_uptime_and_breaches(self) -> None:
        data = QuarterSlaData(
            has_data=True,
            services=[_svc("payment-service", 99.95), _svc("checkout-service", 99.6)],
            breaches=[
                _breach("checkout-service", "2026-02-14", 15),
                _breach("checkout-service", "2026-02-20", 45),
            ],
        )
        with patch("hexawyn.mcp.server.build_sla_report_adapter", return_value=_port(data)):
            from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

            result = generate_sla_report(quarter="2026-Q1")

        assert result["overall_met_count"] == 1
        assert result["overall_breached_count"] == 1
        checkout = next(s for s in result["services"] if s["service_name"] == "checkout-service")
        assert checkout["breach_count"] == 2
        assert checkout["breaches"][0]["impacted_users"] == 1200
        assert result["error"] is None

    def test_prorated_service_flagged(self) -> None:
        data = QuarterSlaData(
            has_data=True, services=[_svc("auth-service", 99.9, coverage=42)], breaches=[]
        )
        with patch("hexawyn.mcp.server.build_sla_report_adapter", return_value=_port(data)):
            from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

            result = generate_sla_report(quarter="2026-Q1")

        assert result["services"][0]["prorated"] is True

    def test_trend_included(self) -> None:
        data = QuarterSlaData(
            has_data=True, services=[_svc("payment", 99.9), _svc("checkout", 99.9)], breaches=[]
        )
        with patch(
            "hexawyn.mcp.server.build_sla_report_adapter",
            return_value=_port(data, previous=99.5),
        ):
            from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

            result = generate_sla_report(quarter="2026-Q1")

        assert result["trend"] == "improving"

    def test_no_data_warns(self) -> None:
        data = QuarterSlaData(has_data=False, services=[], breaches=[])
        with patch("hexawyn.mcp.server.build_sla_report_adapter", return_value=_port(data)):
            from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

            result = generate_sla_report(quarter="2026-Q1")

        assert result["has_data"] is False
        assert result["warning"] != ""

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_sla_report_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

            result = generate_sla_report(quarter="2026-Q1")

        assert result["services"] == []
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.generate_sla_report import register

        assert callable(register)
