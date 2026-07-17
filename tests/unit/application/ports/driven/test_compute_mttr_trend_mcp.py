"""RED → GREEN — MCP tool: compute_mttr_trend."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.mttr_trend_port import (
    IncidentResolutionData,
    MTTRTrendPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestComputeMTTRTrendTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=MTTRTrendPort)
        mock_port.fetch_incidents_by_month.return_value = [
            IncidentResolutionData(
                incident_id="INC-001",
                service_name="payment",
                severity="P1",
                resolution_minutes=45,
                resolved=True,
                root_cause="OOM",
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_mttr_trend_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

            result = compute_mttr_trend(months=["2026-07"])

        assert result["trend"] == "insufficient_data"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_mttr_trend_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

            result = compute_mttr_trend()

        assert result["trend"] == "error"
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_mttr_trend import register

        assert callable(register)
