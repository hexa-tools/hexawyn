from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.mapper import (
    to_response,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest
from hexawyn.domain.services.failure_analysis.rca import analyze_pipeline_failure


class AnalyzeFailedPipelineUseCase:
    def __init__(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = tekton_port
        self._logs_port = pipeline_run_logs_port

    def execute(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)
