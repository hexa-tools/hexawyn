from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.use_case.pipeline_run_logs.command import PipelineRunLogsCommand
from hexawyn.application.use_case.pipeline_run_logs.response import PipelineRunLogsResponse


class PipelineRunLogsUseCase:
    def __init__(self, port: PipelineRunLogsPort) -> None:
        self._port = port

    def execute(self, c: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        logs = self._port.get_logs(
            pipeline_run_name=c.pipeline_run_name, namespace=c.namespace, task_name=c.task_name
        )
        return PipelineRunLogsResponse(logs=[asdict(log_line) for log_line in logs])
