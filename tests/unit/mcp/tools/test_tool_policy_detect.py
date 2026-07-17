"""Unit tests for MCP tool: policy_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyDetectTool:
    def test_policy_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
        ):
            result = policy_detect()

        assert isinstance(result, dict)

    def test_policy_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with (
            patch(
                "hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = policy_detect()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
