"""Unit tests for MCP tool: policy_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyListTool:
    def test_policy_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        mock_response = MagicMock()
        mock_response.policies = [{"name": "require-pod-limits", "action": "enforce"}]
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.policy_list.PolicyListUseCase",
                return_value=mock_uc,
            ),
        ):
            result = policy_list()

        assert isinstance(result, dict)
        assert "error" in result
        assert result.get("error") is None
        assert result.get("policies") == [{"name": "require-pod-limits", "action": "enforce"}]

    def test_policy_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        with patch(
            "hexawyn.mcp.server.build_policy_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = policy_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
