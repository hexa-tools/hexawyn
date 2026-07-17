"""Unit tests for MCP tool: keda_scaledobject_triggers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestKedaScaledobjectTriggersTool:
    def test_keda_scaledobject_triggers_returns_dict(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_triggers import keda_scaledobject_triggers

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()),
        ):
            result = keda_scaledobject_triggers(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_keda_scaledobject_triggers_handles_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_triggers import keda_scaledobject_triggers

        with (
            patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = keda_scaledobject_triggers(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_scaledobject_triggers")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
