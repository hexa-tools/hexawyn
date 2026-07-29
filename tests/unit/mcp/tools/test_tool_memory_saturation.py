"""Unit tests for MCP tool: memory_saturation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMemorySaturationTool:
    def test_memory_saturation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        mock_response = MagicMock()
        mock_response.prediction_window_minutes = 30
        mock_response.critical_pods = []
        mock_response.safe_pod_count = 5
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_memory_saturation_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.memory_saturation.MemorySaturationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = memory_saturation()

        assert isinstance(result, dict)
        assert "critical_pods" in result

    def test_memory_saturation_handles_error(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        with patch(
            "hexawyn.mcp.server.build_memory_saturation_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = memory_saturation()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.memory_saturation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
