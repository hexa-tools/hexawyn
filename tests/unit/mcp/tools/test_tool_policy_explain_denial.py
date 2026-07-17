"""Unit tests for MCP tool: policy_explain_denial."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyExplainDenialTool:
    def test_policy_explain_denial_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_explain_denial import policy_explain_denial

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
        ):
            result = policy_explain_denial(
                resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
            )

        assert isinstance(result, dict)

    def test_policy_explain_denial_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_explain_denial import policy_explain_denial

        with (
            patch(
                "hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = policy_explain_denial(
                resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
            )

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_explain_denial")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
