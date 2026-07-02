from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, StepLog


class KubernetesPipelineRunLogsAdapter(PipelineRunLogsPort):
    def fetch_step_logs(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        return []
