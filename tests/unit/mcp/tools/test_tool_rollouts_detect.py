"""Unit tests for MCP tool: rollouts_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRolloutsDetectTool:
    def test_rollouts_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rollouts_detect import rollouts_detect

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()),
        ):
            result = rollouts_detect()

        assert isinstance(result, dict)

    def test_rollouts_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollouts_detect import rollouts_detect

        with (
            patch(
                "hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = rollouts_detect()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rollouts_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
