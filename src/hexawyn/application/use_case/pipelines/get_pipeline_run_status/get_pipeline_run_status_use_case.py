from hexawyn.application.ports.driven.tekton_pipeline_status_port import TektonPipelineStatusPort
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


class GetPipelineRunStatusUseCase:
    def __init__(self, port: TektonPipelineStatusPort) -> None:
        self._port = port

    def execute(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)
