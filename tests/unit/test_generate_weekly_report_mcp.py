"""RED → GREEN — MCP tool: generate_weekly_reliability_report."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    IncidentRawData,
    ServiceReliabilityRawData,
    WeeklyReliabilityReportPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestGenerateWeeklyReliabilityReportTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=WeeklyReliabilityReportPort)
        mock_port.fetch_service_reliability.return_value = [
            ServiceReliabilityRawData(
                service_name="payment-service",
                uptime_pct=99.92,
                error_rate=0.08,
                p99_latency_ms=245.0,
                slo_target=99.9,
                downtime_minutes=0,
                data_gap_minutes=0,
                created_mid_week=False,
            ),
        ]
        mock_port.fetch_incidents.return_value = [
            IncidentRawData(
                service_name="auth-service",
                timestamp="2026-06-13T14:30:00Z",
                duration_minutes=18,
                error_rate=2.0,
                description="503 errors",
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_reliability_report_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.generate_weekly_reliability_report import (
                generate_weekly_reliability_report,
            )

            result = generate_weekly_reliability_report(window_days=7)

        assert result["services"][0]["slo_status"] == "pass"
        assert result["health_score"] == 100.0
        assert result["total_incident_count"] == 1
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_reliability_report_adapter",
            side_effect=ClusterUnreachableError("cluster down"),
        ):
            from hexawyn.mcp.tools.generate_weekly_reliability_report import (
                generate_weekly_reliability_report,
            )

            result = generate_weekly_reliability_report()

        assert result["health_score"] == 0.0
        assert "cluster" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.generate_weekly_reliability_report import register

        assert callable(register)
