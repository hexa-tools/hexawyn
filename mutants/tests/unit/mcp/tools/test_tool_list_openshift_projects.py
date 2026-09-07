"""Unit tests for MCP tool: list_openshift_projects."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListOpenshiftProjectsTool:
    def test_list_openshift_projects_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_openshift_projects import list_openshift_projects

        mock_response = MagicMock()
        mock_response.items = []
        mock_response.count = 0
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_openshift_resource_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_openshift_projects.ListOpenshiftProjectsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_openshift_projects()

        assert isinstance(result, dict)
        assert "items" in result

    def test_list_openshift_projects_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_openshift_projects import list_openshift_projects

        with patch(
            "hexawyn.mcp.server.build_openshift_resource_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_openshift_projects()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_openshift_projects")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
