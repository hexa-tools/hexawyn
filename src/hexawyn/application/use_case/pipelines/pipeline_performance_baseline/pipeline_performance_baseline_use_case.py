from hexawyn.application.ports.driven.pipeline_baseline_port import PipelineBaselinePort
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.command import (
    PipelinePerformanceBaselineCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.response import (
    PipelinePerformanceBaselineResponse,
)
from hexawyn.domain.services.pipeline_baseline.cicd_performance_baseline_service import (
    compute_baseline,
)


class PipelinePerformanceBaselineUseCase:
    def __init__(self, port: PipelineBaselinePort) -> None:
        self._port = port

    def execute(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )
