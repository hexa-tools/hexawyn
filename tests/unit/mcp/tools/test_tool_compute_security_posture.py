"""Unit tests for MCP tool: compute_security_posture."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeSecurityPostureTool:
    def test_compute_security_posture_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_security_posture_adapter", return_value=MagicMock()),
        ):
            result = compute_security_posture()

        assert isinstance(result, dict)

    def test_compute_security_posture_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

        with (
            patch(
                "hexawyn.mcp.server.build_security_posture_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_security_posture()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_security_posture")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
