"""Unit tests for MCP tool: detect_zombies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectZombiesTool:
    def test_detect_zombies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_zombies import detect_zombies

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_zombie_detection_adapter", return_value=MagicMock()),
        ):
            result = detect_zombies()

        assert isinstance(result, dict)

    def test_detect_zombies_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_zombies import detect_zombies

        with (
            patch(
                "hexawyn.mcp.server.build_zombie_detection_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_zombies()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_zombies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
