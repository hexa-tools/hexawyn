"""Unit tests for MCP tool: pipeline_for_service."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestPipelineForServiceTool:
    def test_pipeline_for_service_returns_dict(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.pipelines.pipeline_for_service.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with patch(
            "hexawyn.mcp.server.build_pipeline_for_service_adapter",
            return_value=MagicMock(),
        ):
            result = pipeline_for_service("test-service")

        assert isinstance(result, dict)
        assert "error" in result

    def test_pipeline_for_service_handles_error(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.pipelines.pipeline_for_service.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with patch(
            "hexawyn.mcp.server.build_pipeline_for_service_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = pipeline_for_service("test-service")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.pipelines.pipeline_for_service.command"] = (
            MagicMock()
        )
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_for_service")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
