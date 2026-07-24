from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.use_case.pipeline_run_logs.command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipeline_run_logs.response import (
    PipelineRunLogsResponse,
)
from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_service_port import (
    PipelineRunLogsServicePort,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, PipelineRunLogsResult


class PipelineRunLogsService(PipelineRunLogsServicePort):
    def __init__(self, port: PipelineRunLogsPort) -> None:
        self._port = port

    def get_logs(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )
