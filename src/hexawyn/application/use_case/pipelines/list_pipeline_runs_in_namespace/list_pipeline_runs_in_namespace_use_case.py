from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.response import (
    ListPipelineRunsInNamespaceResponse,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.sort_stuck import (
    find_stuck_runs,
    sort_by_status_then_time,
)


class ListPipelineRunsInNamespaceUseCase:
    """Fetches all PipelineRuns in a namespace, sorts (Failed first), detects stuck runs."""

    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )
