from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.tekton_pipeline_baseline_adapter import (
    TektonPipelineBaselineAdapter,
)


class TestTektonPipelineBaselineAdapter:
    def test_list_pipeline_runs(self) -> None:
        with patch("hexawyn.mcp.server.get_connection") as mock_conn:
            mock_conn.return_value.execute.return_value.fetchall.return_value = []
            adapter = TektonPipelineBaselineAdapter()
            result = adapter.list_pipeline_runs("pipeline-1", "ns", 10)
            assert result == []

    def test_list_pipeline_runs_with_data(self) -> None:
        with patch("hexawyn.mcp.server.get_connection") as mock_conn:
            mock_conn.return_value.execute.return_value.fetchall.return_value = [
                ("run-1", "Succeeded", 120, "2026-01-01T00:00:00Z", "2026-01-01T00:02:00Z"),
            ]
            adapter = TektonPipelineBaselineAdapter()
            result = adapter.list_pipeline_runs("p", "ns", 10)
            assert len(result) == 1
            assert result[0]["name"] == "run-1"
            assert result[0]["status"] == "Succeeded"

    def test_list_task_runs(self) -> None:
        with patch("hexawyn.mcp.server.get_connection") as mock_conn:
            mock_conn.return_value.execute.return_value.fetchall.return_value = []
            adapter = TektonPipelineBaselineAdapter()
            result = adapter.list_task_runs_for_pipeline("ns", "pr-1")
            assert result == []

    def test_list_task_runs_with_data(self) -> None:
        with patch("hexawyn.mcp.server.get_connection") as mock_conn:
            mock_conn.return_value.execute.return_value.fetchall.return_value = [
                ("task-1", "build", "pr-1", 60),
                ("task-2", "test", "pr-1", 90),
            ]
            adapter = TektonPipelineBaselineAdapter()
            result = adapter.list_task_runs_for_pipeline("ns", "pr-1")
            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["task_name"] == "build"
            assert result[1]["duration_seconds"] == 90  # noqa: PLR2004
