"""Unit tests for MCP tool: diff_helm_values."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDiffHelmValuesTool:
    def test_diff_helm_values_returns_dict(self) -> None:
        from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

        with patch("hexawyn.mcp.server.build_helm_values_diff_adapter", return_value=MagicMock()):
            result = diff_helm_values()

        assert isinstance(result, dict)
        assert "error" in result

    def test_diff_helm_values_handles_error(self) -> None:
        from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

        with patch(
            "hexawyn.mcp.server.build_helm_values_diff_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = diff_helm_values()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_diff_helm_values_success_path(self) -> None:
        from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

        with (
            patch(
                "hexawyn.mcp.server.build_helm_values_diff_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.diff_helm_values.DiffHelmValuesUseCase") as mock_uc,
            patch("hexawyn.mcp.tools.diff_helm_values.DiffHelmValuesCommand"),
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = diff_helm_values()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.diff_helm_values")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
