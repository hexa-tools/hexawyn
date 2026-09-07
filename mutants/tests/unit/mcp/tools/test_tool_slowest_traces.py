"""Unit tests for MCP tool: slowest_traces."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSlowestTracesTool:
    def test_slowest_traces_returns_dict(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        mock_response = MagicMock()
        mock_response.pod_name = "test-pod"
        mock_response.slowest_traces = []
        mock_response.total_traces_found = 10
        mock_response.note = ""
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_slow_trace_search_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.slowest_traces.SlowestTracesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = slowest_traces("test-pod")

        assert isinstance(result, dict)
        assert result["pod_name"] == "test-pod"

    def test_slowest_traces_handles_error(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        with patch(
            "hexawyn.mcp.server.build_slow_trace_search_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = slowest_traces("test-pod")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slowest_traces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
