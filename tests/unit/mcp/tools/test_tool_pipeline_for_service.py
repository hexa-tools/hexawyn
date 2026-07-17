"""Unit tests for MCP tool: pipeline_for_service."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPipelineForServiceTool:
    def test_pipeline_for_service_returns_dict(self) -> None:
        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_pipeline_for_service_adapter", return_value=MagicMock()
            ),
        ):
            result = pipeline_for_service(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_pipeline_for_service_handles_error(self) -> None:
        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with (
            patch(
                "hexawyn.mcp.server.build_pipeline_for_service_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = pipeline_for_service(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_for_service")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
