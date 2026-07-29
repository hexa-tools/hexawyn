"""Unit tests for MCP tool: redundant_calls."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRedundantCallsTool:
    def test_redundant_calls_returns_dict(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        mock_response = MagicMock()
        mock_response.flow = "test-flow"
        mock_response.patterns = []
        mock_response.total_redundant_calls = 0
        mock_response.calculated_waste_ms = 0
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_redundant_call_detection_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.redundant_calls.RedundantCallsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = redundant_calls("test-flow")

        assert isinstance(result, dict)
        assert result["flow"] == "test-flow"

    def test_redundant_calls_handles_error(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        with patch(
            "hexawyn.mcp.server.build_redundant_call_detection_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = redundant_calls("test-flow")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.redundant_calls")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
