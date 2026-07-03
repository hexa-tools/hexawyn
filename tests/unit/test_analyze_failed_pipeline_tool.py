from __future__ import annotations

from unittest.mock import MagicMock, patch


def _task_run(
    status: str = "Failed",
    start_time: str = "2024-01-10T15:00:00Z",
    failing_step_error: str | None = "AssertionError: expected 200 got 500",
) -> dict[str, object]:
    return {
        "name": "run-tests",
        "task_ref": "integration-tests",
        "status": status,
        "start_time": start_time,
        "duration": "10s",
        "failing_step": "integration-tests" if status != "Succeeded" else None,
        "failing_step_error": failing_step_error if status != "Succeeded" else None,
    }


class TestAnalyzeFailedPipelineTool:
    def test_returns_analysis(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter") as build_tekton,
            patch("hexawyn.mcp.server.build_pipeline_run_logs_adapter") as build_logs,
        ):
            history = [_task_run()] + [
                _task_run(status="Succeeded", start_time=f"2024-01-{i:02d}T15:00:00Z")
                for i in range(1, 11)
            ]
            tekton_adapter = MagicMock()
            tekton_adapter.list_task_runs.return_value = history
            build_tekton.return_value = tekton_adapter

            logs_adapter = MagicMock()
            logs_adapter.fetch_step_logs.return_value = []
            build_logs.return_value = logs_adapter

            result = analyze_failed_pipeline(pipeline_name="deploy-payment-v3")

        assert result["error"] is None
        assert result["pipeline_name"] == "deploy-payment-v3"
        assert len(result["failures"]) == 1
        assert result["failures"][0]["failure_type"] == "regression"
        assert result["failures"][0]["confidence"] == 0.85

    def test_handles_pipeline_not_found(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=RuntimeError(
                "Pipeline 'ghost' not found or has no TaskRuns in the requested namespace."
            ),
        ):
            result = analyze_failed_pipeline(pipeline_name="ghost")

        assert "not found" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_failed_pipeline")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
