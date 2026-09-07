"""Unit tests for MCP tool: list_openshift_routes."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListOpenshiftRoutesTool:
    def test_list_openshift_routes_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_openshift_routes import list_openshift_routes

        mock_response = MagicMock()
        mock_response.items = []
        mock_response.count = 0
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_openshift_resource_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_openshift_routes.ListOpenshiftRoutesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_openshift_routes()

        assert isinstance(result, dict)
        assert "items" in result

    def test_list_openshift_routes_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_openshift_routes import list_openshift_routes

        with patch(
            "hexawyn.mcp.server.build_openshift_resource_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_openshift_routes()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_openshift_routes")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
