"""Unit tests for MCP tool: detect_recurring_incidents."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectRecurringIncidentsTool:
    def test_detect_recurring_incidents_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import (
            detect_recurring_incidents,
        )

        with patch("hexawyn.mcp.server.build_recurring_incident_adapter", return_value=MagicMock()):
            result = detect_recurring_incidents()

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_recurring_incidents_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import (
            detect_recurring_incidents,
        )

        with patch(
            "hexawyn.mcp.server.build_recurring_incident_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_recurring_incidents()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_detect_recurring_incidents_success_path(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import (
            detect_recurring_incidents,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_recurring_incident_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_recurring_incidents.DetectRecurringIncidentsUseCase"
            ) as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = detect_recurring_incidents()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_recurring_incidents")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
