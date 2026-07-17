"""Unit tests for MCP tool: list_pipeline_runs_in_namespace."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPipelineRunsInNamespaceTool:
    def test_list_pipeline_runs_in_namespace_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
            list_pipeline_runs_in_namespace,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
        ):
            result = list_pipeline_runs_in_namespace(namespace="test-ns")

        assert isinstance(result, dict)

    def test_list_pipeline_runs_in_namespace_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
            list_pipeline_runs_in_namespace,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_tekton_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = list_pipeline_runs_in_namespace(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_pipeline_runs_in_namespace")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
