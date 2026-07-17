from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.domain.models.pipeline_run_logs import StepLog, StepStatus


class TestPipelineRunLogsTool:
    def test_returns_logs_with_failed(self) -> None:
        from hexawyn.mcp.tools.pipeline_run_logs import pipeline_run_logs

        with patch("hexawyn.mcp.server.build_pipeline_run_logs_adapter") as m:
            a = MagicMock(spec=PipelineRunLogsPort)
            a.fetch_step_logs.return_value = [
                StepLog(
                    step_name="clone-repo",
                    status=StepStatus.SUCCEEDED,
                    log_lines=["ok"],
                    truncated=False,
                ),
                StepLog(
                    step_name="build-image",
                    status=StepStatus.FAILED,
                    log_lines=["ERROR: no space"],
                    truncated=False,
                ),
            ]
            m.return_value = a
            r = pipeline_run_logs(pipeline_run_name="deploy-payment-v2", namespace="ci")
        assert r["error"] is None
        assert r["pipeline_run_found"] is True
        assert r["failed_step_count"] == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.pipeline_run_logs import pipeline_run_logs

        with patch(
            "hexawyn.mcp.server.build_pipeline_run_logs_adapter", side_effect=RuntimeError("boom")
        ):
            r = pipeline_run_logs(pipeline_run_name="x", namespace="ns")
        assert r["error"] == "boom"


class TestBuildPipelineRunLogsAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.pipeline_run_logs_port import (
            PipelineRunLogsPort,
        )
        from hexawyn.mcp.server import build_pipeline_run_logs_adapter

        assert isinstance(build_pipeline_run_logs_adapter(), PipelineRunLogsPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_run_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
