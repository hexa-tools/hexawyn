"""Unit tests for MCP tool: rollouts_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRolloutsListTool:
    def test_rollouts_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rollouts_list import rollouts_list

        mock_response = MagicMock()
        mock_response.rollouts = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.rollouts_list.RolloutsListUseCase",
                return_value=mock_uc,
            ),
        ):
            result = rollouts_list()

        assert isinstance(result, dict)
        assert "rollouts" in result

    def test_rollouts_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollouts_list import rollouts_list

        with patch(
            "hexawyn.mcp.server.build_rollouts_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = rollouts_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rollouts_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
