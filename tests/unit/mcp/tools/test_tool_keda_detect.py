"""Unit tests for MCP tool: keda_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestKedaDetectTool:
    def test_keda_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.version = "2.14.0"
        mock_response.namespace = "keda"
        mock_response.total_scaledobjects = 3
        mock_response.ready_scaledobjects = 2
        mock_response.error_scaledobjects = 1
        mock_response.scaled_to_zero_count = 1
        mock_response.total_scaledjobs = 1
        mock_response.managed_namespaces = ["default"]
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.keda_detect.KedaDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = keda_detect()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["error"] is None

    def test_keda_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = keda_detect()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
