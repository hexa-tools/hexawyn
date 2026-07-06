"""RED → GREEN — MCP tool: detect_recurring_incidents."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.recurring_incident_port import (
    IncidentFrequencyData,
    RecurringIncidentPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestDetectRecurringIncidentsTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=RecurringIncidentPort)
        mock_port.fetch_incidents.return_value = [
            IncidentFrequencyData(
                incident_id="INC-001",
                service_name="payment-service",
                root_cause="DB pool exhausted",
                duration_minutes=20,
                timestamp="2026-07-01T10:00:00Z",
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_recurring_incident_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.detect_recurring_incidents import (
                detect_recurring_incidents,
            )

            result = detect_recurring_incidents()

        assert len(result["services"]) == 1
        assert result["services"][0]["service_name"] == "payment-service"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_recurring_incident_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.detect_recurring_incidents import (
                detect_recurring_incidents,
            )

            result = detect_recurring_incidents()

        assert result["services"] == []
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import register

        assert callable(register)
