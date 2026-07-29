"""Unit tests for MCP tool: check_resource_constraints."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckResourceConstraintsTool:
    def test_check_resource_constraints_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_resource_constraints import check_resource_constraints

        mock_response = MagicMock()
        mock_response.containers = []
        mock_response.summary = "ok"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.check_resource_constraints.CheckResourceConstraintsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = check_resource_constraints()

        assert isinstance(result, dict)
        assert "containers" in result

    def test_check_resource_constraints_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_resource_constraints import check_resource_constraints

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = check_resource_constraints()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_resource_constraints")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
