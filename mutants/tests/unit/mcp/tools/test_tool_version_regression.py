"""Unit tests for MCP tool: version_regression."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestVersionRegressionTool:
    def test_version_regression_returns_dict(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        mock_response = MagicMock()
        mock_response.service_name = "test-svc"
        mock_response.baseline_version = "v1"
        mock_response.current_version = "v2"
        mock_response.verdict = "stable"
        mock_response.p99_delta_pct = 1.0
        mock_response.error_delta_pct = 0.0
        mock_response.flags = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_version_regression_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.version_regression.VersionRegressionUseCase",
                return_value=mock_uc,
            ),
        ):
            result = version_regression("test-svc")

        assert isinstance(result, dict)
        assert result["service_name"] == "test-svc"

    def test_version_regression_handles_error(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        with patch(
            "hexawyn.mcp.server.build_version_regression_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = version_regression("test-svc")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.version_regression")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
