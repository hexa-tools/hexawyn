from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_tracer_port import PipelineTracerPort
from hexawyn.application.use_case.trace_pipeline_run_dag.command import TracePipelineRunDagCommand
from hexawyn.application.use_case.trace_pipeline_run_dag.response import TracePipelineRunDagResponse


class TracePipelineRunDAGUseCase:
    def __init__(self, port: PipelineTracerPort) -> None:
        self._port = port

    def execute(self, c: TracePipelineRunDagCommand) -> TracePipelineRunDagResponse:
        tasks = self._port.trace_dag(pipeline_run_name=c.pipeline_run_name, namespace=c.namespace)
        return TracePipelineRunDagResponse(tasks=[asdict(t) for t in tasks])
