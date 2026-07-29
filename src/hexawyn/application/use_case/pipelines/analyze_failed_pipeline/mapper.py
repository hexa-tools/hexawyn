from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
    FailureAnalysisDict,
)
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineResult,
)


def to_response(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
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
