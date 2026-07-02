from abc import ABC, abstractmethod

from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, StepLog


class PipelineRunLogsPort(ABC):
    @abstractmethod
    def fetch_step_logs(self, request: PipelineRunLogsRequest) -> list[StepLog]: ...
