from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    ListPipelineRunsResponse,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.sort_stats import (
    compute_stats,
    find_outliers,
    start_time_sort_key,
)


class ListPipelineRunsUseCase:
    """Fetches PipelineRuns, sorts, limits, computes stats and flags outliers."""

    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def execute(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )
