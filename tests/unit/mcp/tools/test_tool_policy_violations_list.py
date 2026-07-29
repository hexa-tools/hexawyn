"""Unit tests for MCP tool: policy_violations_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyViolationsListTool:
    def test_policy_violations_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_violations_list import policy_violations_list

        mock_response = MagicMock()
        mock_response.violations = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.policy_violations_list.PolicyViolationsListUseCase",
                return_value=mock_uc,
            ),
        ):
            result = policy_violations_list()

        assert isinstance(result, dict)
        assert "error" in result

    def test_policy_violations_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_violations_list import policy_violations_list

        with patch(
            "hexawyn.mcp.server.build_policy_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = policy_violations_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_violations_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
