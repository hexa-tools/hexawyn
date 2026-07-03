from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_response import (
    AnalyzeFailedPipelineResponse,
    FailureAnalysisDict,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_service_port import (
    AnalyzeFailedPipelineServicePort,
)
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
    AnalyzeFailedPipelineResult,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest
from hexawyn.domain.services.failure_analysis.rca import analyze_pipeline_failure


class AnalyzeFailedPipelineService(AnalyzeFailedPipelineServicePort):
    def __init__(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = tekton_port
        self._logs_port = pipeline_run_logs_port

    def analyze(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name, namespace=command.namespace
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return _to_response(result)


def _to_response(result: AnalyzeFailedPipelineResult) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )
