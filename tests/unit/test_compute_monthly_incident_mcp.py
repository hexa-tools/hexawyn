"""RED → GREEN — MCP tool: compute_monthly_incident_report."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.monthly_incident_port import (
    IncidentSnapshotData,
    MonthlyIncidentPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestComputeMonthlyIncidentReportTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=MonthlyIncidentPort)
        mock_port.fetch_incidents.return_value = [
            IncidentSnapshotData(
                incident_id="INC-001",
                service_name="payment-service",
                severity="P1",
                downtime_minutes=45,
                timestamp="2026-07-15T10:00:00Z",
                resolved_at="2026-07-15T10:45:00Z",
                is_planned_maintenance=False,
                reopened=False,
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_monthly_incident_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.compute_monthly_incident_report import (
                compute_monthly_incident_report,
            )

            result = compute_monthly_incident_report(month="2026-07")

        assert result["total_count"] == 1
        assert result["per_severity"]["P1"]["count"] == 1
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_monthly_incident_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_monthly_incident_report import (
                compute_monthly_incident_report,
            )

            result = compute_monthly_incident_report()

        assert result["total_count"] == 0
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import register

        assert callable(register)
