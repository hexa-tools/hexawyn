from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_tracer_port import PipelineTracerPort
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.command import (
    TracePipelineRunDagCommand,
)
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.response import (
    TracePipelineRunDagResponse,
)
from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
    PipelineDAGTracerService,
)


class TracePipelineRunDagUseCase:
    def __init__(self, port: PipelineTracerPort) -> None:
        self._port = port

    def trace_pipeline_run_dag(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore
