"""Unit tests for MCP tool: policy_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyListTool:
    def test_policy_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
        ):
            result = policy_list()

        assert isinstance(result, dict)

    def test_policy_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        with (
            patch(
                "hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = policy_list()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
