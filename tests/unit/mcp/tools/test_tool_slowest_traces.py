"""Unit tests for MCP tool: slowest_traces."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSlowestTracesTool:
    def test_slowest_traces_returns_dict(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_slow_trace_search_adapter", return_value=MagicMock()),
        ):
            result = slowest_traces(pod_name="test-pod_name")

        assert isinstance(result, dict)

    def test_slowest_traces_handles_error(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        with (
            patch(
                "hexawyn.mcp.server.build_slow_trace_search_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = slowest_traces(pod_name="test-pod_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slowest_traces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
