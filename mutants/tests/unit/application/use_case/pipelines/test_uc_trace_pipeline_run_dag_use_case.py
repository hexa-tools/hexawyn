from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.command import (
    TracePipelineRunDagCommand,
)
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.response import (
    TracePipelineRunDagResponse,
)
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case import (  # noqa: E501
    TracePipelineRunDagUseCase,
)


class TestTracePipelineRunDagUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pipeline_run.return_value = {
            "name": "run-1",
            "status": "Succeeded",
        }
        port.list_task_runs_for_pipeline.return_value = []

        use_case = TracePipelineRunDagUseCase(port=port)
        result = use_case.trace_pipeline_run_dag(
            TracePipelineRunDagCommand(
                pipeline_run_name="run-1",
                namespace="default",
            )
        )

        assert isinstance(result, TracePipelineRunDagResponse)
