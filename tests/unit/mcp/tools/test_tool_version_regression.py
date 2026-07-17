"""Unit tests for MCP tool: version_regression."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestVersionRegressionTool:
    def test_version_regression_returns_dict(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_version_regression_adapter", return_value=MagicMock()),
        ):
            result = version_regression(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_version_regression_handles_error(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        with (
            patch(
                "hexawyn.mcp.server.build_version_regression_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = version_regression(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.version_regression")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
