"""Unit tests for MCP tool: policy_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyAuditTool:
    def test_policy_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_audit import policy_audit

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
        ):
            result = policy_audit()

        assert isinstance(result, dict)

    def test_policy_audit_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_audit import policy_audit

        with (
            patch(
                "hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = policy_audit()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
