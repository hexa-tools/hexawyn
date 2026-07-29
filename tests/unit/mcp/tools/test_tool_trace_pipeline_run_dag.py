"""Unit tests for MCP tool: trace_pipeline_run_dag."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestTracePipelineRunDagTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.command"] = (
            MagicMock()
        )

    def test_trace_pipeline_run_dag_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.trace_pipeline_run_dag import trace_pipeline_run_dag

        with patch(
            "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
            return_value=MagicMock(),
        ):
            result = trace_pipeline_run_dag()

        assert isinstance(result, dict)
        assert "error" in result

    def test_trace_pipeline_run_dag_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.trace_pipeline_run_dag import trace_pipeline_run_dag

        with patch(
            "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = trace_pipeline_run_dag()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.trace_pipeline_run_dag")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
