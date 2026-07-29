"""Unit tests for MCP tool: get_namespace_events."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetNamespaceEventsTool:
    def test_get_namespace_events_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_namespace_events import get_namespace_events

        with patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()):
            result = get_namespace_events()

        assert isinstance(result, dict)
        assert "error" in result

    def test_get_namespace_events_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_namespace_events import get_namespace_events

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_namespace_events()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_get_namespace_events_success_path(self) -> None:
        from hexawyn.mcp.tools.get_namespace_events import get_namespace_events

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.tools.get_namespace_events.GetNamespaceEventsUseCase") as mock_uc,
            patch("hexawyn.mcp.tools.get_namespace_events.GetNamespaceEventsCommand"),
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = get_namespace_events()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_namespace_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
